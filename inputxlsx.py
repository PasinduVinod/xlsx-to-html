import pandas as pd
import json

# Read the Excel file into a DataFrame
df = pd.read_excel('input.xlsx')

# Map column names to new keys
column_mapping = {
    'Order': '2',
    'Order Line': '3',
    'Quantity': '10'
}

# Rename columns
df = df.rename(columns=column_mapping)

# Convert DataFrame to JSON format
json_data = df.to_dict(orient='records')

# Write JSON data to a file
with open('output.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print("JSON file 'output.json' has been successfully created.")
