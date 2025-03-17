import requests

def get_subcategories(category_name="Category:UFC_fighters"):
    url = "https://en.wikipedia.org/w/api.php"
    
    params = {
        'action': 'query',
        'list': 'categorymembers',
        'cmtitle': category_name,
        'cmtype': 'subcat',  # Get subcategories
        'format': 'json',
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        subcategories = data['query']['categorymembers']
        
        print(f"Subcategories of {category_name}:")
        for subcategory in subcategories:
            print(f"- {subcategory['title']}")
    else:
        print("Error fetching data from Wikipedia API")

# Example: Get subcategories of "UFC Fighters"
get_subcategories("Category:Ultimate Fighting Championship")