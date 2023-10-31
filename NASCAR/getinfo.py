from sql_client import SQLClient
sql_client = SQLClient()

current_standings = sql_client.fetch_all("SELECT `Rank`, Driver, `Car #` FROM standings;")

current_standings_str = str(current_standings)

print("The current NASCAR Standings are" + current_standings_str)