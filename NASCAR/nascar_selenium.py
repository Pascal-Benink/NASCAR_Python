import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

import selenium
print("Selenium version:", selenium.__version__)


def getstandings_curent():
    today = datetime.date.today()

    year = today.year

    download_folder = "NASCAR/downloads"
    download_path = os.path.abspath(download_folder)

    firefox_options = Options()
    firefox_options.set_preference("browser.download.folderList", 2)  # 2 indicates a custom location
    firefox_options.set_preference("browser.download.dir", download_path)

    # Create a new instance of the Firefox driver with the custom options
    driver = webdriver.Firefox(options=firefox_options)

    # Navigate to the website
    base_url = "https://frcs.pro/nascar/cup/drivers/point-standings/"
    current_page = 35  # Starting page

    while current_page >= 0:
        url = f"{base_url}{year}/{current_page}"
        driver.get(url)

        try:
            # Wait for the table to be present
            table = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//table[@id='DataTables_Table_0']"))
            )

            # Check if the "No data available in table" message is not present within the table
            if not table.find_elements(By.XPATH, "//tr/td[contains(text(),'No data available in table')]"):
                # Data found, click the CSV button
                csv_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[@class='btn btn-secondary buttons-csv buttons-html5']"))
                )
                csv_button.click()
                break  # Data found, exit the loop

            print(f"No data available on page {current_page}. Going back one page...")
            current_page -= 1  # Go back one page by decrementing current_page

        except Exception as e:
            print(f"Error: {e}")
    driver.quit()
def getstandings_custom():
    year = input('Please enter the year you want to get the NASCAR Data of')

    download_folder = "NASCAR/downloads"
    download_path = os.path.abspath(download_folder)

    firefox_options = Options()
    firefox_options.set_preference("browser.download.folderList", 2)  # 2 indicates a custom location
    firefox_options.set_preference("browser.download.dir", download_path)

    # Create a new instance of the Firefox driver with the custom options
    driver = webdriver.Firefox(options=firefox_options)

    # Navigate to the website
    base_url = "https://frcs.pro/nascar/cup/drivers/point-standings/"
    current_page = 35  # Starting page

    while current_page >= 0:
        url = f"{base_url}{year}/{current_page}"
        driver.get(url)

        try:
            # Wait for the table to be present
            table = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//table[@id='DataTables_Table_0']"))
            )

            # Check if the "No data available in table" message is not present within the table
            if not table.find_elements(By.XPATH, "//tr/td[contains(text(),'No data available in table')]"):
                # Data found, click the CSV button
                csv_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[@class='btn btn-secondary buttons-csv buttons-html5']"))
                )
                csv_button.click()
                break  # Data found, exit the loop

            print(f"No data available on page {current_page}. Going back one page...")
            current_page -= 1  # Go back one page by decrementing current_page

        except Exception as e:
            print(f"Error: {e}")
    driver.quit()