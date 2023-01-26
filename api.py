import requests
import json
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["BDD_FOOT"]
collection = db["premier_league"]

# Make the GET request to the API
url = "http://api.football-data.org/v4/competitions/PL/standings?season=2022"
headers = {"X-Auth-Token": "1bf86dc9d65746149a26808fdc45a5a1"}
response = requests.get(url, headers=headers)

# Check the response status code
if response.status_code != 200:
    print("Error: Failed to retrieve data from API")
else:
    # Parse the response into a Python dictionary
    data = json.loads(response.text)
    # Insert the teams data into the collection
    collection.insert_many(data['standings'][0]['table'])
    print("Data inserted successfully.")


collection = db["serie_a"]


# Make the GET request to the API
url = "http://api.football-data.org/v4/competitions/SA/standings?season=2022"
headers = {"X-Auth-Token": "1bf86dc9d65746149a26808fdc45a5a1"}
response = requests.get(url, headers=headers)

# Check the response status code
if response.status_code != 200:
    print("Error: Failed to retrieve data from API")
else:
    # Parse the response into a Python dictionary
    data = json.loads(response.text)
    # Insert the teams data into the collection
    collection.insert_many(data['standings'][0]['table'])
    print("Data inserted successfully.")

collection = db["ligue_1"]

# Make the GET request to the API
url = "http://api.football-data.org/v4/competitions/FL1/standings?season=2022"
headers = {"X-Auth-Token": "1bf86dc9d65746149a26808fdc45a5a1"}
response = requests.get(url, headers=headers)


# Check the response status code
if response.status_code != 200:
    print("Error: Failed to retrieve data from API")
else:
    # Parse the response into a Python dictionary
    data = json.loads(response.text)
    # Insert the teams data into the collection
    collection.insert_many(data['standings'][0]['table'])
    print("Data inserted successfully.")

    collection = db["bundesliga"]

# Make the GET request to the API
url = "http://api.football-data.org/v4/competitions/BL1/standings?season=2022"
headers = {"X-Auth-Token": "1bf86dc9d65746149a26808fdc45a5a1"}
response = requests.get(url, headers=headers)


# Check the response status code
if response.status_code != 200:
    print("Error: Failed to retrieve data from API")
else:
    # Parse the response into a Python dictionary
    data = json.loads(response.text)
    # Insert the teams data into the collection
    collection.insert_many(data['standings'][0]['table'])
    print("Data inserted successfully.")

    collection = db["liga"]

    # Make the GET request to the API
    url = "http://api.football-data.org/v4/competitions/PD/standings?season=2022"
    headers = {"X-Auth-Token": "1bf86dc9d65746149a26808fdc45a5a1"}
    response = requests.get(url, headers=headers)

    # Check the response status code
    if response.status_code != 200:
        print("Error: Failed to retrieve data from API")
    else:
        # Parse the response into a Python dictionary
        data = json.loads(response.text)
        # Insert the teams data into the collection
        collection.insert_many(data['standings'][0]['table'])
        print("Data inserted successfully.")

    collection = db["liga_nos"]

    # Make the GET request to the API
    url = "http://api.football-data.org/v4/competitions/PPL/standings?season=2022"
    headers = {"X-Auth-Token": "1bf86dc9d65746149a26808fdc45a5a1"}
    response = requests.get(url, headers=headers)

    # Check the response status code
    if response.status_code != 200:
        print("Error: Failed to retrieve data from API")
    else:
        # Parse the response into a Python dictionary
        data = json.loads(response.text)
        # Insert the teams data into the collection
        collection.insert_many(data['standings'][0]['table'])
        print("Data inserted successfully.")







