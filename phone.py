import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'serif'   # stylish font
plt.rcParams['font.size'] = 11
data = {
"Phone":["A","B","C","D","E","F","G","H"],
"Brand":["Samsung","Apple","Samsung","OnePlus","Apple","OnePlus","Samsung","Apple"],
"Sales":[500,650,700,450,600,480,720,680],
"Price":[20000,70000,25000,40000,65000,38000,27000,72000],
"Rating":[4.2,4.6,4.3,4.4,4.5,4.1,4.3,4.7]
}
df = pd.DataFrame(data)
plt.figure(figsize=(15,10))
plt.subplot(2,3,1)
plt.scatter(df["Price"],df["Sales"],color="red")
plt.title("Price vs Sales",fontweight="bold")
plt.subplot(2,3,2)
plt.barh(df["Phone"],df["Sales"],color="blue")
plt.title("Phone Sales",fontweight="bold")
plt.subplot(2,3,3)
plt.stem(df["Sales"],linefmt="green",markerfmt="go")
plt.title("Sales Stem Plot",fontweight="bold")
plt.subplot(2,3,4)
x = np.arange(len(df))
plt.stackplot(x,df["Sales"],df["Rating"],colors=["orange","purple"])
plt.title("Sales & Rating Stack",fontweight="bold")
plt.subplot(2,3,5)
plt.violinplot(df["Sales"])
plt.title("Sales Violin Plot",fontweight="bold")
plt.subplot(2,3,6)
plt.hexbin(df["Price"],df["Sales"],gridsize=10,cmap="viridis")
plt.title("Sales Density Hexbin",fontweight="bold")
plt.suptitle(
"Smartphone Sales Analysis Dashboard",
fontsize=20,
fontweight="bold",
y=1.03
)
plt.subplots_adjust(
top=0.88,
hspace=0.45,
wspace=0.30
)
plt.show()