import requests
from bs4 import BeautifulSoup

# URL of the Sherdog fighter's profile
url = 'https://www.sherdog.com/fighter/Sharabutdin-Magomedov-309711'

# Custom headers to mimic a browser
headers = {
    'User-Agent': '(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49'
}

# Send GET request with headers
response = requests.get(url, headers=headers)

# Check if the page was successfully fetched
if response.status_code == 200:
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Scrape the fighter's name
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

    fight_history_table = soup.find('table', class_="new_table fighter").find_all('tr')
    
    for i in range(len(fight_history_table)):
        if i == 0:
            continue
        final_result = fight_history_table[i].find('span', class_="final_result").text.strip()
        opponent_name = fight_history_table[i].find_all('td')[1].find('a').text.strip()
        event = fight_history_table[i].find_all('td')[2].find('a').text.strip()
        event_time = fight_history_table[i].find_all('td')[2].find('span', class_="sub_line").text.strip()
        win_by = fight_history_table[i].find_all('td')[3].find_all('b')[0].text.strip()
        round = fight_history_table[i].find_all('td')[4].text.strip()
        win_time = fight_history_table[i].find_all('td')[5].text.strip()
        print(f"final_result = {final_result}")
        print(f"opponent_name = {opponent_name}")
        print(f"event = {event}")
        print(f"event_time = {event_time}")
        print(f"win_by = {win_by}")
        print(f"round = {round}")
        print(f"win_time = {win_time}")
        print(f"=" * 50)
    
    
    # Print out the scraped data
    print(f"Fighter: {fighter_name}")
    print(f"birthDate: {birthDate}")
    print(f"height: {height}")
    print(f"weight: {weight}")
    print(f"wins: {wins}")
    print(f"lose: {lose}")

    print(f"Win_KO: {Win_ko}")
    print(f"Win_TKO_rate: {Win_Tko_rate}")
    print(f"Win_Submission: {Win_submission}")
    print(f"Win_Submission_rate: {Win_submission_rate}")
    print(f"Win_decisions: {Win_decisions}")
    print(f"Win_decisions_rate: {Win_decisions_rate}")



    print(f"Lose_KO: {Lose_ko}")
    print(f"Lose_TKO_rate: {Lose_Tko_rate}")
    print(f"Lose_Submission: {Lose_submission}")
    print(f"Lose_Submission_rate: {Lose_submission_rate}")
    print(f"Lose_decisions: {Lose_decisions}")
    print(f"Lose_decisions_rate: {Lose_decisions_rate}")
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
    