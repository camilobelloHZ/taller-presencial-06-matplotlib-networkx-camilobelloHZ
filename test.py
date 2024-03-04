"""GitHub Classroom autograding script."""

import os

import pandas as pd

from country_collaboration import main

main(20)

#
# Retorna error si la carpeta output/ no existe
if not os.path.exists("countries.csv"):
    raise FileNotFoundError("File 'countries.csv' not found")

#
# Lee el contenido del archivo output.txt
dataframe = pd.read_csv("countries.csv")
dataframe = dataframe.set_index("countries")

print(dataframe)

assert dataframe["United States of America"] == 579
assert dataframe["China"] == 273
assert dataframe["India"] == 174
assert dataframe["United Kingdom"] == 173
assert dataframe["Italy"] == 112

#
#
if not os.path.exists("co_occurrences.csv"):
    raise FileNotFoundError("File 'co_occurrences.csv' not found")


if not os.path.exists("network.png"):
    raise FileNotFoundError("File 'network.pmg' not found")
