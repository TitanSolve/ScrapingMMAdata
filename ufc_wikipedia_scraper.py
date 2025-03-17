import requests
from bs4 import BeautifulSoup
import csv

def fetch_ufc_event_data(event_number):
    url = f"https://en.wikipedia.org/wiki/UFC_{event_number}"
    print(f"Fetching UFC {event_number} data...")
    page = requests.get(url)
    
    if page.status_code != 200:
        print(f"Failed to fetch page for UFC {event_number}. HTTP Status Code: {page.status_code}")
        return None
    
    soup = BeautifulSoup(page.content, "html.parser")
    
    # Extract the event title
    try:
        event_title = soup.find('h1', {'id': 'firstHeading'}).get_text(strip=True)
        print(f"Event title: {event_title}")
    except AttributeError:
        print(f"Failed to fetch event title for UFC {event_number}")
        return None
    
    # Look for the fight result tables
    fight_results = soup.find_all("table", {"class": "toccolours"})
    
    if not fight_results:
        print(f"Warning: No fight results found for UFC {event_number}.")
        return event_title, []
    
    # Extract fight results from the tables
    fight_data = []
    for table in fight_results:
        rows = table.find_all("tr")
        for row in rows[1:]:  # Skip the header row
            cols = row.find_all("td")
            if len(cols) >= 4:  # Ensure we have enough columns (e.g., fighter names, result, etc.)
                weight_class = cols[0].get_text(strip=True)
                fighter_1 = cols[1].get_text(strip=True)
                result = cols[2].get_text(strip=True)
                fighter_2 = cols[3].get_text(strip=True)
                method = cols[4].get_text(strip=True)
                round = cols[5].get_text(strip=True)
                time = cols[6].get_text(strip=True)
                
                fight_data.append([weight_class, fighter_1, result, fighter_2, method, round, time])
    
    if not fight_data:
        print(f"Warning: No detailed fight data found for UFC {event_number}.")
    
    return event_title, fight_data

def save_fight_results_to_csv(fight_results, filename):
    if fight_results:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(['Event Title', 'Weight Class', 'Fighter 1','Result', 'Fighter 2', 'Method', 'Round', 'Time'])  # Adjust header as needed
            for result in fight_results:
                writer.writerow(result)
        print(f"CSV saved to {filename}")
    else:
        print("No data to save.")

def main():
    # List of UFC events you want to fetch (you can add more UFC event numbers here)
    ufc_events = list(range(1, 310))
    
    all_fight_results = []
    
    for event_number in ufc_events:
        event_title, fight_results = fetch_ufc_event_data(event_number)
        
        if event_title and fight_results:
            print(f"Fetched data for {event_title} ({event_number}) with {len(fight_results)} fight results.")
            for fight in fight_results:
                all_fight_results.append([event_title] + fight)
        else:
            print(f"No fight data found for UFC {event_number}.")
    
    # Save the results to CSV if any data was collected
    if all_fight_results:
        save_fight_results_to_csv(all_fight_results, 'ufc_fight_results.csv')
    else:
        print("No fight results were available for any of the events.")

if __name__ == "__main__":
    main()
