import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df_AVONET_IUCN = pd.read_csv("./data/AVONET_IUCN.csv") #Reads in the AVONET_IUCN spreadsheet
df = df_AVONET_IUCN.select_dtypes(include=[np.number]).dropna() #Selects the columns with only numbers and removes the rows with missing values
IUCN_categories = df_AVONET_IUCN.loc[df.index, "RL Category"]
scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)

pca = PCA(n_components=2)
pca.fit(scaled_data)
x_pca = pca.transform(scaled_data)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=x_pca[:, 0], y=x_pca[:, 1], hue=IUCN_categories, palette="viridis")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.ylim(-5, 25)
plt.xlim(-5, 27)
plt.title("AVONET PCA")
plt.savefig("./output/AVONET_PCA.png", dpi=300, bbox_inches="tight")
plt.show()

