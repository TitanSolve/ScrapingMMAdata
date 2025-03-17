from bs4 import BeautifulSoup

# Load the HTML file
file_path = "Boxer Records & Profiles _ Box.live.html"  # Adjust path if needed
with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Extract boxer names from relevant classes
boxer_names = set()  # Use a set to remove duplicates
fighter_divs = soup.find_all(class_=["d-flex flex-wrap w-100"])

for div in fighter_divs:
    links = div.find_all("a")  # Assuming names are within <a> tags
    for link in links:
        text = link.get_text(strip=True)
        if text:
            boxer_names.add(text)  # Add to set to ensure uniqueness

# Convert set to list and print names
boxer_names = sorted(boxer_names)  # Optional: Sort alphabetically

for name in boxer_names:
    print(name)