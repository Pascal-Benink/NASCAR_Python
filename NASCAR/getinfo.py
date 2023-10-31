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