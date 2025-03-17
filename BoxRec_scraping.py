from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--incognito")

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL of the BoxRec page for a specific boxer
url = 'https://www.boxrec.com/en/proboxer/123456'  # Replace with the actual URL

# Open the webpage
driver.get(url)

try:
    # Wait for the boxer's name to be visible on the page
    boxer_name_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1"))  # Modify this XPath if necessary
    )
    boxer_name = boxer_name_element.text.strip()
    print(f"Boxer: {boxer_name}")

    # You can extract more elements similarly (e.g., record, title, etc.)
    # Example: Extract boxer's record
    record_element = driver.find_element(By.XPATH, "//div[@class='boxer-record']")
    record = record_element.text.strip()
    print(f"Record: {record}")
except Exception as e:
    print(f"Error extracting data: {e}")

# Close the browser after extraction
driver.quit()
