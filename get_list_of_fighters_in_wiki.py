import requests
import csv

# Set up the URL parameters
api_key = '850a88aeb3c29599ce2db46832aa229f'
base_url = "https://liveapi.yext.com/v2/accounts/me/answers/vertical/query"
params = {
    'experienceKey': 'answers-en',
    'api_key': api_key,
    'v': '20220511',
    'version': 'PRODUCTION',
    'locale': 'en',
    'input': 'api athletes',
    'verticalKey': 'athletes',
    'limit': 21,  # Number of results per page
    'offset': 0,  # Starting point for the results
    'retrieveFacets': 'true',
    'facetFilters': '{}',
    'sessionTrackingEnabled': 'true',
    'sortBys': '[]',
    'source': 'STANDARD',
    'jsLibVersion': 'v1.14.3'
}

# Initialize a list to store all the fighters' data
all_fighters = []

# Function to get fighters' data from the API
def get_fighters(offset):
    params['offset'] = offset
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        # If 'response' contains the 'results', process them
        if 'response' in data and 'results' in data['response']:
            return data['response']['results']
        else:
            return []
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []

# Function to save the data to a CSV file
def save_to_csv(fighters):
    with open('ufc_fighters.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'NickName', 'Age', 'Birthday', 'Gender', 'Height', 'Weight', 'Weight_class', 'Url', 'RecordDraws', 'RecordLosses', 'RecordNoContests', 
                         'RecordWins', 'WeightClassAbbreviation', 'WeightClassId', 'Stance', ])
        
# 'type': 'ce_athletes', 'landingPageUrl': 'http://www.ufc.com/athlete/wuziazibieke-jiahefu', 'name': 'Wuziazibieke Jiahefu', 'c_activeInAnswers': True, 
# 'c_age': '34', 'c_dOB': '1990-04-09', 'c_fightingOutOfCountry': 'China', 'c_fightingOutOfState': 'Hebei', 'c_fightingOutOfTriCode': 'CHN', 
# 'c_height': '69.0', 'c_homeCountry': 'China', 'c_homeState': ['Xinjiang'], 'c_homeTriCode': 'CHN', 'c_nickname': 'Prairie Kitty',
# 'c_reach': '70.5', 'c_recordDraws': '1', 'c_recordLosses': '12', 'c_recordNoContests': '0', 'c_recordWins': '29', 'c_stance': 'Orthodox', 
# 'c_uFCLink': 'http://www.ufc.com/athlete/Wuziazibieke-Jiahefu', 'c_weight': '145.0', 'c_weightClass': 'Featherweight', 'c_weightClassAbbreviation': 'FTW', 
# 'c_weightClassId': '6', 'c_weightClassOrder': '1', 'firstName': 'Wuziazibieke', 'gender': 'Male', 'lastName': 'Jiahefu', 'uid': '1000059553'}, 'highlightedFields': {}}
        
        for fighter in fighters:
            name = fighter['data'].get('name', 'N/A')
            nickName = fighter['data'].get('c_nickname', 'N/A')
            age = fighter['data'].get('c_age', 'N/A')
            birthday = fighter['data'].get('c_dOB', 'N/A')
            gender = fighter['data'].get('gender', 'N/A')
            height = fighter['data'].get('c_height', 'N/A')
            weight = fighter['data'].get('c_weight', 'N/A')
            weight_class = fighter['data'].get('c_weightClass', 'N/A')
            url = fighter['data'].get('landingPageUrl', 'N/A')      
            recordDraws = fighter['data'].get('c_recordDraws', 'N/A')
            recordLosses = fighter['data'].get('c_recordLosses', 'N/A')
            recordNoContests = fighter['data'].get('c_recordNoContests', 'N/A')
            recordWins = fighter['data'].get('c_recordWins', 'N/A')
            weightClassAbbreviation = fighter['data'].get('c_weightClassAbbreviation', 'N/A')
            weightClassId = fighter['data'].get('c_weightClassId', 'N/A')
            stance = fighter['data'].get('c_stance', 'N/A')
            
            print(name)
            
            writer.writerow([name, nickName, age, birthday, gender, height, weight, weight_class, url, recordDraws, recordLosses, recordNoContests, recordWins, 
                             weightClassAbbreviation, weightClassId, stance, ])

# Loop through the pages and collect data
offset = 0
while True:
    print(f"Fetching data for offset: {offset}")
    fighters = get_fighters(offset)
    
    if not fighters:  # No more fighters to fetch
        break
    
    all_fighters.extend(fighters)
    offset += 21  # Increase offset by the limit (21)

# Once all data is fetched, save it to a CSV
save_to_csv(all_fighters)

print(f"Finished fetching {len(all_fighters)} fighters and saved to 'ufc_fighters.csv'")