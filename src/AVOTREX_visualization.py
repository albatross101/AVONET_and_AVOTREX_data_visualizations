import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/AVOTREX.csv")

#Order counts and proportions
order_counts = df["order"].value_counts()
order_proportions_AVOTREX = df["order"].value_counts(normalize=True)
plt.bar(order_proportions_AVOTREX.index, order_proportions_AVOTREX.values)
plt.xlabel("Order")
plt.ylabel("Proportion")
plt.title("Order Proportions of Extinct Birds")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("output/AVOTREX_Order_Proportions.png", dpi=300, bbox_inches="tight")
plt.show()

#Flight ability counts
flight_ability_counts = df["flight_ability"].value_counts()
plt.bar(flight_ability_counts.index.astype(str), flight_ability_counts.values, width=0.4, label=("0 = Flightless, 0.5 = Weak flyer, 1 = Flighted"))
plt.xlabel("Flight Ability")
plt.ylabel("Number of Species")
plt.title("Flight Ability of Extinct Birds")
plt.tight_layout()
plt.legend()
plt.savefig("output/AVOTREX_Flight_Ability_Counts.png", dpi=300, bbox_inches="tight")
plt.show()

#Endemicity
endemicity_counts = df["island_endemicity"].value_counts()
plt.bar(endemicity_counts.index, endemicity_counts.values)
plt.xlabel("Endemicity")
plt.ylabel("Number of Species")
plt.title("Endemicity of Extinct Birds")
plt.tight_layout()
plt.savefig("output/AVOTREX_Endemicity_Counts.png", dpi=300, bbox_inches="tight")
plt.show()