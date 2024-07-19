import os
import json
import datetime
from collections import Counter
# Corrected directory path
directory = r"C:\Users\gurja\OneDrive\Desktop\json files"

# List of JSON file names
file_names = [
    '1stdata.json',
    '2nddata.json',
    '3rddata.json',
    '4thdata.json',
    '5thdata.json',
    '6thdata.json',
    '7thdata.json',
    '8thdata.json'
]

# Loop through each file
for file_name in file_names:
    file_path = os.path.join(directory, file_name)

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        print(f"Data from {file_name}:")
        print(data)
        print()

    except FileNotFoundError:
        print(f"File {file_name} not found.")

    except json.JSONDecodeError:
        print(f"Error decoding JSON in file {file_name}.")


    def get_day_of_week(date_str):
        date_obj = datetime.datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %z')
        return date_obj.strftime('%A')