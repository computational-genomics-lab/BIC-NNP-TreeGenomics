import pandas as pd
import cnsplots as cns
 
# Load data from CSV (not from cnsplots' built-in datasets)
df = pd.read_csv("iris_data_scatter.csv")
print(df.head())
 
# Basic scatter plot: petal length vs petal width, colored by species
cns.figure(140, 120)
ax = cns.scatterplot(
    data=df,
    x="petal_length",
    y="petal_width",
    s=12,
    hue="species",
)
ax.set_title("Petal Length vs Petal Width")
ax.set_xlabel("Petal Length (cm)")
ax.set_ylabel("Petal Width (cm)")
cns.take_legend_out()
 
cns.savefig("11_scatter_plot.jpg")
print("Saved 11_scatter_plot.jpg")