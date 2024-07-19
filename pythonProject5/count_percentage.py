import json
from collections import Counter

# Function to load data from JSON files
def load_data(file_paths):
    all_data = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            data = json.load(file)
            all_data.extend(data)
    return all_data

# Function to count emails by day of the week
def count_days_of_week(data):
    day_counts = Counter(item['day_of_week'] for item in data)
    return day_counts

# Function to calculate percentages
def calculate_percentages(day_counts):
    total_emails = sum(day_counts.values())
    percentages = {day: (count / total_emails) * 100 for day, count in day_counts.items()}
    return percentages

# File paths to JSON files
file_paths = [
    '1stdata.json',
    '2nddata.json',
    '3rddata.json',
    '4thdata.json',
    '5thdata.json',
    '6thdata.json',
    '7thdata.json',
    '8thdata.json'
]

# Load and process data
data = load_data(file_paths)
day_counts = count_days_of_week(data)
percentages = calculate_percentages(day_counts)

# Print results
print("Day counts:", day_counts)
print("Percentages:", percentages)
