from scraper_service import run_scrape

def search():
    search_query = input("Search query: ")
    city = input("City: ")
    max_results = int(input("Max results: "))
    output_path = input("Output path (e.g. results.csv): ")
    append = input("Append to existing file? (y/n): ").lower() == "y"

    run_scrape(
        search_query=search_query,
        city=city,
        max_results=max_results,
        output_path=output_path,
        append = True if append else False
    )

def batch_search():
    max_results = 200
    output_path = "export.csv"
    append = True
    cities = ["Calais", "Boulogne-sur-Mer", "Dunkerque", "Amiens", "Creil"]
    queries = ["restaurant"]

    for city in cities:
        for query in queries:
            run_scrape(
                search_query=query,
                city=city,
                max_results=max_results,
                output_path=output_path,
                append = True if append else False
            )
            
if __name__ == "__main__":
    batch_search()
