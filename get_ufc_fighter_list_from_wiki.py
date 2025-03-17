import requests
from bs4 import BeautifulSoup

def scrape_fighter_list_from_wiki(category="UFC_fighters"):
    url = f"https://en.wikipedia.org/wiki/Category:{category}"

    # Send GET request
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all links within the category
        fighter_links = soup.find_all('a', href=True)
        
        # Extract fighter names and URLs
        fighters = []
        for link in fighter_links:
            title = link.get('title')
            # if title and "fighter" in title:
            fighters.append(title)
        
        # Print out the list of fighters
        print(f"Fighters in category {category}:")
        for fighter in fighters:
            print(f"- {fighter}")
    else:
        print(f"Failed to retrieve data from {url}")

# Example: Scraping UFC Fighters list
scrape_fighter_list_from_wiki("Ultimate_Fighting_Championship_male_fighters")