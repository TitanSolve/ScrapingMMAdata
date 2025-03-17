from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

import requests
from bs4 import BeautifulSoup
import csv

# List of fighter URLs (Replace this with your actual list of fighter URLs)
fighter_urls = [
    'https://www.sherdog.com/fighter/Sharabutdin-Magomedov-309711',
    'https://www.sherdog.com/fighter/Michael-Page-91937',
    'https://www.sherdog.com/fighter/Kevin-Lee-84342',
    'https://www.sherdog.com/fighter/Sean-Strickland-30452',
    'https://www.sherdog.com/fighter/Alex-Pereira-224511',
    'https://www.sherdog.com/fighter/Dricus-Du-Plessis-146193',
    'https://www.sherdog.com/fighter/Philip-Keller-158979',
    'https://www.sherdog.com/fighter/Jailton-Almeida-114657',
    'https://www.sherdog.com/fighter/Tom-Aspinall-65231',
    'https://www.sherdog.com/fighter/Jiri-Prochazka-97529',
    'https://www.sherdog.com/fighter/Dricus-Du-Plessis-146193',
    'https://www.sherdog.com/fighter/Yves-Landu-63101',
    'https://www.sherdog.com/fighter/Michael-Page-91937',
    'https://www.sherdog.com/fighter/Dricus-Du-Plessis-146193',
    'https://www.sherdog.com/fighter/Sean-Strickland-30452',
    'https://www.sherdog.com/fighter/Tatiana-Suarez-161107',
    'https://www.sherdog.com/fighter/Weili-Zhang-186663',
    'https://www.sherdog.com/fighter/Dakota-Ditcheva-320485',
    'https://www.sherdog.com/fighter/Dovletdzhan-Yagshimuradov-96307',
    'https://www.sherdog.com/fighter/Shamil-Musaev-119289',
    'https://www.sherdog.com/fighter/Denis-Goltsov-72521',
    'https://www.sherdog.com/fighter/Timur-Khizriev-258185',
    'https://www.sherdog.com/fighter/Cong-Wang-413126'
    # Add more fighter URLs here
]

# Custom headers to mimic a browser
headers = {
    'User-Agent': '(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49'
}

