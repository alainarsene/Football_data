# Football_Stats

![bigDataimage]([file:///C:/Users/Lucas/PycharmProjects/API-FOOT/logo.jpg](https://www.google.com/search?q=image+foot&&tbm=isch&ved=2ahUKEwiWn_TYkeb8AhVoTaQEHUsbD_gQ2-cCegQIABAA&oq=image+foot&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEOoCECc6BAgjECc6CAgAEIAEELEDOgQIABBDOgcIABCxAxBDUN4LWMc8YPpCaAFwAHgAgAFgiAGbB5IBAjExmAEAoAEBqgELZ3dzLXdpei1pbWewAQrAAQE&sclient=img&ei=DevSY9bkF-iakdUPy7a8wA8&bih=722&biw=1536#imgrc=B0TaIWXbts0PcM)


# Description 

Le Football est un sport collectif très populaire notament suite a une coupe du monde.
Notre Projet consiste a metre en relation la statistique de la valeur des Clubs et des championnat sur des performances sportives.


# Technologie

- Pycharm : Python
- Jupyter : Python
- Mongodb Compass

# Installation
Tout d'abord il faut télécharger:

-Mongodb Compass pour obtenir une base de donnée en local
-Un éditeur python capable de créer des interfaces (Pycharm)

Il est important d'importer les bibliothèque suivante pour pouvoir utiliser L'API, l'interface python et la base de données Mongodb Compass:

- import tkinter as tk
  from tkinter import ttk
  from tkinter import *
-import pymongo
-import requests
-import json
-import csv
-from pymongo import MongoClient

# Procédure

Tout d'abord quand vous aurait télécharger notre projet sur github :
- Vous aller éxecuter sur l'editeur python les fichiers api.py et csv.py une seule fois (cela va créer une base donnée sur Mongodb Compass avec toute les collections nécessaires).   
- Vous pouvez ensuite éxecuter le fichier page.py qui ouvrira l'interface.
- Dans l'interface vous pouvez sélectionner les différents championnats , la valeurs des clubs des championnats et leurs suppressions avec les differents bouttons
- Avec le fichier updatepremierleague.py vous pouvez modifier les clubs dans le championnat de la Premier League en indiquant le nom (shortName sur MongodbCompass) du Club

# Visualisation

La visualisation des données se fait avec jupyter notebook et l'éditeur python(Pycharm)

# Auteur

Lucas Constant
Alain Fosso
Jovick Fotsing




