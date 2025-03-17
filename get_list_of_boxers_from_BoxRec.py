# import time
# import undetected_chromedriver as uc
# from bs4 import BeautifulSoup

# # Start undetected Chrome
# options = uc.ChromeOptions()
# options.headless = False  # Set to True to run in the background
# driver = uc.Chrome(options=options)

# # Open the BoxRec ratings page
# driver.get("https://boxrec.com/en/ratings")

# # Wait for JavaScript to load (adjust time if needed)
# time.sleep(5)

# # Parse the page with BeautifulSoup
# soup = BeautifulSoup(driver.page_source, "html.parser")

# # Close the browser
# driver.quit()

# # Extract boxer's hyperlinks
# boxer_links = []
# for link in soup.select('a.personLink'):
#     href = link.get("href")
#     if href:
#         boxer_links.append(f'https://boxrec.com/{href}')

# # Print results
# for link in boxer_links:
#     print(link)

import time
import undetected_chromedriver as uc
from bs4 import BeautifulSoup

# Start undetected Chrome
options = uc.ChromeOptions()
options.headless = False  # Set to True to run in the background

driver = uc.Chrome(options=options)

# Store all boxer links
boxer_links = []

try:
    for offset in range(50, 549 * 50, 50):  # Loop through pages
        url = f"https://boxrec.com/en/ratings?offset={offset}"
        print(f"Scraping: {url}")

        driver.get(url)
        time.sleep(10)  # Wait for JavaScript to load

        # Parse the page
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Extract boxer's hyperlinks
        for link in soup.select('a.personLink'):
            href = link.get("href")
            if href:
                full_url = f'https://boxrec.com{href}'
                print(full_url)
                boxer_links.append(full_url)       
        
        f = open("boxrec_boxers.txt", "w", encoding="utf-8")
        for link in boxer_links:
            f.write(link + "\n")
        f.close()
        

finally:
    driver.quit()  # Ensure the browser quits properly

# Print all links
for link in boxer_links:
    print(link)

# Save to file
# with open("boxrec_boxers.txt", "w", encoding="utf-8") as f:
#     for link in boxer_links:
#         f.write(link + "\n")

print(f"✅ Scraped {len(boxer_links)} boxers and saved to boxrec_boxers.txt")
