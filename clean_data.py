import csv
import os

# Set the path to the folder containing the CSV files
path = "/Users/rohlaxelskaara/Desktop/us_weather_data_2"

# Iterate through the files in the folder
for filename in os.listdir(path):

    # Open the file and read the rows
    with open(os.path.join(path, filename), "r") as csv_file:
        rows = [row for row in csv.reader(csv_file)]

    # Store all data from row 4 and down
    rows = rows[3:]

    # Extract the state name and weather type from the filename
    state = filename.split("_")[0]
    weather_type = filename.split("_")[1][:-4]

    # Add the state and type columns to each row
    rows[0].append("type")
    rows[0].append("state")

    # Append headings for new columns
    for row in rows[1:]:
        row.append(weather_type)
        row.append(state)

    # Write the rows to a new file
    with open(os.path.join(path, filename), "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in rows:
            csv_writer.writerow(row)
