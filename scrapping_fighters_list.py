from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Correct path to ChromeDriver executable (update to your actual path)
driver_path = r'C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver.exe'

# Set up Chrome options (optional: headless mode)
chrome_options = Options()
chrome_options.add_argument('--headless')  # Optional: Run headless if you don't need a GUI

# Set up the ChromeDriver service
service = Service(driver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of Sherdog Fighter List (Starting with letter 'A')
url = 'https://www.sherdog.com/fighters?letter=A'

# Go to the webpage
driver.get(url)

# Wait for the page to load completely
time.sleep(2)

# Create a list to store all fighter links
fighter_links = []

# Function to scrape all fighter links on the current page
def scrape_fighter_links():
    # Find all the fighter links on the page (you may need to update the selector)
    fighters = driver.find_elements(By.XPATH, "//a[contains(@href, '/fighter/')]")
    for fighter in fighters:
        fighter_links.append(fighter.get_attribute('href'))

# Scrape the first page (A)
scrape_fighter_links()

# Check if there is a 'Next' button to go to the next page
while True:
    try:
        # Click the "Next" button
        next_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Next')]")
        next_button.click()
        time.sleep(2)  # Wait for the next page to load
        
        # Scrape fighter links from the new page
        scrape_fighter_links()
        
    except Exception as e:
        print(f"Reached the last page or an error occurred: {e}")
        break  # Exit the loop when no more pages are found

# Close the browser
driver.quit()

# Output the list of fighter links
print(f"Found {len(fighter_links)} fighter links.")
for link in fighter_links:
    print(link)