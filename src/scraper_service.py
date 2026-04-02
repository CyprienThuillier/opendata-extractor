import asyncio
import time
from analyser import analyze
from export import export_file

def run_scrape(
    search_query: str,
    city: str,
    max_results: int,
    output_path: str,
    on_result=None,
    existing_urls: set = None,
    append: bool = False,
    website_search: bool = False,
):
    return asyncio.run(
        _run_async(search_query, city, max_results, output_path, on_result, existing_urls or set(), append, website_search)
    )

async def _run_async(search_query, city, max_results, output_path, on_result, existing_urls, append, website_search):
    from playwright.async_api import async_playwright
    import asyncio as aio

    all_urls = set()
    all_results = []
    init_time = int(time.time())

    async with async_playwright() as pw:
      browser = await pw.firefox.launch(headless=True)
      sem = aio.Semaphore(3)

      page = await browser.new_page()
      query = f"{search_query} {city}".strip()
      await page.goto(f"https://www.google.com/maps/search/{query}")
      try:
        for label in ["Tout refuser", "Tout accepter", "Accept all"]:
          try:
            await page.get_by_role("button", name=label).click(timeout=3000)
            await page.wait_for_load_state("networkidle", timeout=5000)
            break
          except Exception:
            pass
      except Exception:
        pass
      await page.wait_for_selector("a.hfpxzc", timeout=30000)
      feed = page.locator("div[role='feed']")
      previous = 0
      while len(all_urls) < max_results:
        await feed.evaluate("el => el.scrollTo(0, el.scrollHeight)")
        await page.wait_for_timeout(2000)
        items = page.locator("a.hfpxzc")
        count = await items.count()
        if count == previous:
          break
        previous = count
        for i in range(count):
          href = await items.nth(i).get_attribute("href")
          if href and href not in all_urls and href not in existing_urls:
            all_urls.add(href)
          if len(all_urls) >= max_results:
            break
      await page.close()

      new_urls = list(all_urls)[:max_results]
      print(f"[Scraper] Collected {len(new_urls)} new URLs")

      tasks = [analyze(browser, url, 3, sem, search_query) for url in new_urls]
      results = await aio.gather(*tasks)
      if not website_search:
        valid = [r for r in results if r is not None]
      else:
        valid = [r for r in results if r is not None and not r.get("website")]

      export_file(valid, filename=output_path, append=append)
      if on_result:
        for r in valid:
          on_result(r)
      all_results.extend(valid)

      await browser.close()

    elapsed = int(time.time()) - init_time
    print(f"Done in {elapsed // 60:02d}m{elapsed % 60:02d}s — {len(all_results)} results")
    return all_results