# Function to scrape data for a single fighter
def scrape_fighter_data(fighter_url):
    response = requests.get(fighter_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve data for {fighter_url}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Scrape personal data (name, birthdate, height, weight, etc.)
    fighter_name = soup.find('span', class_='fn').text.strip()
    status_table = soup.find('div', class_='bio-holder').find('table')
    td_tags = status_table.find_all('tr')
    
    birthDate = td_tags[0].find_all('td')[1].find('span', itemprop='birthDate').text.strip()
    height = td_tags[1].find_all('td')[1].find('b', itemprop='height').text.strip()
    weight = td_tags[2].find_all('td')[1].find('b', itemprop='weight').text.strip()
    wins = soup.find('div', class_="winloses win").find_all('span')[1].text.strip()
    lose = soup.find('div', class_="winloses lose").find_all('span')[1].text.strip()

    Win_ko = soup.find('div', class_="wins").find_all('div', class_='meter')[0].find_all('div', class_="pl")[0].text.strip()
    Win_Tko_rate = soup.find('div', class_="wins").find_all('div', class_='meter')[0].find_all('div', class_="pr")[0].text.strip()
    Win_submission = soup.find('div', class_="wins").find_all('div', class_='meter')[1].find_all('div', class_="pl")[0].text.strip()
    Win_submission_rate = soup.find('div', class_="wins").find_all('div', class_='meter')[1].find_all('div', class_="pr")[0].text.strip()
    Win_decisions = soup.find('div', class_="wins").find_all('div', class_='meter')[2].find_all('div', class_="pl")[0].text.strip()
    Win_decisions_rate = soup.find('div', class_="wins").find_all('div', class_='meter')[2].find_all('div', class_="pr")[0].text.strip()

    Lose_ko = soup.find('div', class_="loses").find_all('div', class_='meter')[0].find_all('div', class_="pl")[0].text.strip()
    Lose_Tko_rate = soup.find('div', class_="loses").find_all('div', class_='meter')[0].find_all('div', class_="pr")[0].text.strip()
    Lose_submission = soup.find('div', class_="loses").find_all('div', class_='meter')[1].find_all('div', class_="pl")[0].text.strip()
    Lose_submission_rate = soup.find('div', class_="loses").find_all('div', class_='meter')[1].find_all('div', class_="pr")[0].text.strip()
    Lose_decisions = soup.find('div', class_="loses").find_all('div', class_='meter')[2].find_all('div', class_="pl")[0].text.strip()
    Lose_decisions_rate = soup.find('div', class_="loses").find_all('div', class_='meter')[2].find_all('div', class_="pr")[0].text.strip()

    # Fight history
    fight_history_table = soup.find('table', class_="new_table fighter").find_all('tr')

    fight_history = []
    for i in range(1, len(fight_history_table)):  # Skip the header row
        final_result = fight_history_table[i].find('span', class_="final_result").text.strip()
        opponent_name = fight_history_table[i].find_all('td')[1].find('a').text.strip()
        event = fight_history_table[i].find_all('td')[2].find('a').text.strip()
        event_time = fight_history_table[i].find_all('td')[2].find('span', class_="sub_line").text.strip()
        win_by = fight_history_table[i].find_all('td')[3].find_all('b')[0].text.strip()
        round = fight_history_table[i].find_all('td')[4].text.strip()
        win_time = fight_history_table[i].find_all('td')[5].text.strip()

        fight_history.append([final_result, opponent_name, event, event_time, win_by, round, win_time])

    # Return all the scraped data
    return {
        'fighter_name': fighter_name,
        'birth_date': birthDate,
        'height': height,
        'weight': weight,
        'wins': wins,
        'lose': lose,
        'Win_KO': Win_ko,
        'Win_TKO_rate': Win_Tko_rate,
        'Win_submission': Win_submission,
        'Win_submission_rate': Win_submission_rate,
        'Win_decisions': Win_decisions,
        'Win_decisions_rate': Win_decisions_rate,
        'Lose_KO': Lose_ko,
        'Lose_TKO_rate': Lose_Tko_rate,
        'Lose_submission': Lose_submission,
        'Lose_submission_rate': Lose_submission_rate,
        'Lose_decisions': Lose_decisions,
        'Lose_decisions_rate': Lose_decisions_rate,
        'fight_history': fight_history
    }

# Function to write data to CSV file
def write_to_csv(fighter_data_list):
    # Open the CSV file and create a writer
    with open('fighters_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow([
            'Fighter Name', 'Birth Date', 'Height', 'Weight', 'Wins', 'Losses', 'Win KO', 'Win TKO Rate',
            'Win Submission', 'Win Submission Rate', 'Win Decisions', 'Win Decisions Rate',
            'Lose KO', 'Lose TKO Rate', 'Lose Submission', 'Lose Submission Rate', 'Lose Decisions', 'Lose Decisions Rate',
            'Final Result', 'Opponent Name', 'Event', 'Event Time', 'Win By', 'Round', 'Win Time'
        ])

        # Write data for all fighters
        for fighter_data in fighter_data_list:
            # Write the personal data
            personal_data = [
                fighter_data['fighter_name'], fighter_data['birth_date'], fighter_data['height'], fighter_data['weight'],
                fighter_data['wins'], fighter_data['lose'], fighter_data['Win_KO'], fighter_data['Win_TKO_rate'],
                fighter_data['Win_submission'], fighter_data['Win_submission_rate'], fighter_data['Win_decisions'],
                fighter_data['Win_decisions_rate'], fighter_data['Lose_KO'], fighter_data['Lose_TKO_rate'],
                fighter_data['Lose_submission'], fighter_data['Lose_submission_rate'], fighter_data['Lose_decisions'],
                fighter_data['Lose_decisions_rate']
            ]

            # Write fight history
            for fight in fighter_data['fight_history']:
                row = personal_data + fight
                writer.writerow(row)

# Main function to scrape data for all fighters
def scrape_all_fighters(fighter_urls):
    all_fighter_data = []
    
    for url in fighter_urls:
        print(f"Scraping data for {url}...")
        fighter_data = scrape_fighter_data(url)
        if fighter_data:
            all_fighter_data.append(fighter_data)
        # Sleep to avoid hitting the server too quickly
        time.sleep(1)

    # After collecting all data, write to CSV
    write_to_csv(all_fighter_data)
    print("Data saved to 'fighters_data.csv'.")

# Scrape all the fighters
scrape_all_fighters(fighter_urls)