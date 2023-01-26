import tkinter as tk
from tkinter import ttk
from tkinter import *
import pymongo



class Example(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Premierleague)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()


class Premierleague(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.iconbitmap('logo.ico')
        master.title("Football Stats")
        ttk.Button(self, text="Liga",
                   command=lambda: master.switch_frame(Liga)).grid(row=2, column=0, sticky="W")

        ttk.Button(self, text="Serie A",
                   command=lambda: master.switch_frame(Seriea)).grid(row=2, column=1, sticky="W")
        ttk.Button(self, text="Ligue 1",
                   command=lambda: master.switch_frame(Ligue1)).grid(row=2, column=2, sticky="W")
        ttk.Button(self, text="Bundesliga",
                   command=lambda: master.switch_frame(Bundesliga)).grid(row=2, column=3, sticky="W")
        ttk.Button(self, text="Liga Nos",
                   command=lambda: master.switch_frame(Liganos)).grid(row=2, column=4, sticky="W")
        ttk.Button(self, text="Supprimer une Equipe de Premier League",
                   command=lambda: master.switch_frame(Delete_premier_league)).grid(row=3, column=5, sticky="W")
        ttk.Button(self, text="Valeur Marchande Premier League",
                   command=lambda: master.switch_frame(PremierleagueValeur)).grid(row=4, column=5, sticky="W")

        self.table = ttk.Treeview(self)
        self.table["columns"] = ("nom", "position", "points", "matchjoue", "gagne", "nul", "perdu", "bp", "bc", "db")
        self.table.column("nom", width=200)
        self.table.column("position", width=100)
        self.table.column("points", width=50)
        self.table.column("matchjoue", width=50)
        self.table.column("gagne", width=50)
        self.table.column("nul", width=50)
        self.table.column("perdu", width=50)
        self.table.column("bp", width=50)
        self.table.column("bc", width=50)
        self.table.column("db", width=50)

        self.table.heading("nom", text="Premier League")
        self.table.heading("position", text="Position")
        self.table.heading("points", text="Pts")
        self.table.heading("matchjoue", text="MJ")
        self.table.heading("gagne", text="G")
        self.table.heading("nul", text="N")
        self.table.heading("perdu", text="P")
        self.table.heading("bp", text="BP")
        self.table.heading("bc", text="BC")
        self.table.heading("db", text="DB")

        self.table.configure(height=20)
        self.table.grid(row=2, column=5, sticky="W")

        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["BDD_FOOT"]
        collection = db["COLLECTION_FOOT"]

        data = db.premier_league.find()
        for e in data:
            self.table.insert("", "end", values=(
            e['team']['shortName'], e['position'], e['points'], e["playedGames"], e["won"], e["draw"], e["lost"],
            e["goalsFor"], e["goalsAgainst"], e["goalDifference"]))


class Liga(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ttk.Button(self, text="Premier League",
                   command=lambda: master.switch_frame(Premierleague)).grid(row=2, column=0, sticky="W")
        ttk.Button(self, text="Serie A",
                   command=lambda: master.switch_frame(Seriea)).grid(row=2, column=1, sticky="W")
        ttk.Button(self, text="Ligue 1",
                   command=lambda: master.switch_frame(Ligue1)).grid(row=2, column=2, sticky="W")
        ttk.Button(self, text="Bundesliga",
                   command=lambda: master.switch_frame(Bundesliga)).grid(row=2, column=3, sticky="W")
        ttk.Button(self, text="Liga Nos",
                   command=lambda: master.switch_frame(Liganos)).grid(row=2, column=4, sticky="W")
        ttk.Button(self, text="Supprimer une Equipe de Liga",
                   command=lambda: master.switch_frame(Delete_liga)).grid(row=3, column=5, sticky="W")
        ttk.Button(self, text="Valeur Marchande Liga",
                   command=lambda: master.switch_frame(LigaValeur)).grid(row=4, column=5, sticky="W")
        self.table = ttk.Treeview(self)
        self.table["columns"] = ("nom", "position", "points", "matchjoue", "gagne", "nul", "perdu", "bp", "bc", "db")
        self.table.column("nom", width=200)
        self.table.column("position", width=100)
        self.table.column("points", width=50)
        self.table.column("matchjoue", width=50)
        self.table.column("gagne", width=50)
        self.table.column("nul", width=50)
        self.table.column("perdu", width=50)
        self.table.column("bp", width=50)
        self.table.column("bc", width=50)
        self.table.column("db", width=50)

        self.table.heading("nom", text="Liga")
        self.table.heading("position", text="Position")
        self.table.heading("points", text="Pts")
        self.table.heading("matchjoue", text="MJ")
        self.table.heading("gagne", text="G")
        self.table.heading("nul", text="N")
        self.table.heading("perdu", text="P")
        self.table.heading("bp", text="BP")
        self.table.heading("bc", text="BC")
        self.table.heading("db", text="DB")
        self.table.configure(height=20)
        self.table.grid(row=2, column=5, sticky="W")

        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["BDD_FOOT"]
        collection = db["COLLECTION_FOOT"]

        data = db.liga.find()
        for e in data:
            self.table.insert("", "end", values=(
                e['team']['shortName'], e['position'], e['points'], e["playedGames"], e["won"], e["draw"], e["lost"],
                e["goalsFor"], e["goalsAgainst"], e["goalDifference"]))


class Seriea(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ttk.Button(self, text="Premier League",
                   command=lambda: master.switch_frame(Premierleague)).grid(row=2, column=0, sticky="W")
        ttk.Button(self, text="Liga",
                   command=lambda: master.switch_frame(Liga)).grid(row=2, column=1, sticky="W")
        ttk.Button(self, text="Ligue 1",
                   command=lambda: master.switch_frame(Ligue1)).grid(row=2, column=2, sticky="W")
        ttk.Button(self, text="Bundesliga",
                   command=lambda: master.switch_frame(Bundesliga)).grid(row=2, column=3, sticky="W")
        ttk.Button(self, text="Liga Nos",
                   command=lambda: master.switch_frame(Liganos)).grid(row=2, column=4, sticky="W")
        ttk.Button(self, text="Supprimer une Equipe de Série A",
                   command=lambda: master.switch_frame(Delete_serie_a)).grid(row=3, column=5, sticky="W")
        ttk.Button(self, text="Valeur Marchande Série A",
                   command=lambda: master.switch_frame(SerieaValeur)).grid(row=4, column=5, sticky="W")
        self.table = ttk.Treeview(self)
        self.table["columns"] = ("nom", "position", "points", "matchjoue", "gagne", "nul", "perdu", "bp", "bc", "db")
        self.table.column("nom", width=200)
        self.table.column("position", width=100)
        self.table.column("points", width=50)
        self.table.column("matchjoue", width=50)
        self.table.column("gagne", width=50)
        self.table.column("nul", width=50)
        self.table.column("perdu", width=50)
        self.table.column("bp", width=50)
        self.table.column("bc", width=50)
        self.table.column("db", width=50)

        self.table.heading("nom", text="Serie A")
        self.table.heading("position", text="Position")
        self.table.heading("points", text="Pts")
        self.table.heading("matchjoue", text="MJ")
        self.table.heading("gagne", text="G")
        self.table.heading("nul", text="N")
        self.table.heading("perdu", text="P")
        self.table.heading("bp", text="BP")
        self.table.heading("bc", text="BC")
        self.table.heading("db", text="DB")
        self.table.configure(height=20)
        self.table.grid(row=2, column=5, sticky="W")

        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["BDD_FOOT"]
        collection = db["COLLECTION_FOOT"]

        data = db.serie_a.find()
        for e in data:
            self.table.insert("", "end", values=(
                e['team']['shortName'], e['position'], e['points'], e["playedGames"], e["won"], e["draw"], e["lost"],
                e["goalsFor"], e["goalsAgainst"], e["goalDifference"]))


class Ligue1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ttk.Button(self, text="Premier League",
                   command=lambda: master.switch_frame(Premierleague)).grid(row=2, column=0, sticky="W")
        ttk.Button(self, text="Liga",
                   command=lambda: master.switch_frame(Liga)).grid(row=2, column=1, sticky="W")
        ttk.Button(self, text="Serie A",
                   command=lambda: master.switch_frame(Seriea)).grid(row=2, column=2, sticky="W")
        ttk.Button(self, text="Bundesliga",
                   command=lambda: master.switch_frame(Bundesliga)).grid(row=2, column=3, sticky="W")
        ttk.Button(self, text="Liga Nos",
                   command=lambda: master.switch_frame(Liganos)).grid(row=2, column=4, sticky="W")
        ttk.Button(self, text="Supprimer une Equipe de Ligue 1",
                   command=lambda: master.switch_frame(Delete_ligue_1)).grid(row=3, column=5, sticky="W")
        ttk.Button(self, text="Valeur Marchande Ligue 1",
                   command=lambda: master.switch_frame(Ligue1Valeur)).grid(row=4, column=5, sticky="W")
        self.table = ttk.Treeview(self)
        self.table["columns"] = ("nom", "position", "points", "matchjoue", "gagne", "nul", "perdu", "bp", "bc", "db")
        self.table.column("nom", width=200)
        self.table.column("position", width=100)
        self.table.column("points", width=50)
        self.table.column("matchjoue", width=50)
        self.table.column("gagne", width=50)
        self.table.column("nul", width=50)
        self.table.column("perdu", width=50)
        self.table.column("bp", width=50)
        self.table.column("bc", width=50)
        self.table.column("db", width=50)

        self.table.heading("nom", text="Ligue 1")
        self.table.heading("position", text="Position")
        self.table.heading("points", text="Pts")
        self.table.heading("matchjoue", text="MJ")
        self.table.heading("gagne", text="G")
        self.table.heading("nul", text="N")
        self.table.heading("perdu", text="P")
        self.table.heading("bp", text="BP")
        self.table.heading("bc", text="BC")
        self.table.heading("db", text="DB")
        self.table.configure(height=20)
        self.table.grid(row=2, column=5, sticky="W")

        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["BDD_FOOT"]


        data = db.ligue_1.find()
        for e in data:
            self.table.insert("", "end", values=(
                e['team']['shortName'], e['position'], e['points'], e["playedGames"], e["won"], e["draw"], e["lost"],
                e["goalsFor"], e["goalsAgainst"], e["goalDifference"]))


class Bundesliga(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ttk.Button(self, text="Premier League",
                   command=lambda: master.switch_frame(Premierleague)).grid(row=2, column=0, sticky="W")
        ttk.Button(self, text="Liga",
                   command=lambda: master.switch_frame(Liga)).grid(row=2, column=1, sticky="W")
        ttk.Button(self, text="Serie A",
                   command=lambda: master.switch_frame(Seriea)).grid(row=2, column=2, sticky="W")
        ttk.Button(self, text="Ligue 1",
                   command=lambda: master.switch_frame(Ligue1)).grid(row=2, column=3, sticky="W")
        ttk.Button(self, text="Liga Nos",
                   command=lambda: master.switch_frame(Liganos)).grid(row=2, column=4, sticky="W")
        ttk.Button(self, text="Supprimer une Equipe de bundesliga",
                   command=lambda: master.switch_frame(Delete_bundesliga)).grid(row=3, column=5, sticky="W")
        ttk.Button(self, text="Valeur Marchande Bundesliga",
                   command=lambda: master.switch_frame(BundesligaValeur)).grid(row=4, column=5, sticky="W")
        self.table = ttk.Treeview(self)
        self.table["columns"] = ("nom", "position", "points", "matchjoue", "gagne", "nul", "perdu", "bp", "bc", "db")
        self.table.column("nom", width=200)
        self.table.column("position", width=100)
        self.table.column("points", width=50)
        self.table.column("matchjoue", width=50)
        self.table.column("gagne", width=50)
        self.table.column("nul", width=50)
        self.table.column("perdu", width=50)
        self.table.column("bp", width=50)
        self.table.column("bc", width=50)
        self.table.column("db", width=50)

        self.table.heading("nom", text="Bundesliga")
        self.table.heading("position", text="Position")
        self.table.heading("points", text="Pts")
        self.table.heading("matchjoue", text="MJ")
        self.table.heading("gagne", text="G")
        self.table.heading("nul", text="N")
        self.table.heading("perdu", text="P")
        self.table.heading("bp", text="BP")
        self.table.heading("bc", text="BC")
        self.table.heading("db", text="DB")
        self.table.configure(height=20)
        self.table.grid(row=2, column=5, sticky="W")

        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["BDD_FOOT"]
        collection = db["COLLECTION_FOOT"]

        data = db.bundesliga.find()
        for e in data:
            self.table.insert("", "end", values=(
                e['team']['shortName'], e['position'], e['points'], e["playedGames"], e["won"], e["draw"], e["lost"],
                e["goalsFor"], e["goalsAgainst"], e["goalDifference"]))


class Liganos(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ttk.Button(self, text="Premier League",
                   command=lambda: master.switch_frame(Premierleague)).grid(row=2, column=0, sticky="W")
        ttk.Button(self, text="Liga",
                   command=lambda: master.switch_frame(Liga)).grid(row=2, column=1, sticky="W")
        ttk.Button(self, text="Serie A",
                   command=lambda: master.switch_frame(Seriea)).grid(row=2, column=2, sticky="W")
        ttk.Button(self, text="Ligue 1",
                   command=lambda: master.switch_frame(Ligue1)).grid(row=2, column=3, sticky="W")
        ttk.Button(self, text="Bundesliga",
                   command=lambda: master.switch_frame(Bundesliga)).grid(row=2, column=4, sticky="W")
        ttk.Button(self, text="Supprimer une Equipe de Liga Nos",
                   command=lambda: master.switch_frame(Delete_liga_nos)).grid(row=3, column=5, sticky="W")
        ttk.Button(self, text="Valeur Marchande Liga Nos",
                   command=lambda: master.switch_frame(LiganosValeur)).grid(row=4, column=5, sticky="W")
        self.table = ttk.Treeview(self)
        self.table["columns"] = ("nom", "position", "points", "matchjoue", "gagne", "nul", "perdu", "bp", "bc", "db")
        self.table.column("nom", width=200)
        self.table.column("position", width=100)
        self.table.column("points", width=50)
        self.table.column("matchjoue", width=50)
        self.table.column("gagne", width=50)
        self.table.column("nul", width=50)
        self.table.column("perdu", width=50)
        self.table.column("bp", width=50)
        self.table.column("bc", width=50)
        self.table.column("db", width=50)

        self.table.heading("nom", text="Liga Nos")
        self.table.heading("position", text="Position")
        self.table.heading("points", text="Pts")
        self.table.heading("matchjoue", text="MJ")
        self.table.heading("gagne", text="G")
        self.table.heading("nul", text="N")
        self.table.heading("perdu", text="P")
        self.table.heading("bp", text="BP")
        self.table.heading("bc", text="BC")
        self.table.heading("db", text="DB")
        self.table.configure(height=20)
        self.table.grid(row=2, column=5, sticky="W")

        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["BDD_FOOT"]
        collection = db["COLLECTION_FOOT"]

        data = db.liga_nos.find()
        for e in data:
            self.table.insert("", "end", values=(
                e['team']['shortName'], e['position'], e['points'], e["playedGames"], e["won"], e["draw"], e["lost"],
                e["goalsFor"], e["goalsAgainst"], e["goalDifference"]))

class Delete_premier_league(tk.Frame):

 def __init__(self, master):


    # Connect to the MongoDB client
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Select the database and collection
    db = client["BDD_FOOT"]
    collection = db["premier_league"]
    # Label and entry widget for team name

    tk.Frame.__init__(self, master)
    ttk.Button(self, text="Premier League",
               command=lambda: master.switch_frame(Premierleague)).grid(row=2, column=0, sticky="W")

    # Delete button
    def delete_document():
            team_shortName = team_shortName_entry.get()
        # Get the document from the collection based on the team name
            document = collection.find_one({"team.shortName": team_shortName})
            if document:
                collection.delete_one({"_id": document["_id"]})
                deleted_label = Label(master, text="Equipe supprimé")
                deleted_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')
            else:
                team_not_found_label = Label(master, text="Equipe non trouvé")
                team_not_found_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')



    tk.Frame.__init__(self, master)
    ttk.delete_button = Button(master, text="Supprimer", command=delete_document)
    ttk.delete_button.grid(row=0, column=2, padx=5, pady=5, sticky='e')
    ttk.Button(self, text="Premier League",
               command=lambda: master.switch_frame(Premierleague)).grid(row=2, column=0, sticky="W")

    team_shortName_label = Label(master, text="Entré le nom d'une Equipe: ")
    team_shortName_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    team_shortName_entry = Entry(master)
    team_shortName_entry.grid(row=0, column=1, padx=5, pady=5)

class Delete_liga(tk.Frame):
 def __init__(self, master):
    # Connect to the MongoDB client
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Select the database and collection
    db = client["BDD_FOOT"]
    collection = db["liga"]
    # Label and entry widget for team name
    team_shortName_label = Label(master, text="Entré le nom d'une Equipe: ")
    team_shortName_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    team_shortName_entry = Entry(master)
    team_shortName_entry.grid(row=0, column=1, padx=5, pady=5)

    # Delete button
    def delete_document():
        team_shortName = team_shortName_entry.get()
        # Get the document from the collection based on the team name
        document = collection.find_one({"team.shortName": team_shortName})
        if document:
            collection.delete_one({"_id": document["_id"]})
            deleted_label = Label(master, text="Equipe supprimé")
            deleted_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')
        else:
            team_not_found_label = Label(master, text="Equipe non trouvé")
            team_not_found_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')

    delete_button = Button(master, text="Supprimer", command=delete_document)
    delete_button.grid(row=0, column=2, padx=5, pady=5, sticky='e')


class Delete_serie_a(tk.Frame):
 def __init__(self, master):
    # Connect to the MongoDB client
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Select the database and collection
    db = client["BDD_FOOT"]
    collection = db["serie_a"]
    # Label and entry widget for team name
    team_shortName_label = Label(master, text="Entré le nom d'une Equipe: ")
    team_shortName_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    team_shortName_entry = Entry(master)
    team_shortName_entry.grid(row=0, column=1, padx=5, pady=5)

    # Delete button
    def delete_document():
        team_shortName = team_shortName_entry.get()
        # Get the document from the collection based on the team name
        document = collection.find_one({"team.shortName": team_shortName})
        if document:
            collection.delete_one({"_id": document["_id"]})
            deleted_label = Label(master, text="Equipe supprimé")
            deleted_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')
        else:
            team_not_found_label = Label(master, text="Equipe non trouvé")
            team_not_found_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')

    delete_button = Button(master, text="Supprimer", command=delete_document)
    delete_button.grid(row=0, column=2, padx=5, pady=5, sticky='e')

class Delete_ligue_1(tk.Frame):
 def __init__(self, master):
    # Connect to the MongoDB client
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Select the database and collection
    db = client["BDD_FOOT"]
    collection = db["ligue_1"]
    # Label and entry widget for team name
    team_shortName_label = Label(master, text="Entré le nom d'une Equipe: ")
    team_shortName_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    team_shortName_entry = Entry(master)
    team_shortName_entry.grid(row=0, column=1, padx=5, pady=5)

    # Delete button
    def delete_document():
        team_shortName = team_shortName_entry.get()
        # Get the document from the collection based on the team name
        document = collection.find_one({"team.shortName": team_shortName})
        if document:
            collection.delete_one({"_id": document["_id"]})
            deleted_label = Label(master, text="Equipe supprimé")
            deleted_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')
        else:
            team_not_found_label = Label(master, text="Equipe non trouvé")
            team_not_found_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')

    delete_button = Button(master, text="Supprimer", command=delete_document)
    delete_button.grid(row=0, column=2, padx=5, pady=5, sticky='e')

class Delete_bundesliga(tk.Frame):
 def __init__(self, master):
    # Connect to the MongoDB client
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Select the database and collection
    db = client["BDD_FOOT"]
    collection = db["bundesliga"]
    # Label and entry widget for team name
    team_shortName_label = Label(master, text="Entré le nom d'une Equipe: ")
    team_shortName_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    team_shortName_entry = Entry(master)
    team_shortName_entry.grid(row=0, column=1, padx=5, pady=5)

    # Delete button
    def delete_document():
        team_shortName = team_shortName_entry.get()
        # Get the document from the collection based on the team name
        document = collection.find_one({"team.shortName": team_shortName})
        if document:
            collection.delete_one({"_id": document["_id"]})
            deleted_label = Label(master, text="Equipe supprimé")
            deleted_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')
        else:
            team_not_found_label = Label(master, text="Equipe non trouvé")
            team_not_found_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')

    delete_button = Button(master, text="Supprimer", command=delete_document)
    delete_button.grid(row=0, column=2, padx=5, pady=5, sticky='e')

class Delete_liga_nos(tk.Frame):
 def __init__(self, master):
    # Connect to the MongoDB client
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Select the database and collection
    db = client["BDD_FOOT"]
    collection = db["liga_nos"]
    # Label and entry widget for team name
    team_shortName_label = Label(master, text="Entré le nom d'une Equipe: ")
    team_shortName_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    team_shortName_entry = Entry(master)
    team_shortName_entry.grid(row=0, column=1, padx=5, pady=5)

    # Delete button
    def delete_document():
        team_shortName = team_shortName_entry.get()
        # Get the document from the collection based on the team name
        document = collection.find_one({"team.shortName": team_shortName})
        if document:
            collection.delete_one({"_id": document["_id"]})
            deleted_label = Label(master, text="Equipe supprimé")
            deleted_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')
        else:
            team_not_found_label = Label(master, text="Equipe non trouvé")
            team_not_found_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')

    delete_button = Button(master, text="Supprimer", command=delete_document)
    delete_button.grid(row=0, column=2, padx=5, pady=5, sticky='e')





class PremierleagueValeur(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ttk.Button(self, text="Premier League",
                   command=lambda: master.switch_frame(Premierleague)).grid(row=2, column=0, sticky="W")

        self.table = ttk.Treeview(self)
        self.table["columns"] = ("Club", "Valeurs","position","points","playedGames","won","draw","lost","goalsFor","goalsAgainst","goalDifference","form")
        self.table.column("Club", width=200)
        self.table.column("Valeurs", width=200)
        self.table.column("position", width=70)
        self.table.column("points", width=70)
        self.table.column("playedGames", width=40)
        self.table.column("won", width=40)
        self.table.column("draw", width=40)
        self.table.column("lost", width=40)
        self.table.column("goalsFor", width=40)
        self.table.column("goalsAgainst", width=40)
        self.table.column("goalDifference", width=40)
        self.table.column("form", width=90)


        self.table.heading("Club", text="Premier League")
        self.table.heading("Valeurs", text="Valeur Marchande (en Millions €)")
        self.table.heading("position", text="Position")
        self.table.heading("points", text="Points")
        self.table.heading("playedGames", text="MJ")
        self.table.heading("won", text="G")
        self.table.heading("draw", text="N")
        self.table.heading("lost", text="L")
        self.table.heading("goalsFor", text="BP")
        self.table.heading("goalsAgainst", text="BC")
        self.table.heading("goalDifference", text="BD")
        self.table.heading("form", text="DB")
        self.table.configure(height=20)
        self.table.grid(row=2, column=5, sticky="W")

        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["BDD_FOOT"]
        collection = db["PremierleagueValeur"]

        data = db.PremierleagueValeur.find()
        for e in data:
            self.table.insert("", "end", values=(e["Club"], e["Valeurs"],e["position"],e["points"],e["playedGames"],e["won"],e["draw"],e["lost"],e["goalsFor"],e["goalsAgainst"],e["goalDifference"],e["form"]))


class LigaValeur(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ttk.Button(self, text="Liga",
                   command=lambda: master.switch_frame(Liga)).grid(row=2, column=0, sticky="W")

        self.table = ttk.Treeview(self)
        self.table["columns"] = ("Club", "Valeurs","position","points","playedGames","won","draw","lost","goalsFor","goalsAgainst","goalDifference","form")
        self.table.column("Club", width=200)
        self.table.column("Valeurs", width=200)
        self.table.column("position", width=70)
        self.table.column("points", width=70)
        self.table.column("playedGames", width=40)
        self.table.column("won", width=40)
        self.table.column("draw", width=40)
        self.table.column("lost", width=40)
        self.table.column("goalsFor", width=40)
        self.table.column("goalsAgainst", width=40)
        self.table.column("goalDifference", width=40)
        self.table.column("form", width=90)


        self.table.heading("Club", text=" Liga")
        self.table.heading("Valeurs", text="Valeur Marchande (en Millions €)")
        self.table.heading("position", text="Position")
        self.table.heading("points", text="Points")
        self.table.heading("playedGames", text="MJ")
        self.table.heading("won", text="G")
        self.table.heading("draw", text="N")
        self.table.heading("lost", text="L")
        self.table.heading("goalsFor", text="BP")
        self.table.heading("goalsAgainst", text="BC")
        self.table.heading("goalDifference", text="BD")
        self.table.heading("form", text="DB")
        self.table.configure(height=20)
        self.table.grid(row=2, column=5, sticky="W")

        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["BDD_FOOT"]
        collection = db["LigaValeur"]

        data = db.LigaValeur.find()
        for e in data:
            self.table.insert("", "end", values=(e["Club"], e["Valeurs"],e["position"],e["points"],e["playedGames"],e["won"],e["draw"],e["lost"],e["goalsFor"],e["goalsAgainst"],e["goalDifference"],e["form"]))


class SerieaValeur(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ttk.Button(self, text="Série A",
                   command=lambda: master.switch_frame(Seriea)).grid(row=2, column=0, sticky="W")

        self.table = ttk.Treeview(self)
        self.table["columns"] = ("Club", "Valeurs","position","points","playedGames","won","draw","lost","goalsFor","goalsAgainst","goalDifference","form")
        self.table.column("Club", width=200)
        self.table.column("Valeurs", width=200)
        self.table.column("position", width=70)
        self.table.column("points", width=70)
        self.table.column("playedGames", width=40)
        self.table.column("won", width=40)
        self.table.column("draw", width=40)
        self.table.column("lost", width=40)
        self.table.column("goalsFor", width=40)
        self.table.column("goalsAgainst", width=40)
        self.table.column("goalDifference", width=40)
        self.table.column("form", width=90)


        self.table.heading("Club", text=" Serie A")
        self.table.heading("Valeurs", text="Valeur Marchande (en Millions €)")
        self.table.heading("position", text="Position")
        self.table.heading("points", text="Points")
        self.table.heading("playedGames", text="MJ")
        self.table.heading("won", text="G")
        self.table.heading("draw", text="N")
        self.table.heading("lost", text="L")
        self.table.heading("goalsFor", text="BP")
        self.table.heading("goalsAgainst", text="BC")
        self.table.heading("goalDifference", text="BD")
        self.table.heading("form", text="DB")
        self.table.configure(height=20)
        self.table.grid(row=2, column=5, sticky="W")

        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["BDD_FOOT"]
        collection = db["SerieaValeur"]

        data = db.SerieaValeur.find()
        for e in data:
            self.table.insert("", "end", values=(e["Club"], e["Valeurs"],e["position"],e["points"],e["playedGames"],e["won"],e["draw"],e["lost"],e["goalsFor"],e["goalsAgainst"],e["goalDifference"],e["form"]))


class Ligue1Valeur(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ttk.Button(self, text="Ligue 1",
                   command=lambda: master.switch_frame(Ligue1)).grid(row=2, column=0, sticky="W")

        self.table = ttk.Treeview(self)
        self.table["columns"] = ("Club", "Valeurs","position","points","playedGames","won","draw","lost","goalsFor","goalsAgainst","goalDifference","form")
        self.table.column("Club", width=200)
        self.table.column("Valeurs", width=200)
        self.table.column("position", width=70)
        self.table.column("points", width=70)
        self.table.column("playedGames", width=40)
        self.table.column("won", width=40)
        self.table.column("draw", width=40)
        self.table.column("lost", width=40)
        self.table.column("goalsFor", width=40)
        self.table.column("goalsAgainst", width=40)
        self.table.column("goalDifference", width=40)
        self.table.column("form", width=90)


        self.table.heading("Club", text=" Ligue 1")
        self.table.heading("Valeurs", text="Valeur Marchande (en Millions €)")
        self.table.heading("position", text="Position")
        self.table.heading("points", text="Points")
        self.table.heading("playedGames", text="MJ")
        self.table.heading("won", text="G")
        self.table.heading("draw", text="N")
        self.table.heading("lost", text="L")
        self.table.heading("goalsFor", text="BP")
        self.table.heading("goalsAgainst", text="BC")
        self.table.heading("goalDifference", text="BD")
        self.table.heading("form", text="DB")
        self.table.configure(height=20)
        self.table.grid(row=2, column=5, sticky="W")

        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["BDD_FOOT"]
        collection = db["Ligue1Valeur"]

        data = db.Ligue1Valeur.find()
        for e in data:
            self.table.insert("", "end", values=(e["Club"], e["Valeurs"],e["position"],e["points"],e["playedGames"],e["won"],e["draw"],e["lost"],e["goalsFor"],e["goalsAgainst"],e["goalDifference"],e["form"]))


class BundesligaValeur(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ttk.Button(self, text="Bundesliga",
                   command=lambda: master.switch_frame(Bundesliga)).grid(row=2, column=0, sticky="W")

        self.table = ttk.Treeview(self)
        self.table["columns"] = ("Club", "Valeurs","position","points","playedGames","won","draw","lost","goalsFor","goalsAgainst","goalDifference","form")
        self.table.column("Club", width=200)
        self.table.column("Valeurs", width=200)
        self.table.column("position", width=70)
        self.table.column("points", width=70)
        self.table.column("playedGames", width=40)
        self.table.column("won", width=40)
        self.table.column("draw", width=40)
        self.table.column("lost", width=40)
        self.table.column("goalsFor", width=40)
        self.table.column("goalsAgainst", width=40)
        self.table.column("goalDifference", width=40)
        self.table.column("form", width=90)


        self.table.heading("Club", text="Bundesliga")
        self.table.heading("Valeurs", text="Valeur Marchande (en Millions €)")
        self.table.heading("position", text="Position")
        self.table.heading("points", text="Points")
        self.table.heading("playedGames", text="MJ")
        self.table.heading("won", text="G")
        self.table.heading("draw", text="N")
        self.table.heading("lost", text="L")
        self.table.heading("goalsFor", text="BP")
        self.table.heading("goalsAgainst", text="BC")
        self.table.heading("goalDifference", text="BD")
        self.table.heading("form", text="DB")
        self.table.configure(height=20)
        self.table.grid(row=2, column=5, sticky="W")

        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["BDD_FOOT"]
        collection = db["BundesligaValeur"]

        data = db.BundesligaValeur.find()
        for e in data:
            self.table.insert("", "end", values=(e["Club"], e["Valeurs"],e["position"],e["points"],e["playedGames"],e["won"],e["draw"],e["lost"],e["goalsFor"],e["goalsAgainst"],e["goalDifference"],e["form"]))



class LiganosValeur(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ttk.Button(self, text="Liga Nos",
                   command=lambda: master.switch_frame(Liganos)).grid(row=2, column=0, sticky="W")

        self.table = ttk.Treeview(self)
        self.table["columns"] = ("Club", "Valeurs","position","points","playedGames","won","draw","lost","goalsFor","goalsAgainst","goalDifference","form")
        self.table.column("Club", width=200)
        self.table.column("Valeurs", width=200)
        self.table.column("position", width=70)
        self.table.column("points", width=70)
        self.table.column("playedGames", width=40)
        self.table.column("won", width=40)
        self.table.column("draw", width=40)
        self.table.column("lost", width=40)
        self.table.column("goalsFor", width=40)
        self.table.column("goalsAgainst", width=40)
        self.table.column("goalDifference", width=40)
        self.table.column("form", width=90)


        self.table.heading("Club", text=" Liga Nos")
        self.table.heading("Valeurs", text="Valeur Marchande (en Millions €)")
        self.table.heading("position", text="Position")
        self.table.heading("points", text="Points")
        self.table.heading("playedGames", text="MJ")
        self.table.heading("won", text="G")
        self.table.heading("draw", text="N")
        self.table.heading("lost", text="L")
        self.table.heading("goalsFor", text="BP")
        self.table.heading("goalsAgainst", text="BC")
        self.table.heading("goalDifference", text="BD")
        self.table.heading("form", text="DB")
        self.table.configure(height=20)
        self.table.grid(row=2, column=5, sticky="W")

        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["BDD_FOOT"]
        collection = db["LiganosValeur"]

        data = db.LiganosValeur.find()
        for e in data:
            self.table.insert("", "end", values=(e["Club"], e["Valeurs"],e["position"],e["points"],e["playedGames"],e["won"],e["draw"],e["lost"],e["goalsFor"],e["goalsAgainst"],e["goalDifference"],e["form"]))


if __name__ == "__main__":
    app = Example()
    app.mainloop()
