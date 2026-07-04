import pandas as pd
from pandas.core.nanops import F

#AVOTREX analysis
df = pd.read_csv("data/AVOTREX.csv")

#Kipps Distance
kipps_distance = df["kipps_distance"]
with open("Kipps_distance_comparison.txt", "a") as file:
    file.write("Average Kipp's Distance of Extinct Birds: " + str(kipps_distance.mean()) + " mm" + "\n")

#Mass
mass = df["body_mass"]
with open("Mass_comparison.txt", "a") as file:
    file.write("Average Mass of Extinct Birds: " + str(mass.mean()) + " g" + "\n")

#Hand-Wing Index
culmen_length = df["beak_length_culmen"]
with open("Culmen_length_comparison.txt", "a") as file:
    file.write("Average Culmen Length of Extinct Birds: " + str(culmen_length.mean()) + " mm" + "\n")
