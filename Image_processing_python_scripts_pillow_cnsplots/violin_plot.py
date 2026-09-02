import pandas as pd
import cnsplots as cns
 
# Load data from CSV
df = pd.read_csv("iris_data_scatter.csv")
print(df.head())
 
species_order = ["setosa", "versicolor", "virginica"]
 
# Violin plot of petal length by species
cns.figure(160, 140, color_cycle="Ecotyper1")
ax = cns.violinplot(
    data=df,
    x="species",
    y="petal_length",
    order=species_order,
)
ax.set_title("Petal Length Distribution by Species")
ax.set_xlabel("Species")
ax.set_ylabel("Petal Length (cm)")
 
cns.savefig("17_violin_plot.jpg")
print("Saved 17_violin_plot.jpg")
 
# Bonus: split each species by a second measurement using hue
# (here we bucket sepal_width into High/Low around the median for demo)
df["sepal_width_group"] = df["sepal_width"].apply(
    lambda w: "High" if w >= df["sepal_width"].median() else "Low"
)
 
cns.figure(200, 150, color_cycle="Ecotyper1")
ax2 = cns.violinplot(
    data=df,
    x="species",
    y="petal_length",
    order=species_order,
    hue="sepal_width_group",
)
ax2.set_title("Petal Length by Species and Sepal Width Group")
cns.take_legend_out()
 
cns.savefig("17b_violin_plot_by_hue.jpg")
print("Saved 17b_violin_plot_by_hue.jpg")
 