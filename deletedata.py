import pymongo
from tkinter import *

# Connect to the MongoDB client
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the database and collection
db = client["BDD_FOOT"]
collection = db["premier_league"]



# GUI for deleting the document
root = Tk()
root.title("Delete Document")
root.geometry("400x200")

# Label and entry widget for team name
team_shortName_label = Label(root, text="Entré le nom d'une Equipe: ")
team_shortName_label.grid(row=0, column=0, padx=5, pady=5,sticky='w')
team_shortName_entry = Entry(root)
team_shortName_entry.grid(row=0, column=1, padx=5, pady=5)

# Delete button
def delete_document():
    team_shortName = team_shortName_entry.get()
    # Get the document from the collection based on the team name
    document = collection.find_one({"team.shortName": team_shortName})
    if document:
        collection.delete_one({"_id": document["_id"]})
        deleted_label = Label(root, text="Equipe supprimé")
        deleted_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5,sticky='w')
    else:
        team_not_found_label = Label(root, text="Equipe non trouvé")
        team_not_found_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5,sticky='w')

delete_button = Button(root, text="Supprimer", command=delete_document)
delete_button.grid(row=0, column=2, padx=5, pady=5,sticky='e')

root.mainloop()

