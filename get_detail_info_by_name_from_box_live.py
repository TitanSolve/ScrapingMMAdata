import requests
from bs4 import BeautifulSoup
import time
import json

# List of boxer names
boxers = [
    "Abass Baraou"
]

# Headers to mimic a real browser request
headers = {"User-Agent": "Chrome/133.0.6943.127"}

# Function to get boxer details from profile page
def get_boxer_details(profile_url):
    response = requests.get(profile_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    details = {"Profile URL": profile_url}
    
    print(f"details={details}")
    datas = soup.find_all(class_=["stats-row__content text-left ml-3 headings-text-color h-100"]);
    print( len(datas))
    
    # Extracting general info (Modify this part if structure changes)
    for row in datas:  
        
        print(row)
        
        cells = row.find_all("td")
        if len(cells) == 2:
            key = cells[0].get_text(strip=True)
            value = cells[1].get_text(strip=True)
            details[key] = value
    
    return details

# Scrape details for each boxer
boxer_data = {}

for boxer in boxers:
    print(f"Fetching profile for: {boxer}...")    
    profile_url = f"https://box.live/boxers/{boxer.replace(' ', '-')}/"
    
    print(profile_url)
    
    if profile_url:
        details = get_boxer_details(profile_url)
        boxer_data[boxer] = details
    else:
        print(f"Profile not found for {boxer}.")
    
    time.sleep(2)  # Delay to prevent being blocked

# Save to JSON file
with open("boxer_details.json", "w", encoding="utf-8") as file:
    json.dump(boxer_data, file, indent=4)

print("Scraping completed. Data saved to boxer_details.json.")
