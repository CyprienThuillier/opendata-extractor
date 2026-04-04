from scraper_service import run_scrape
import argparse

# Argparse version
parser = argparse.ArgumentParser(description="Scrape search results")
parser.add_argument("--query", "-q", type=str, required=True, help="Search query")
parser.add_argument("--location", "-l", type=str, required=True, help="Location")
parser.add_argument("--max-results", "-m", type=int, required=True, help="Max results")
parser.add_argument("--website-search", "-w", action="store_true", help="Enable website search")
parser.add_argument("--output", "-o", type=str, default="results.csv", help="Output file path")
parser.add_argument("--append", "-a", action="store_true", help="Append to existing file")
args = parser.parse_args()
query = args.query
location = args.location
max_results = args.max_results
website_search = args.website_search
output_path = args.output
append = args.append

# Without argparse version
# search_type = input("Select an option:\n 1. Basic search\n 2. No website search\n>> ")
# if search_type != "1" and search_type != "2":
#     print("Invalid option.")
#     exit()
# query = input("Search query: ")
# if query == "":
#     print("Search query cannot be empty.")
#     exit()
# location = input("Location: ")
# if location == "":
#     print("Location cannot be empty.")
#     exit()
# max_results = int(input("Max results: "))
# if max_results <= 0:
#     print("Max results must be greater than 0.")
#     exit()
    
print("Running search...")

def search(query=None, location=None, max_results=None, website_search=False, output_path="results.csv", append=True):
    run_scrape(
        search_query=query,
        city=location,
        max_results=max_results,
        output_path=output_path,
        append=append,
        website_search=website_search,
    )

if not website_search:
    search(query=query, location=location, max_results=max_results, website_search=False, output_path=output_path, append=append)
elif website_search:
    search(query=query, location=location, max_results=max_results, website_search=True, output_path=output_path, append=append)