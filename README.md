# Football_Stats



# Description 

Le Football est un sport collectif très populaire notamment suite a une coupe du monde.
Notre Projet consiste a mettre en relation la statistique de la valeur des Clubs et des championnats sur des performances sportives.


# Technologie

- Pycharm : Python
- Jupyter : Python
- Mongodb Compass

# Installation
Tout d'abord il faut télécharger:

-Mongodb Compass pour obtenir une base de donnée en local
-Un éditeur python capable de créer des interfaces: Pycharm

Il est important d'importer les bibliothèques suivantes pour pouvoir utiliser L'API, l'interface python et la base de données Mongodb Compass:

- import tkinter as tk
  from tkinter import ttk
  from tkinter import *
-import pymongo
-import requests
-import json
-import csv
-from pymongo import MongoClient

# Procédure

Tout d'abord quand vous aurez téléchargé notre projet sur github :
- Vous allez éxecuter sur l'editeur python les fichiers api.py et csv.py une seule fois (cela va créer une base de données sur Mongodb Compass avec toutes les collections nécessaires).   
- Vous pouvez ensuite éxecuter le fichier page.py qui ouvrira l'interface.
- Dans l'interface vous pouvez sélectionner les différents championnats , la valeurs des clubs des championnats et leur suppression avec les differents bouttons
- Avec le fichier updatepremierleague.py vous pouvez modifier les clubs dans le championnat de la Premier League en indiquant le nom (shortName sur MongodbCompass) du Club.

# Visualisation

La visualisation des données se fait avec jupyter notebook et l'éditeur python(Pycharm)

# Auteur

Lucas Constant
Alain Fosso
Jovick Fotsing




