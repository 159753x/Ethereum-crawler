import requests
import os
from dotenv import load_dotenv
from prettytable import PrettyTable
from datetime import datetime

load_dotenv(".env")
api_key = os.getenv("etherscan_api_key")

def get_transactions(address: str = '0x4675C7e5BaAFBFFbca748158bEcBA61ef3b0a263', 
                     start_block: int = 0, 
                     end_block: int = 99999999):
    """
    Fetch all normal transactions for a given address from start_block to end_block.
    """
    url = "https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": start_block,
        "endblock": end_block,
        "page": 1,
        "offset": 100,   # maximum number of transactions per page
        "sort": "desc",
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] == "1":
        return data["result"]
    else:
        # If status is not 1, usually means no transactions or an error
        return []
    

def display_transactions(transactions):
    """
    Displays transactions in a tabular format in the console.
    """
    table = PrettyTable()
    table.field_names = ["Block", "Timestamp (UTC)", "From", "To", "Value (ETH)", "Tx Hash"]
    
    for tx in transactions:
        block_number = tx["blockNumber"]
        time_utc = datetime.fromtimestamp(int(tx["timeStamp"])).strftime('%Y-%m-%d %H:%M:%S')
        from_addr = tx["from"]
        to_addr = tx["to"]
        value_eth = int(tx["value"]) / 1e18
        tx_hash = tx["hash"]

        table.add_row([block_number, time_utc, from_addr, to_addr, f"{value_eth:.6f}", tx_hash])
    
    print(table)


user_input_addr = input("Enter address of account: ")
user_input_block = input("Enter Block number from which should fetching begin: ")
data = get_transactions(address=user_input_addr, start_block=user_input_block)

if not data:
    print("There is not any transactions with that address or address is wrong ")
else:
    display_transactions(data)