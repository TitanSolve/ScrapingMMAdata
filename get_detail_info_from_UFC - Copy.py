import requests
from bs4 import BeautifulSoup
import csv
import time

# List of UFC fighter URLs (replace these with actual fighter URLs)
fighter_urls = [

    # Add more URLs here
]

# Custom headers to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.6943.54 Safari/537.36'
}

# Function to scrape detailed data of a single fighter from UFC website
def scrape_ufc_fighter_data(fighter_url):
    response = requests.get(fighter_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve data for {fighter_url}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')


    # Scrape fighter's name
    fighter_name = "N/A"
    try:
        fighter_name = soup.find('h1', class_='hero-profile__name').text.strip()
    except AttributeError:
        pass
    division = "N/A"
    try:
        division = soup.find('p', class_='hero-profile__division-title').text.strip()
    except AttributeError:
        pass
    total_status = "N/A"
    try:
        total_status = soup.find('p', class_='hero-profile__division-body').text.strip()
    except AttributeError:
        pass
    win_by_knockout = "N/A"
    win_by_submission = "N/A"
    title_defence = "N/A"
    try:
        win_by_knockout = soup.find_all('div', class_='hero-profile__stat')[0].find_all('p')[0].text.strip()
    except IndexError:
        pass
    
    try:
        win_by_submission = soup.find_all('div', class_='hero-profile__stat')[1].find_all('p')[0].text.strip()
    except IndexError:
        pass
    
    try:
        title_defence = soup.find_all('div', class_='hero-profile__stat')[2].find_all('p')[0].text.strip()
    except IndexError:
        pass
        
    striking_accuracy = "N/A"
    sig_Strikes_landed = "N/A"
    sig_Strikes_attempted = "N/A"
    
    try:
        striking_accuracy = soup.find_all('div','e-chart-circle__wrapper')[0].find_all('title')[0].text.replace("Striking accuracy", "").replace("%", "").strip()
    except IndexError:
        pass
    
    try:
        sig_Strikes_attempted = soup.find_all('dd', class_='c-overlap__stats-value')[1].text.strip()
    except IndexError:
        pass
    
    try:
        sig_Strikes_landed = soup.find_all('dd', class_='c-overlap__stats-value')[0].text.strip()
    except IndexError:
        pass
    
    takeDown_accuracy = "N/A"
    takeDown_landed = "N/A"
    takeDown_attempted = "N/A"
    
    try:
        takeDown_accuracy = soup.find_all('div','e-chart-circle__wrapper')[1].find_all('title')[0].text.replace("Takedown Accuracy", "").replace("%", "").strip()
    except IndexError:
        pass
    
    try:
        takeDown_landed = soup.find_all('dd', class_='c-overlap__stats-value')[2].text.strip()
    except IndexError:
        pass
    
    try:
        takeDown_attempted = soup.find_all('dd', class_='c-overlap__stats-value')[3].text.strip()    
    except IndexError:
        pass
    
    # if len(soup.find_all('div','e-chart-circle__wrapper')) > 1:
    #     takeDown_accuracy = soup.find_all('div','e-chart-circle__wrapper')[1].find_all('title')[0].text.replace("Takedown Accuracy", "").replace("%", "").strip()
    #     takeDown_landed = soup.find_all('dd', class_='c-overlap__stats-value')[2].text.strip()
    #     takeDown_attempted = soup.find_all('dd', class_='c-overlap__stats-value')[3].text.strip()    
    
    sig_str_landed_per_min = "N/A"
    sig_str_absorbed_per_min = "N/A"
    takeDown_avg_per_15_min = "N/A"
    
    submission_avg_per_15_min = "N/A"
    sig_str_defence = "N/A"
    
    try:
        sig_str_landed_per_min = soup.find_all('div', class_='c-stat-compare__number')[0].text.strip()
    except IndexError:
        pass
    
    try:
        sig_str_absorbed_per_min = soup.find_all('div', class_='c-stat-compare__number')[1].text.strip()
    except IndexError:
        pass
    
    try:
        takeDown_avg_per_15_min = soup.find_all('div', class_='c-stat-compare__number')[2].text.strip()
    except IndexError:
        pass
    
    try:
        submission_avg_per_15_min = soup.find_all('div', class_='c-stat-compare__number')[3].text.strip()
    except IndexError:
        pass
    
    try:
        sig_str_defence = soup.find_all('div', class_='c-stat-compare__number')[4].text.strip()
    except IndexError:
        pass
    
    # sig_str_landed_per_min = soup.find_all('div', class_='c-stat-compare__number')[0].text.strip()
    # sig_str_absorbed_per_min = soup.find_all('div', class_='c-stat-compare__number')[1].text.strip()
    # takeDown_avg_per_15_min = soup.find_all('div', class_='c-stat-compare__number')[2].text.strip()
    # submission_avg_per_15_min = soup.find_all('div', class_='c-stat-compare__number')[3].text.strip()
    # sig_str_defence = soup.find_all('div', class_='c-stat-compare__number')[4].text.strip()
    
    takeDown_defence = "N/A"
    knockdown_avg = "N/A"
    avg_fight_fime = "N/A"
        
    if len(soup.find_all('div', class_='c-stat-compare__number')) < 8:
        try:
            knockdown_avg = soup.find_all('div', class_='c-stat-compare__number')[5].text.strip()
        except IndexError:
            pass
        
        try:
            avg_fight_fime = soup.find_all('div', class_='c-stat-compare__number')[6].text.strip()
        except IndexError:
            pass
    else:
        try:
            takeDown_defence = soup.find_all('div', class_='c-stat-compare__number')[5].text.strip()
        except IndexError:
            pass
        try:
            knockdown_avg = soup.find_all('div', class_='c-stat-compare__number')[6].text.strip()
        except IndexError:
            pass
        try:
            avg_fight_fime = soup.find_all('div', class_='c-stat-compare__number')[7].text.strip()
        except IndexError:
            pass
    
    sig_str_by_position_standing = "N/A"
    sig_str_by_position_clinch = "N/A"
    sig_str_by_position_ground = "N/A"
    win_by_method_KO_TKO = "N/A"
    win_by_method_DEC = "N/A"
    win_by_method_SUB = "N/A"
    sig_str_by_target_head = "N/A"
    sig_str_by_target_head_percent = "N/A"
    sig_str_by_target_body = "N/A"
    sig_str_by_target_body_percent = "N/A"
    sig_str_by_target_leg = "N/A"
    sig_str_by_target_leg_percent = "N/A"

    try:        
        sig_str_by_position_standing = soup.find_all('div', class_='c-stat-3bar__value')[0].text.strip()
    except IndexError:
        pass
    
    try:
        sig_str_by_position_clinch = soup.find_all('div', class_='c-stat-3bar__value')[1].text.strip()
    except IndexError:
        pass
    
    try:
        sig_str_by_position_ground = soup.find_all('div', class_='c-stat-3bar__value')[2].text.strip()
    except IndexError:
        pass
    
    try:
        win_by_method_KO_TKO = soup.find_all('div', class_='c-stat-3bar__value')[3].text.strip()
    except IndexError:
        pass
    
    try:
        win_by_method_DEC = soup.find_all('div', class_='c-stat-3bar__value')[4].text.strip()
    except IndexError:
        pass
    
    try:
        win_by_method_SUB = soup.find_all('div', class_='c-stat-3bar__value')[5].text.strip()
    except IndexError:
        pass
    
    try:
        sig_str_by_target_head = soup.find('text', id='e-stat-body_x5F__x5F_head_value').text.strip()
    except AttributeError:
        pass
    
    try:
        sig_str_by_target_head_percent = soup.find('text', id='e-stat-body_x5F__x5F_head_percent').text.strip()
    except AttributeError:
        pass
    
    try:
        sig_str_by_target_body = soup.find('text', id='e-stat-body_x5F__x5F_body_value').text.strip()
    except AttributeError:
        pass
    
    try:
        sig_str_by_target_body_percent = soup.find('text', id='e-stat-body_x5F__x5F_body_percent').text.strip()
    except AttributeError:
        pass
    
    try:
        sig_str_by_target_leg = soup.find('text', id='e-stat-body_x5F__x5F_leg_value').text.strip()
    except AttributeError:
        pass
    
    try:
        sig_str_by_target_leg_percent = soup.find('text', id='e-stat-body_x5F__x5F_leg_percent').text.strip()
    except AttributeError:
        pass
    
    height = "N/A"
    weight = "N/A"
    age = "N/A"
    status = "N/A"
    
    try:
        status = soup.find_all('div', class_='c-bio__text')[0].text.strip()
    except IndexError:
        pass
    
    if len(soup.find_all('div', class_='c-bio__text')) < 4:
        try:
            age = soup.find_all('div', class_='c-bio__text')[2].text.strip()
        except IndexError:
            pass
    else:
        try:
            age = soup.find_all('div', class_='c-bio__text')[3].text.strip()
        except IndexError:
            pass
        
    if len(soup.find_all('div', class_='c-bio__text')) < 6 and len(soup.find_all('div', class_='c-bio__text')) > 4:
        try:
            weight = soup.find_all('div', class_='c-bio__text')[4].text.strip()    
        except IndexError:
            pass
    if len(soup.find_all('div', class_='c-bio__text')) > 5:
        try:
            height = soup.find_all('div', class_='c-bio__text')[4].text.strip()
        except IndexError:
            pass
        try:
            weight = soup.find_all('div', class_='c-bio__text')[5].text.strip()
        except IndexError:
            pass
    
    # Scrape fight history
    fight_history_section =  []
    
    try:
        fight_history_section = soup.find_all('div', class_ ='c-card-event--athlete-results__info')
    except AttributeError:
        pass
    
    fight_history = []
    if fight_history_section:
        for row in fight_history_section:
            try:
                player1_name = row.find('h3', class_="c-card-event--athlete-results__headline").find_all('a')[0].text.strip()
            except IndexError:
                pass
            try:
                player2_name = row.find('h3', class_="c-card-event--athlete-results__headline").find_all('a')[1].text.strip()
            except IndexError:
                pass
            opponent = ""
            if player1_name == fighter_name:
                opponent = player2_name
            else:
                opponent = player1_name
            
            match_date = "N/A"
            try:
                match_date = row.find('div', class_="c-card-event--athlete-results__date").text.strip()
            except AttributeError:
                pass
            
            columns = []
            try:
                columns = row.find('div', class_="c-card-event--athlete-results__results").find_all('div', class_='c-card-event--athlete-results__result')
            except AttributeError:
                pass
            round = "N/A"
            match_time = "N/A"
            method = "N/A"
            if len(columns) == 1:
                try:
                    method = columns[0].find('div', class_="c-card-event--athlete-results__result-text").text.strip()
                except AttributeError:
                    pass
            if len(columns) == 3:
                try:
                    round = columns[0].find('div', class_="c-card-event--athlete-results__result-text").text.strip()
                except AttributeError:
                    pass
                try:
                    match_time = columns[1].find('div', class_="c-card-event--athlete-results__result-text").text.strip()
                except AttributeError:
                    pass
                try:
                    method = columns[2].find('div', class_="c-card-event--athlete-results__result-text").text.strip()              
                except AttributeError:
                    pass

            fight_history.append([opponent, match_date, round, match_time, method])

    print(fight_history)

    # Return all the scraped data
    return {
        'fighter_name': fighter_name,
        'status' : status,
        'age' : age,
        'height' : height,
        'weight' : weight,
        'division' : division,
        'total_status' : total_status,
        'win_by_knockout' : win_by_knockout,
        'win_by_submission' : win_by_submission,
        'title_defence' : title_defence,
        'striking_accuracy' : striking_accuracy,
        'sig_Strikes_landed' : sig_Strikes_landed,
        'sig_Strikes_attempted' : sig_Strikes_attempted,
        'takeDown_accuracy' : takeDown_accuracy,
        'takeDown_landed' : takeDown_landed,
        'takeDown_attempted' : takeDown_attempted,
        'sig_str_landed_per_min' : sig_str_landed_per_min,
        'sig_str_absorbed_per_min' : sig_str_absorbed_per_min,
        'takeDown_avg_per_15_min' : takeDown_avg_per_15_min,
        'submission_avg_per_15_min' : submission_avg_per_15_min,
        'sig_str_defence' : sig_str_defence,
        'takeDown_defence' : takeDown_defence,
        'knockdown_avg' : knockdown_avg,
        'avg_fight_fime' : avg_fight_fime,
        'sig_str_by_position_standing' : sig_str_by_position_standing,
        'sig_str_by_position_clinch' : sig_str_by_position_clinch,
        'sig_str_by_position_ground' : sig_str_by_position_ground,
        'win_by_method_KO_TKO' : win_by_method_KO_TKO,
        'win_by_method_DEC' : win_by_method_DEC,
        'win_by_method_SUB' : win_by_method_SUB,
        'sig_str_by_target_head' : sig_str_by_target_head,
        'sig_str_by_target_head_percent' : sig_str_by_target_head_percent,
        'sig_str_by_target_body' : sig_str_by_target_body,
        'sig_str_by_target_body_percent' : sig_str_by_target_body_percent,
        'sig_str_by_target_leg' : sig_str_by_target_leg,
        'sig_str_by_target_leg_percent' : sig_str_by_target_leg_percent,
        'fight_history': fight_history
    }

# Function to write data to CSV file
def write_to_csv(fighter_data_list):
    # Open the CSV file and create a writer
    with open('ufc_fighter_data_from_UFC.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow([ 'fighter_name','status' ,'age' ,'height' ,'weight' ,'division' ,'total_status' ,'win_by_knockout' ,'win_by_submission' ,'title_defence' ,
                         'striking_accuracy' ,'sig_Strikes_landed' ,'sig_Strikes_attempted' ,'takeDown_accuracy' ,'takeDown_landed' ,'takeDown_attempted' ,
                         'sig_str_landed_per_min' ,'sig_str_absorbed_per_min' ,'takeDown_avg_per_15_min' ,'submission_avg_per_15_min' ,'sig_str_defence' ,'takeDown_defence' ,
                         'knockdown_avg' ,'avg_fight_fime' ,'sig_str_by_position_standing' ,'sig_str_by_position_clinch' ,'sig_str_by_position_ground' ,'win_by_method_KO_TKO' ,
                         'win_by_method_DEC' ,'win_by_method_SUB' ,'sig_str_by_target_head' ,'sig_str_by_target_head_percent' ,'sig_str_by_target_body' ,
                         'sig_str_by_target_body_percent' ,'sig_str_by_target_leg' ,'sig_str_by_target_leg_percent' ,'fight_history' ])

        # Write data for all fighters
        for fighter_data in fighter_data_list:
            # Write the personal data
            personal_data = [
                fighter_data['fighter_name'], fighter_data['status' ], fighter_data['age' ], fighter_data['height' ], fighter_data['weight' ], fighter_data['division' ], 
                fighter_data['total_status' ], fighter_data['win_by_knockout' ], fighter_data['win_by_submission' ], fighter_data['title_defence' ], 
                fighter_data['striking_accuracy' ], fighter_data['sig_Strikes_landed' ], fighter_data['sig_Strikes_attempted' ], fighter_data['takeDown_accuracy' ], 
                fighter_data['takeDown_landed' ], fighter_data['takeDown_attempted' ], fighter_data['sig_str_landed_per_min' ], fighter_data['sig_str_absorbed_per_min' ], 
                fighter_data['takeDown_avg_per_15_min' ], fighter_data['submission_avg_per_15_min' ], fighter_data['sig_str_defence' ], fighter_data['takeDown_defence' ], 
                fighter_data['knockdown_avg' ], fighter_data['avg_fight_fime' ], fighter_data['sig_str_by_position_standing' ], fighter_data['sig_str_by_position_clinch' ], 
                fighter_data['sig_str_by_position_ground' ], fighter_data['win_by_method_KO_TKO' ], fighter_data['win_by_method_DEC' ], fighter_data['win_by_method_SUB' ], 
                fighter_data['sig_str_by_target_head' ], fighter_data['sig_str_by_target_head_percent' ], fighter_data['sig_str_by_target_body' ], 
                fighter_data['sig_str_by_target_body_percent' ], fighter_data['sig_str_by_target_leg' ], fighter_data['sig_str_by_target_leg_percent' ], 
                fighter_data['fight_history'] 
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
        fighter_data = scrape_ufc_fighter_data(url)
        if fighter_data:
            all_fighter_data.append(fighter_data)
        # Sleep to avoid hitting the server too quickly
        # time.sleep(1)

    # After collecting all data, write to CSV
    
    write_to_csv(all_fighter_data)
    
    print("Data saved to 'ufc_fighter_data_from_UFC.csv'.")

# Scrape all the fighters
scrape_all_fighters(fighter_urls)
