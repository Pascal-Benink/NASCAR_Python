from sql_client import SQLClient

sql_client = SQLClient()

def deleterallinfo():
    thechoice = str(input("Are you sure you want to delete all info? Y/N:"))

    if thechoice == "y" or thechoice == "Y":
        sql_client.query_fix("DELETE FROM standings;")
        print("Records deleted successfully.")
    elif thechoice == "n" or thechoice == "N":
        print("Deletion canceled.")
    else:
        print("Invalid input")

def insertallstandings(csv):
    print("Invalid input")