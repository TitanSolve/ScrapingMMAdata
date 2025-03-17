import requests

# Define the Wikidata ID for Mike Tyson (change to another boxer as needed)
wikidata_id = "Q79031"  # For Mike Tyson. You can change this for other boxers.

# URL to access the JSON data for this entity
url = f"https://www.wikidata.org/wiki/Special:EntityData/{wikidata_id}.json"

# Send a GET request to retrieve the data
response = requests.get(url)

# Parse the JSON data
data = response.json()

# print( data )

# print("---------------------------------------------------------------------");

# Check the structure of the raw data to inspect claims
entity = data["entities"][wikidata_id]

# Print out the raw data to understand its structure
print("Raw Data Structure:\n", entity)

# Extract specific claims (height, weight, total fights, etc.)
claims = entity.get("claims", {})

# Function to extract the value from a claim
def get_claim_value(claims_list):
    if claims_list:
        # Each claim may have multiple values, so we pick the first
        return claims_list[0].get("mainsnak", {}).get("datavalue", {}).get("value", {}).get("quantity", {}).get("value", None)
    return None

# Extract the specific claims for height, weight, and career statistics
height = claims.get("P2048", [])
weight = claims.get("P2067", [])
total_fights = claims.get("P1344", [])
wins = claims.get("P1345", [])
losses = claims.get("P1346", [])
draws = claims.get("P1347", [])

# Extract the values using the function
height_value = get_claim_value(height)
weight_value = get_claim_value(weight)
total_fights_value = get_claim_value(total_fights)
wins_value = get_claim_value(wins)
losses_value = get_claim_value(losses)
draws_value = get_claim_value(draws)

# Print the extracted data
print(f"Height: {height_value} meters")
print(f"Weight: {weight_value} kg")
print(f"Total Fights: {total_fights_value}")
print(f"Wins: {wins_value}")
print(f"Losses: {losses_value}")
print(f"Draws: {draws_value}")



# import requests

# def get_wikidata_id(boxer_name):
#     # Wikipedia API endpoint
#     url = f"https://en.wikipedia.org/w/api.php"

#     # Parameters to search for the Wikidata ID
#     params = {
#         "action": "query",
#         "format": "json",
#         "titles": boxer_name,
#         "prop": "pageprops",
#         "ppprop": "wikibase_item",
#     }

#     response = requests.get(url, params=params)
#     data = response.json()

#     # Extract the Wikidata ID from the response
#     pages = data.get("query", {}).get("pages", {})
#     for page in pages.values():
#         return page.get("pageprops", {}).get("wikibase_item", None)

#     return None

# # Example usage
# boxer_name = "Mike Tyson"  # Change this to any boxer’s name
# wikidata_id = get_wikidata_id(boxer_name)

# if wikidata_id:
#     print(f"Wikidata ID for {boxer_name}: {wikidata_id}")
# else:
#     print("Wikidata ID not found.")