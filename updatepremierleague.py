import pymongo
from tkinter import *

# Connect to the MongoDB client
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the database and collection
db = client["BDD_FOOT"]
collection = db["premier_league"]

# GUI for updating the document
root = Tk()
root.title("Update Document")
root.geometry("400x200")

# Label and entry widget for team name
team_shortName_label = Label(root, text="Entrer le nom d'une Equipe: ")
team_shortName_label.grid(row=0, column=1, sticky="W")
team_shortName_entry = Entry(root)
team_shortName_entry.grid(row=0, column=2, sticky="W")

# Update button
def update_document():
    team_shortName= team_shortName_entry.get()
    # Get the document from the collection based on the team name
    document = collection.find_one({"team.shortName": team_shortName})
    if document:
        # Labels for displaying current values
        position_label = Label(root, text="Position: " + str(document["position"]))
        position_label.grid(row=1, column=2, sticky="W")
        id_label = Label(root, text="id: " + str(document["team"]["id"]))
        id_label.grid(row=2, column=2, sticky="W")
        team_label = Label(root, text="Team: " + document["team"]["name"])
        team_label.grid(row=3, column=2, sticky="W")
        shortName_label = Label(root, text="shortName: " + document["team"]["shortName"])
        shortName_label.grid(row=4, column=2, sticky="W")
        tla_label = Label(root, text="tla: " + document["team"]["tla"])
        tla_label.grid(row=5, column=2, sticky="W")
        crest_label = Label(root, text="crest: " + document["team"]["crest"])
        crest_label.grid(row=6, column=2, sticky="W")
        played_games_label = Label(root, text="Played Games: " + str(document["playedGames"]))
        played_games_label.grid(row=7, column=2, sticky="W")
        form_label = Label(root, text="Form: " + document["form"])
        form_label.grid(row=8, column=2, sticky="W")
        won_label = Label(root, text="Won: " + str(document["won"]))
        won_label.grid(row=9, column=2, sticky="W")
        draw_label = Label(root, text="Draw: " + str(document["draw"]))
        draw_label.grid(row=10, column=2, sticky="W")
        lost_label = Label(root, text="Lost: " + str(document["lost"]))
        lost_label.grid(row=11, column=2, sticky="W")
        points_label = Label(root, text="Points: " + str(document["points"]))
        points_label.grid(row=12, column=2, sticky="W")
        goals_for_label = Label(root, text="Goals For: " + str(document["goalsFor"]))
        goals_for_label.grid(row=13, column=2, sticky="W")
        goals_against_label = Label(root, text="Goals Against: " + str(document["goalsAgainst"]))
        goals_against_label.grid(row=14, column=2, sticky="W")
        goal_diff_label = Label(root, text="Goal Difference: " + str(document["goalDifference"]))
        goal_diff_label.grid(row=15, column=2, sticky="W")

        # Entry widgets for updating the values
        position_entry = Entry(root)
        position_entry.grid(row=1, column=3, sticky="W")
        id_entry = Entry(root)
        id_entry.grid(row=2, column=3, sticky="W")
        team_entry = Entry(root)
        team_entry.grid(row=3, column=3, sticky="W")
        shortName_entry = Entry(root)
        shortName_entry.grid(row=4, column=3, sticky="W")
        tla_entry = Entry(root)
        tla_entry.grid(row=5, column=3, sticky="W")
        crest_entry = Entry(root)
        crest_entry.grid(row=6, column=3, sticky="W")
        played_games_entry = Entry(root)
        played_games_entry.grid(row=7, column=3, sticky="W")
        form_entry = Entry(root)
        form_entry.grid(row=8, column=3, sticky="W")
        won_entry = Entry(root)
        won_entry.grid(row=9, column=3, sticky="W")
        draw_entry = Entry(root)
        draw_entry.grid(row=10, column=3, sticky="W")
        lost_entry = Entry(root)
        lost_entry.grid(row=11, column=3, sticky="W")
        points_entry = Entry(root)
        points_entry.grid(row=12, column=3, sticky="W")
        goals_for_entry = Entry(root)
        goals_for_entry.grid(row=13, column=3, sticky="W")
        goals_against_entry = Entry(root)
        goals_against_entry.grid(row=14, column=3, sticky="W")
        goal_diff_entry = Entry(root)
        goal_diff_entry.grid(row=15, column=3, sticky="W")
        def update_data():
            # Get the updated values from the entry widgets
            document["position"] = int(position_entry.get())
            document["team"]["id"] = int(id_entry.get())
            document["team"]["name"] = team_entry.get()
            document["team"]["shortName"] = shortName_entry.get()
            document["team"]["tla"] = tla_entry.get()
            document["team"]["crest"] = crest_entry.get()
            document["playedGames"] = int(played_games_entry.get())
            document["form"] = form_entry.get()
            document["won"] = int(won_entry.get())
            document["draw"] = int(draw_entry.get())
            document["lost"] = int(lost_entry.get())
            document["points"] = int(points_entry.get())
            document["goalsFor"] = int(goals_for_entry.get())
            document["goalsAgainst"] = int(goals_against_entry.get())
            document["goalDifference"] = int(goal_diff_entry.get())

            # Update the document in the collection
            collection.update_one({"_id": document["_id"]}, {"$set": document})

            # Update the labels with the new values
            position_label.config(text="Position: " + str(document["position"]))
            id_label.config(text="id: " + str(document["team"]["id"]))
            team_label.config(text="Equipe: " + document["team"]["name"])
            shortName_label.config(text="Diminutif: " + document["team"]["shortName"])
            tla_label.config(text="Initial: " + document["team"]["tla"])
            crest_label.config(text="Image: " + document["team"]["crest"])
            played_games_label.config(text="MJ: " + str(document["playedGames"]))
            form_label.config(text="Form: " + document["form"])
            won_label.config(text="G: " + str(document["won"]))
            draw_label.config(text="N: " + str(document["draw"]))
            lost_label.config(text="P: " + str(document["lost"]))
            points_label.config(text="Pts: " + str(document["points"]))
            goals_for_label.config(text="BP: " + str(document["goalsFor"]))
            goals_against_label.config(text="BC: " + str(document["goalsAgainst"]))
            goal_diff_label.config(text="DB: " + str(document["goalDifference"]))
        update_data_button = Button(root, text="Mise a jour de l'équipe", command=update_data)
        update_data_button.grid(row=18, column=3, sticky="W")
    else:
        team_not_found_label = Label(root, text="Equipe non trouvé")
        team_not_found_label.grid(row=16, column=3, sticky="W")

update_button = Button(root, text="Rechercher", command=update_document)
update_button.grid(row=0, column=3, sticky="W")
root.mainloop()