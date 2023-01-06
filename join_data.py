import csv
import os

# Set the path to the folder containing the csv files
path = "/Users/rohlaxelskaara/Desktop/us_weather_data"

# Open a new csv file to write the data to
with open('us_weather_data.csv', 'w', newline='') as output_file:
    # Create a writer object
    writer = csv.writer(output_file)

    # Iterate through the files in the folder
    for file in os.listdir(path):
        # Open the csv file
        with open(os.path.join(path, file), 'r') as input_file:
            # Create a reader object
            reader = csv.reader(input_file)
            # Skip the first row
            next(reader)
            # Write the rest of the rows to the output file
            for row in reader:
                writer.writerow(row)