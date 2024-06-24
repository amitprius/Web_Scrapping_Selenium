from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import csv

from bs4 import BeautifulSoup

# Set up the WebDriver
# Creating a webdriver instance
driver = webdriver.Chrome()

# Open LinkedIn and log in
driver.get("https://linkedin.com/uas/login")

# Allow time for the page to load
time.sleep(3)

# Log in to LinkedIn
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys("xxxxxxxxxx@gmail.com")
password.send_keys("xxxxxxxxxx")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Maximize the browser window
driver.maximize_window()

# Allow time for the page to load
time.sleep(60)

# Perform a search
search_bar = driver.find_element(By.XPATH, "//input[@aria-label='Search']")
time.sleep(5)
search_query = "Python Developer"
search_bar.send_keys(search_query)
time.sleep(5)
search_bar.send_keys(Keys.RETURN)

# Allow time for search results to load
time.sleep(15)

# Click on the "People" tab
people_tab = driver.find_element(By.XPATH, "//*[@id='search-reusables__filters-bar']/ul/li[1]/button")
time.sleep(5)
people_tab.send_keys(Keys.RETURN)

# Allow time for the "People" tab results to load
time.sleep(5)

#//*[@data-test-pagination-page-btn="1"]/button
# Function to scrape user information from a profile
def scrape_profile():


    # Extract profile IDs from the href attributes of <a> elements
    profile_links = driver.find_elements(By.XPATH, "//a[contains(@href, 'linkedin.com/in')]")

    profile_ids = set()

    for link in profile_links:
        href = link.get_attribute("href")
        # Extract profile ID
        profile_id = href.split("/in/")[-1].split("?")[0]

        # Filter out profile IDs starting with "ACo"
        if not profile_id.startswith("ACo"):
            profile_ids.add(profile_id)
        

    # Convert set to list for further use if needed
    profile_ids_list = list(profile_ids)

    print(profile_ids_list)


    start = time.time()
 
    # will be used in the while loop
    initialScroll = 0
    finalScroll = 1000
    
    while True:
        driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
        # this command scrolls the window starting from
        # the pixel value stored in the initialScroll
        # variable to the pixel value stored at the
        # finalScroll variable
        initialScroll = finalScroll
        finalScroll += 1000
    
        # we will stop the script for 3 seconds so that
        # the data can load
        time.sleep(5)
        # You can change it as per your needs and internet speed
    
        end = time.time()
    
        # We will scroll for 20 seconds.
        # You can change it as per your needs and internet speed
        if round(end - start) > 20:
            break

    next_page = driver.find_element(By.XPATH, "//button[span[text()='Next']]")
    time.sleep(5)
    next_page.send_keys(Keys.RETURN)

    time.sleep(10)
    
scrape_users = scrape_profile()


#print("Scraping complete. Data saved to linkedin_profiles.csv.")

# Keep the browser open
input("Press Enter to close the browser and end the script...")

# Optionally close the browser
# driver.quit()
