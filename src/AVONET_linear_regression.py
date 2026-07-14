import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from scipy import stats
import matplotlib.pyplot as plt

df_AVONET_IUCN = pd.read_csv("./data/AVONET_IUCN.csv")
x = np.array(df_AVONET_IUCN["Tarsus.Length"]).reshape(-1, 1)
y = np.array(df_AVONET_IUCN["Wing.Length"])
x_flat = x.flatten()
result = stats.linregress(x_flat, y)
model = LinearRegression().fit(x, y)
r_squared = model.score(x, y)
print(f"Coefficient of determination: {r_squared}")
print(f"Intercept: {model.intercept_}") 
print(f"Slope: {model.coef_}")
y_pred = model.predict(x)
print(f"Predicted values: {y_pred[:5]}")
print(f"P-value: {result.pvalue:.2e}")

#Plot the data points and regression line
plt.scatter(x, y)
plt.plot(x, y_pred, color="red")
plt.xlabel("Tarsus Length (mm)")
plt.ylabel("Wing Length (mm)")
plt.ylim(0, 1000)
plt.title("Linear Regression of Tarsus Length vs. Wing Length")
plt.savefig("./output/AVONET_Tarsus_Length_vs_Wing_Length_Linear_Regression.png", dpi=300, bbox_inches="tight")
plt.show()