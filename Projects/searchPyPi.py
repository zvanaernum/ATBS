#! python3
# searchpypi.py  - Opens several search results

import sys  # For accessing command-line arguments
import webbrowser  # For opening URLs in a web browser
from selenium import webdriver  # For controlling the web browser
from selenium.webdriver.common.by import By  # For locating elements
from selenium.webdriver.support.ui import WebDriverWait  # For waiting until elements are available
from selenium.webdriver.support import expected_conditions as EC  # For specifying the conditions to wait for

# Initialize the Firefox driver (make sure geckodriver is in your PATH)
driver = webdriver.Firefox()

# Use the command-line arguments to create the search URL
searchURL = 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:])
print('Searching...')  # Display this text while downloading the search results page
driver.get(searchURL)  # Navigate to the search URL

# Wait for the search results to load
try:
    # Wait up to 10 seconds for elements with the class 'package-snippet' to be present
    results_loaded = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.package-snippet'))
    )
    print('Results loaded')
except Exception as e:
    # If there's an error (e.g., timeout), print the error message and exit
    print(f'Error: {e}')
    driver.quit()
    exit()

# Retrieve top search results
linkElems = driver.find_elements(By.CSS_SELECTOR, 'a.package-snippet')  # Find elements with the class 'package-snippet'
print(f'Found {len(linkElems)} links')  # Print the number of links found

# Open a browser tab for each result
numOpen = min(5, len(linkElems))  # Open the first 5 links or the length of the elements list, whichever is fewer
for i in range(numOpen):
    urlToOpen = linkElems[i].get_attribute('href')  # Get the href attribute (URL) of each link element
    print('Opening', urlToOpen)  # Print the URL being opened
    webbrowser.open(urlToOpen)  # Open the URL in a new browser tab

# Close the Selenium driver
driver.quit()  # Quit the browser
