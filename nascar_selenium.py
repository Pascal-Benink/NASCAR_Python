import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from fillinfo import *


def getstandings_curent():
    today = datetime.date.today()

    year = str(today.year)
    print('Preparing download:')

    download_folder = "NASCAR/downloads"
    download_path = os.path.abspath(download_folder)

    file_path = f"NASCAR/downloads/{year} NASCAR Cup Series Driver Points Standings.csv"

    # Check if the file exists
    if os.path.exists(file_path):
        # If the file exists, delete it
        os.remove(file_path)

    file_path2 = f"NASCAR/downloads/{year} NASCAR Cup Series Driver Points Standings_modified.csv"

    # Check if the file exists
    if os.path.exists(file_path2):
        # If the file exists, delete it
        os.remove(file_path2)

    firefox_options = Options()
    firefox_options.set_preference("browser.download.folderList", 2)  # 2 indicates a custom location
    firefox_options.set_preference("browser.download.dir", download_path)

    # Create a new instance of the Firefox driver with the custom options
    driver = webdriver.Firefox(options=firefox_options)

    # Navigate to the website
    base_url = "https://frcs.pro/nascar/cup/drivers/point-standings/"
    current_page = 36  # Starting page

    while current_page >= 1:
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
                print('downloading')

                break  # Data found, exit the loop

            if current_page == 1:
                print('Data not found update aborted')
                driver.quit()
                return
            print(f"No data available on page {current_page}. Going back one page...")
            current_page -= 1  # Go back one page by decrementing current_page

        except Exception as e:
            print(f"Error: {e}")
    driver.quit()

    files = os.listdir(download_path)

    # Search for a file that contains the year
    matching_files = [file for file in files if year in file]

    if matching_files:
        for matching_file in matching_files:
            correct = download_path + "/" + f"{year} NASCAR Cup Series Driver Points Standings.csv"
            matching_file_with_path = download_path + "/" + matching_file
            # print(matching_file_with_path)
            os.rename(matching_file_with_path, correct)

    # Define the file paths
    input_csv_file = f"NASCAR/downloads/{year} NASCAR Cup Series Driver Points Standings.csv"
    output_csv_file = f"NASCAR/downloads/{year} NASCAR Cup Series Driver Points Standings_modified.csv"

    # Process the CSV file
    with open(input_csv_file, 'r') as input_file, open(output_csv_file, 'w', newline='') as output_file:
        csv_reader = csv.reader(input_file)
        csv_writer = csv.writer(output_file)

        for row in csv_reader:
            # Check if there are at least two cells in the row (e.g., to skip the header row)
            if len(row) >= 2:
                # Remove the second cell (from "Rank +/-") by slicing the list
                modified_row = row[:1] + row[2:]

                # Remove commas from numeric columns (e.g., 'Points' and 'BHND')
                modified_row[5] = modified_row[5].replace(',', '')
                modified_row[6] = modified_row[6].replace(',', '')

                for i in range(len(modified_row)):
                    if modified_row[i] == "--":
                        modified_row[i] = None

                csv_writer.writerow(modified_row)
            else:
                # Handle rows with less than two cells (e.g., header row)
                csv_writer.writerow(row)

    print("Processing complete. Modified data saved to", output_csv_file)

    csv_file = f'NASCAR/downloads/{year} NASCAR Cup Series Driver Points Standings_modified.csv'
    print(f'Now Updating the database with the latest Nascar Cup standings of {year}')
    if sql_client.check_table_exists('standings'):
        sql_client.query_fix("DELETE FROM standings;")
    print("Old records deleted successfully.")
    table_name = "standings"

    if sql_client.check_table_exists(table_name):
        with open(csv_file, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # Assuming the CSV columns match the table columns
                keys = row.keys()
                values = tuple(row.values())
                values = tuple(None if value == '' else value for value in values)
                sql_client.insert(keys, values, table_name)
    else:
        q = 'CREATE TABLE `standings` (`Rank` INT DEFAULT NULL, `STS` INT DEFAULT NULL, `Driver` VARCHAR(255) DEFAULT NULL, `Car #` INT DEFAULT NULL, `Make` VARCHAR(255) DEFAULT NULL, `Points` INT DEFAULT NULL, `BHND` INT DEFAULT NULL, `PO PTS` INT DEFAULT NULL, `P` INT DEFAULT NULL, `Win` INT DEFAULT NULL, `T5` INT DEFAULT NULL, `T10` INT DEFAULT NULL, `STG Win` INT DEFAULT NULL)'
        sql_client.query_fix(q)

        with open(csv_file, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # Assuming the CSV columns match the table columns
                keys = row.keys()
                values = tuple(row.values())
                values = tuple(None if value == '' else value for value in values)
                sql_client.insert(keys, values, table_name)

    print("Data Has been updated.")


def getstandings_custom():
    year = input('Please enter the year you want to get the NASCAR Data of: ')

    print('Preparing download:')

    download_folder = "NASCAR/downloads"
    download_path = os.path.abspath(download_folder)

    file_path = f"NASCAR/downloads/{year} NASCAR Cup Series Driver Points Standings.csv"

    # Check if the file exists
    if os.path.exists(file_path):
        # If the file exists, delete it
        os.remove(file_path)

    file_path2 = f"NASCAR/downloads/{year} NASCAR Cup Series Driver Points Standings_modified.csv"

    # Check if the file exists
    if os.path.exists(file_path2):
        # If the file exists, delete it
        os.remove(file_path2)

    firefox_options = Options()
    firefox_options.set_preference("browser.download.folderList", 2)  # 2 indicates a custom location
    firefox_options.set_preference("browser.download.dir", download_path)

    # Create a new instance of the Firefox driver with the custom options
    driver = webdriver.Firefox(options=firefox_options)

    # Navigate to the website
    base_url = "https://frcs.pro/nascar/cup/drivers/point-standings/"
    current_page = 36  # Starting page

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

            if current_page == 1:
                print('Data not found update aborted')
                driver.quit()
                return
            print(f"No data available on page {current_page}. Going back one page...")
            current_page -= 1  # Go back one page by decrementing current_page

        except Exception as e:
            print(f"Error: {e}")
    driver.quit()

    files = os.listdir(download_path)

    # Search for a file that contains the year
    matching_files = [file for file in files if year in file]

    if matching_files:
        for matching_file in matching_files:
            correct = download_path + "/" + f"{year} NASCAR Cup Series Driver Points Standings.csv"
            matching_file_with_path = download_path + "/" + matching_file
            # print(matching_file_with_path)
            os.rename(matching_file_with_path, correct)

    input_csv_file = f"NASCAR/downloads/{year} NASCAR Cup Series Driver Points Standings.csv"
    output_csv_file = f"NASCAR/downloads/{year} NASCAR Cup Series Driver Points Standings_modified.csv"

    # Process the CSV file
    with open(input_csv_file, 'r') as input_file, open(output_csv_file, 'w', newline='') as output_file:
        csv_reader = csv.reader(input_file)
        csv_writer = csv.writer(output_file)

        for row in csv_reader:
            # Check if there are at least two cells in the row (e.g., to skip the header row)
            if len(row) >= 2:
                # Remove the second cell (from "Rank +/-") by slicing the list
                modified_row = row[:1] + row[2:]

                # Remove commas from numeric columns (e.g., 'Points' and 'BHND')
                modified_row[5] = modified_row[5].replace(',', '')
                modified_row[6] = modified_row[6].replace(',', '')

                for i in range(len(modified_row)):
                    if modified_row[i] == "--":
                        modified_row[i] = None

                csv_writer.writerow(modified_row)
            else:
                # Handle rows with less than two cells (e.g., header row)
                csv_writer.writerow(row)

    print("Processing complete. Modified data saved to", output_csv_file)

    csv_file = f'NASCAR/downloads/{year} NASCAR Cup Series Driver Points Standings_modified.csv'
    print(f'Now Updating the database with the latest Nascar Cup standings of {year}')
    sql_client.query_fix("DELETE FROM standings;")
    print("Old records deleted successfully.")
    table_name = "standings"

    if sql_client.check_table_exists(table_name):
        with open(csv_file, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # Assuming the CSV columns match the table columns
                keys = row.keys()
                values = tuple(row.values())
                values = tuple(None if value == '' else value for value in values)
                sql_client.insert(keys, values, table_name)
    else:
        q = 'CREATE TABLE `standings` (`Rank` INT DEFAULT NULL, `STS` INT DEFAULT NULL, `Driver` VARCHAR(255) DEFAULT NULL, `Car #` INT DEFAULT NULL, `Make` VARCHAR(255) DEFAULT NULL, `Points` INT DEFAULT NULL, `BHND` INT DEFAULT NULL, `PO PTS` INT DEFAULT NULL, `P` INT DEFAULT NULL, `Win` INT DEFAULT NULL, `T5` INT DEFAULT NULL, `T10` INT DEFAULT NULL, `STG Win` INT DEFAULT NULL)'
        sql_client.query_fix(q)

        with open(csv_file, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # Assuming the CSV columns match the table columns
                keys = row.keys()
                values = tuple(row.values())
                values = tuple(None if value == '' else value for value in values)
                sql_client.insert(keys, values, table_name)

    print("Data Has been updated.")
