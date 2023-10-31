from sql_client import SQLClient
sql_client = SQLClient()

def get_info():
    current_standings = sql_client.fetch_all("SELECT `Rank`, Driver, `Car #`, Points FROM standings;")

    current_standings_str = str(current_standings)

    print("The current NASCAR Cup Standings are: ")
    for data in current_standings:
        print(data)

def get_info_from_name(name):
    name = str(name)
    current_standings = sql_client.fetch_all("SELECT `Rank`, Driver, `Car #`, Points FROM standings WHERE Driver = '" + name + "'';")

    current_standings_str = str(current_standings)

    print("The current NASCAR Cup Standings are: ")
    for data in current_standings:
        print(data)

def get_info_best():
    current_standings = sql_client.fetch_all("SELECT `Rank`, Driver, `Car #`, Points FROM standings WHERE `Points` = (SELECT MAX(`Points`) FROM standings);")

    current_standings_str = str(current_standings)

    print("The current NASCAR Cup Standings are: ")
    for data in current_standings:
        print(data)

def get_info_driver_manufacturer():
    manu = str(sql_client.fetch_all("SELECT DISTINCT Make FROM standings"))
    print('The Manufacturers are' + manu)
    name = str(input("Input Manufacturer name here: "))
    current_standings = sql_client.fetch_all("SELECT `Rank`, Driver, `Car #`, Points FROM standings WHERE Make = '" + name + "';")

    current_standings_str = str(current_standings)

    print("The current NASCAR Cup Standings are: ")
    for data in current_standings:
        print(data)

def add_competitor():
    MAX_POINTS_data = sql_client.fetch_all("SELECT DISTINCT Points FROM standings WHERE `Points` = (SELECT MAX(`Points`) FROM standings);")
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
        # query = (
        #     f"INSERT INTO standings "
        #     f"(`Rank`, `Rank +/-`, `STS`, `Driver`, `Car #`, `Make`, `Points`, `BHND`, `PO PTS`, `P`, `Win`, `T5`, `T10`, `STG Win`) "
        #     f"VALUES "
        #     f"({Rank}, NULL, {STS}, '{Driver}', {Car}, '{Make}', {Points}, {BHND}, {PO_PTS}, {P}, {Win}, {T5}, {T10}, {STG_Win})"
        # )
        #
        # sql_client.fetch_all(query)
        # Define the keys and values you want to insert
        keys = (
        "`Rank`", "`Rank +/-`", "`STS`", "`Driver`", "`Car #`", "`Make`", "`Points`", "`BHND`", "`PO PTS`", "`P`", "`Win`", "`T5`", "`T10`",
        "`STG Win`")
        values = (Rank, None, STS, Driver, Car, Make, Points, BHND, PO_PTS, P, Win, T5, T10, STG_Win)
        table = "standings"

        # Use the insert function to insert the data
        sql_client.insert(keys, values, table)
        print('Insert Successful')
    elif confirm == 'N' or confirm == 'n':
        print('Competitor standing add Canceled')
    else:
        print('invalid Input')

def delete_stand():

    searchname = str(input("What driver his standings do you want to delete?: "))

    current = str(sql_client.fetch_all(
        "SELECT * FROM standings WHERE Driver = '" + searchname + "';"))


    thechoice = str(input("Are you sure you want to delete \n" + current + " \ny/n:"))
    if thechoice == "y":
        current_standings = str(sql_client.fetch_all(
            "DELETE FROM standings WHERE Driver = '" + searchname + "';"))
    elif thechoice == "n":
        print("Deleting cancelled")
    else:
        print("invalid input")





