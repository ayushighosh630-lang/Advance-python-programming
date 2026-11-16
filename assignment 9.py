import csv
import json

# CSV file path
filename = "addresses.csv"

# Read data from CSV file
data = []

with open(filename, "r") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        data.append(row)

# Convert CSV data into JSON format
json_data = json.dumps(data, indent=4)

# Write JSON data to output file
with open("output.json", "w") as file:
    file.write(json_data)

# Display output
print("CSV data successfully converted into JSON format.")
print(json_data)