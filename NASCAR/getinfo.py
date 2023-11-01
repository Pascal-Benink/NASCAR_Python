from sql_client import SQLClient

sql_client = SQLClient()
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'


def get_info():
    current_standings = sql_client.fetch_all("SELECT `Rank`, Driver, `Car #`, Points FROM standings;")
    print(GREEN + "DATA FOUND!" + RESET)
    print("The current NASCAR Cup Standings are: ")
    for data in current_standings:
        print(data)


def custom_select():
    print('This custom query command only uses SELECT and no DELETE/INPUT/UPDATE')
    try:
        thing = input(f"Give me a query to run: ")

        data = sql_client.fetch_all(thing)
        print(GREEN + "DATA FOUND!" + RESET)
        for current_standing in data:
            print(current_standing)

    except Exception as e:

        if "You have an error in your SQL syntax" in str(e):  # Example: Check for a specific MySQL error code
            print(RED + "You have a syntax error please use a valid query" + RESET)

        elif "1146 (42S02)" in str(e):
            print(RED + "this table doesnt exist try using a valid table" + RESET)
        else:
            print(RED + f"An SQL error occurred: {e}" + RESET)


# Call the function


def get_info_from_name(name):
    name = str(name)
    current_standings = sql_client.fetch_all(
        "SELECT `Rank`, Driver, `Car #`, Points FROM standings WHERE Driver = '" + name + "'';")

    current_standings_str = str(current_standings)

    print("The current NASCAR Cup Standings are: ")
    print(GREEN + "DATA FOUND!" + RESET)
    for data in current_standings:
        print(data)


def get_info_best():
    current_standings = sql_client.fetch_all(
        "SELECT `Rank`, Driver, `Car #`, Points FROM standings WHERE `Points` = (SELECT MAX(`Points`) FROM standings);")

    current_standings_str = str(current_standings)
    print(GREEN + "DATA FOUND!" + RESET)
    print("The current NASCAR Cup Standings are: ")
    for data in current_standings:
        print(data)


def get_info_driver_manufacturer():
    manu = str(sql_client.fetch_all("SELECT DISTINCT Make FROM standings"))
    print('The Manufacturers are' + manu)
    name = str(input("Input Manufacturer name here: "))
    current_standings = sql_client.fetch_all(
        "SELECT `Rank`, Driver, `Car #`, Points FROM standings WHERE Make = '" + name + "';")

    current_standings_str = str(current_standings)

    print("The current NASCAR Cup Standings are: ")
    print(GREEN + "DATA FOUND!" + RESET)
    for data in current_standings:
        print(data)


def add_competitor():
    global MAX_POINTS
    MAX_POINTS_data = sql_client.fetch_all(
        "SELECT DISTINCT Points FROM standings WHERE `Points` = (SELECT MAX(`Points`) FROM standings);")
    if MAX_POINTS_data:
        MAX_POINTS = MAX_POINTS_data[0].get('Points', 0)
    else:
        print("No data found")
    # print(str(MAX_POINTS))
    Rank = int(input("Input standings rank here: "))
    STS = int(input("Input Starts here: "))
    Driver = str(input("Input DRIVER name here: "))
    Car = int(input("Input Car number here: "))
    Make = str(input("Input Manufacturer name here: "))
    Points = int(input("Input Points here: "))
    PO_PTS = int(input("Input Playoff Points here: "))
    P = int(input("Input Poles here: "))
    Win = int(input("Input wins here: "))
    T5 = int(input("Input number of Top 5 here: "))
    T10 = int(input("Input number of Top 10 name here: "))
    STG_Win = int(input("Input stage Wins here: "))

    BHND = Points - MAX_POINTS

    confirm = input(f'DO you want to add the competitor standing: \n'
                    f'Rank: {Rank}, STS: {STS}, Driver: {Driver}, Car: {Car}, Make: {Make}, Points: {Points}, BHND: {BHND}, PO_PTS: {PO_PTS}, P: {P}, Win: {Win}, T5: {T5}, T10: {T10}, STG_Win: {STG_Win}\n'
                    f'Y/N: ')

    if confirm == 'Y' or confirm == 'y':
        keys = (
            "`Rank`", "`STS`", "`Driver`", "`Car #`", "`Make`", "`Points`", "`BHND`", "`PO PTS`", "`P`",
            "`Win`", "`T5`", "`T10`",
            "`STG Win`")
        values = (Rank, STS, Driver, Car, Make, Points, BHND, PO_PTS, P, Win, T5, T10, STG_Win)
        table = "standings"

        # Use the insert function to insert the data
        sql_client.insert(keys, values, table)
        print(GREEN + "INSERT Successfull!" + RESET)
    elif confirm == 'N' or confirm == 'n':
        print('Competitor standing add Canceled')
    else:
        print('invalid Input')


def delete_stand():
    searchname = input("What driver's standings do you want to delete?: ")

    # Check if the record exists
    existing_record = sql_client.fetch_all(
        "SELECT * FROM standings WHERE Driver = '" + searchname + "';")

    if not existing_record:
        print("No record found for the specified driver.")
        return  # Exit the function

    current = str(existing_record)

    thechoice = str(input("Are you sure you want to delete \n" + current + " \ny/n:"))

    if thechoice == "y":
        sql_client.query_fix("DELETE FROM standings WHERE Driver = '" + searchname + "';")
        print(GREEN + "DATA DELETED!" + RESET)
    elif thechoice == "n":
        print("Deletion canceled.")
    else:
        print("Invalid input")


def update():
    searchname = input("What driver's standings do you want to Update?: ")

    standing_collumn = input("What standing do you want to Update?: ")

    if standing_collumn == 'Points':
        MAX_POINTS_data = sql_client.fetch_all(
            "SELECT DISTINCT Points FROM standings WHERE `Points` = (SELECT MAX(`Points`) FROM standings);")
        if MAX_POINTS_data:
            MAX_POINTS = MAX_POINTS_data[0].get('Points', 0)
        else:
            print("No data found")

        Points = int(input("What is the new value?: "))

        BHND = Points - MAX_POINTS

        sql_client.query_fix(f"UPDATE standings SET Points = {Points}, BHND = {BHND} WHERE Driver = '{searchname}';")
        print(f'{standing_collumn},BHND of {searchname} is now Updated to {Points} and {BHND}')
    else:
        value = input("What is the new value?: ")
        sql_client.query_fix(f"UPDATE standings SET `{standing_collumn}` = {value} WHERE Driver = '{searchname}';")
        print(GREEN + f'{standing_collumn} of {searchname} is now Updated to {value}' + RESET)


def check_name():
    standings = sql_client.fetch_all('SELECT Driver FROM standings')
    for data in standings:
        driver_name = data.get('Driver', '')  # Get the Driver value from the result
        if driver_name is None or driver_name == '':
            print(f' \033[91m ERR1 NULL/EMPTY PROBLEM: {driver_name} \033[0m')
            sql_client.query_fix("DELETE FROM standings WHERE Driver IS NULL OR Driver = ''")
            print('\033[92m Problem solved \033[0m')
        else:
            print(f" \033[92m No changes: {driver_name} \033[0m")


def insert_tester():
    amount = 0
    while amount <= 10:
        amount += 1
        sql_client.query_fix("INSERT INTO standings (Driver) VALUES (NULl)")
        print(f"fake null {amount} made!")
        print(GREEN + "ADDING COMPLETE!" + RESET)
