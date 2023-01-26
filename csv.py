# import the necessary libraries
import csv
from pymongo import MongoClient

# connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# specify the database and collection
db = client["BDD_FOOT"]
collection = db["BundesligaValeur"]

# read the CSV file
with open("Allemagne.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# insert the data into the collection
collection.insert_many(data)




# specify the database and collection
db = client["BDD_FOOT"]
collection = db["LigaValeur"]

# read the CSV file
with open("Espagne_1.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# insert the data into the collection
collection.insert_many(data)




db = client["BDD_FOOT"]
collection = db["Ligue1Valeur"]

# read the CSV file
with open("France.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# insert the data into the collection
collection.insert_many(data)




db = client["BDD_FOOT"]
collection = db["LiganosValeur"]

# read the CSV file
with open("Portugal.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# insert the data into the collection
collection.insert_many(data)



db = client["BDD_FOOT"]
collection = db["SerieaValeur"]

# read the CSV file
with open("Italie.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# insert the data into the collection
collection.insert_many(data)

# close the connection



db = client["BDD_FOOT"]
collection = db["PremierleagueValeur"]

# read the CSV file
with open("Angleterre.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# insert the data into the collection
collection.insert_many(data)

# close the connection
client.close()