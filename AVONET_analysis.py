import pandas as pd
from pandas.core.nanops import F

#AVONET analysis
df = pd.read_csv("data/AVONET.csv")

#Kipps Distance
kipps_distance = df["Kipps.Distance"]
with open("Kipps_distance_comparison.txt", "a") as file:
    file.write("Average Kipp's Distance of Living Birds: " + str(kipps_distance.mean()) + " mm" + "\n")

#Mass
mass = df["Mass"]
with open("Mass_comparison.txt", "a") as file:
    file.write("Average Mass of Living Birds: " + str(mass.mean()) + " g" + "\n")

#Culmen Length
culmen = df["Beak.Length_Culmen"]
with open("Culmen_length_comparison.txt", "a") as file:
    file.write("Average Culmen Length of Living Birds: " + str(culmen.mean()) + " mm" + "\n")








