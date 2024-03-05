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

assert dataframe.loc["United States"]["count"] == 579
assert dataframe.loc["China"]["count"] == 273
assert dataframe.loc["India"]["count"] == 174
assert dataframe.loc["United Kingdom"]["count"] == 173
assert dataframe.loc["Italy"]["count"] == 112

#
#
if not os.path.exists("co_occurrences.csv"):
    raise FileNotFoundError("File 'co_occurrences.csv' not found")


if not os.path.exists("network.png"):
    raise FileNotFoundError("File 'network.pmg' not found")
