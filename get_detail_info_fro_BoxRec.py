import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Start undetected Chrome
options = uc.ChromeOptions()
options.headless = False  # Set to True to run in the background

# Create a new WebDriver instance with the given options
driver = uc.Chrome(options=options)

# URL of the boxer profile
url = "https://boxrec.com/en/box-pro/659772"

# Open the page
driver.get(url)

# Wait for the profile or key element (like a profile box) to be present
try:
    # Wait until a known element is present on the page, for example, the boxer profile
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "profile-box")))

    # Now that the page has loaded, get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Debugging: print the current URL (to check if there's a redirect or CAPTCHA)
    print(f"Current URL: {driver.current_url}")

    # Scrape the career data or other relevant sections from the page
    career_tag = soup.find("td", colspan="2")

    # Print the career tag content
    if career_tag:
        print(career_tag.text.strip())
    else:
        print("Career tag not found.")

except Exception as e:
    print(f"Error: {e}")

# Close the driver after scraping
driver.quit()
