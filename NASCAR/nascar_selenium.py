from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

download_folder = "NASCAR/downloads"
download_path = os.path.abspath(download_folder)

firefox_options = Options()
firefox_options.set_preference("browser.download.folderList", 2)  # 2 indicates a custom location
firefox_options.set_preference("browser.download.dir", download_path)

# Create a new instance of the Firefox driver with the custom options
driver = webdriver.Firefox(options=firefox_options)

# Navigate to the website
url = "https://frcs.pro/nascar/cup/drivers/point-standings/2023/35"
driver.get(url)
try:
    # Wait for the CSV button to be clickable
    csv_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-secondary buttons-csv buttons-html5']")))
    csv_button.click()

    driver.quit()

except Exception as e:
    print("An error occurred: ", e)
    driver.quit()