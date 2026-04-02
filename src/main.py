from scraper_service import run_scrape

search_type = input("Select an option:\n 1. Basic search\n 2. No website search\n>> ")
if search_type != "1" and search_type != "2":
    print("Invalid option.")
    exit()
query = input("Search query: ")
if query == "":
    print("Search query cannot be empty.")
    exit()
location = input("Location: ")
if location == "":
    print("Location cannot be empty.")
    exit()
max_results = int(input("Max results: "))
if max_results <= 0:
    print("Max results must be greater than 0.")
    exit()
    
print("Running search...")

def search(query=None, location=None, max_results=None, website_search=False):
    run_scrape(
        search_query=query,
        city=location,
        max_results=max_results,
        output_path='results.csv',
        append=True,
        website_search=website_search,
    )

if search_type == "1":
    search(query=query, location=location, max_results=max_results, website_search=False)
elif search_type == "2":
    search(query=query, location=location, max_results=max_results, website_search=True)