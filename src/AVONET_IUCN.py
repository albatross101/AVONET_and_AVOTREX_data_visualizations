import pandas as pd

#1130 out of 11009 species missing IUCN rating

df_AVONET = pd.read_csv("./data/AVONET.csv")

df_AviList = pd.read_excel("./data/AviList.xlsx") #Reads in the AviList spreadsheet
species = df_AviList[df_AviList["Taxon_rank"] == "species"] #Makes a dataframe only of the items in the Taxon_rank column that are species
species_and_IUCN = species[["Scientific_name", "IUCN_Red_List_Category"]] #Makes a new dataframe with the scientific name and the IUCN Red List Category
df_AVONET_IUCN = pd.merge(df_AVONET, species_and_IUCN, left_on="Species1", right_on="Scientific_name", how="left") #Merges the AVONET dataframe with the species_and_IUCN dataframe on the Species1 column and the Scientific_name column
df_AVONET_IUCN.to_csv("./data/AVONET_IUCN.csv", index=False) #Saves the dataframe to a csv file

missing_species = df_AVONET_IUCN[df_AVONET_IUCN["IUCN_Red_List_Category"].isna()]["Species1"]
with open("./output/missing_species.txt", "w") as file:
    file.write("Species missing IUCN rating: " + "\n" + missing_species.head(1130).to_string() + "\n")

#Test to see how many species are missing IUCN rating
# missing = df_AVONET_IUCN["IUCN_Red_List_Category"].isna().sum()
# total = len(df_AVONET_IUCN)
# print(f"{missing} out of {total} species missing IUCN rating")