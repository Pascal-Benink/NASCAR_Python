from sql_client import SQLClient

sql_client = SQLClient()
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'


def green_print(text):
    print(GREEN + str(text) + RESET)


def error_text(text):
    print(RED + str(text) + RESET)


def get_info():
    current_standings = sql_client.fetch_all("SELECT `Rank`, Driver, `Car #`, Points FROM standings;")
    green_print('DATA FOUND!')
    print("The current NASCAR Cup Standings are: ")
    for data in current_standings:
        print(data)


def custom_select():
    print('This custom query command only uses SELECT and no DELETE/INPUT/UPDATE')
    try:
        query = input(f"Give me a query to run: ")

        data = sql_client.fetch_all(query)
        green_print('DATA FOUND!')
        for current_standing in data:
            print(current_standing)

    except Exception as e:

        if "You have an error in your SQL syntax" in str(e):
            error_text('Syntax error check your code')
        elif "1146 (42S02)" in str(e):
            error_text('Table not found insert a valid table')
        else:
            error_text('An sql error has occurred: ' + str(e))


def get_info_from_name(name):
    name = str(name)
    current_standings = sql_client.fetch_all(
        "SELECT `Rank`, Driver, `Car #`, Points FROM standings WHERE Driver = '" + name + "'';")

    current_standings_str = str(current_standings)

    print("The current NASCAR Cup Standings are: ")
    green_print('DATA FOUND!')
    for data in current_standings:
        print(data)


def get_info_best():
    current_standings = sql_client.fetch_all(
        "SELECT `Rank`, Driver, `Car #`, Points FROM standings WHERE `Points` = (SELECT MAX(`Points`) FROM standings);")

    current_standings_str = str(current_standings)
    green_print('DATA FOUND!')
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
    green_print('DATA FOUND!')
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
    rank = int(input("Input standings rank here: "))
    sts = int(input("Input Starts here: "))
    driver = str(input("Input DRIVER name here: "))
    car = int(input("Input Car number here: "))
    make = str(input("Input Manufacturer name here: "))
    points = int(input("Input Points here: "))
    po_pts = int(input("Input Playoff Points here: "))
    p = int(input("Input Poles here: "))
    win = int(input("Input wins here: "))
    t5 = int(input("Input number of Top 5 here: "))
    t10 = int(input("Input number of Top 10 name here: "))
    stg_win = int(input("Input stage Wins here: "))

    bhnd = points - MAX_POINTS

    confirm = input(f'DO you want to add the competitor standing: \n'
                    f'Rank: {rank}, STS: {sts}, Driver: {driver}, Car: {car}, Make: {make}, Points: {points}, BHND: {bhnd}, PO_PTS: {po_pts}, P: {p}, Win: {win}, T5: {t5}, T10: {t10}, STG_Win: {stg_win}\n'
                    f'Y/N: ')

    if confirm == 'Y' or confirm == 'y':
        keys = (
            "`Rank`", "`STS`", "`Driver`", "`Car #`", "`Make`", "`Points`", "`BHND`", "`PO PTS`", "`P`",
            "`Win`", "`T5`", "`T10`",
            "`STG Win`")
        values = (rank, sts, driver, car, make, points, bhnd, po_pts, p, win, t5, t10, stg_win)
        table = "standings"

        # Use the insert function to insert the data
        sql_client.insert(keys, values, table)
        green_print('insert success')
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
        green_print('DATA DELETED!')
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
            error_text(f'ERR1 NULL problem found!: {driver_name}')
            sql_client.query_fix("DELETE FROM standings WHERE Driver IS NULL OR Driver = ''")
            green_print('problem solved')
        else:
            print(f" \033[92m No changes: {driver_name} \033[0m")


def insert_tester():
    amount = 0
    while amount <= 10:
        amount += 1
        sql_client.query_fix("INSERT INTO standings (Driver) VALUES (NULl)")
        print(f"fake null {amount} made!")
        green_print('DATA ADDED!')
