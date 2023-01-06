import urllib.request

#List of us states
states = [
    "Alabama",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming",
    "Alaska"
]

# Folder path
path = "/Users/rohlaxelskaara/Desktop/us_weather_data_2"

# Itterate through each state
for state in range(1, len(states)+1):

    # Creating the filenames, including state and weather parameter
    new_name_temp = states[state-1] + "_" + "temperature.csv"
    new_name_prec = states[state - 1] + "_" + "precipitation.csv"

    # Alaska is set as 50, hawaii does not exist
    if state == 49:
        state = 50

    # Download the csv for temperature and precipitation for each state
    temperature = f"https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/{state}/tavg/all/1/1970-2022.csv"
    precipitation = f"https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/{state}/pcp/all/1/1970-2022.csv"

    # Save the csv to a specified folder
    urllib.request.urlretrieve(temperature, "{}/{}".format(path, new_name_temp))
    urllib.request.urlretrieve(precipitation, "{}/{}".format(path, new_name_prec))

