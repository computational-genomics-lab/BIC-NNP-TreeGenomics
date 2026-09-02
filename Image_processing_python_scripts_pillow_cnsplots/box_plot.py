import pandas as pd
import cnsplots as cns
 
# Load data from CSV
df = pd.read_csv("iris_data_scatter.csv")
print(df.head())
 
species_order = ["setosa", "versicolor", "virginica"]
 
# Boxplot of petal length by species, with pairwise significance tests
cns.figure(160, 140)
ax = cns.boxplot(
    data=df,
    x="species",
    y="petal_length",
    order=species_order,
    pairs=[
        ("setosa", "versicolor"),
        ("versicolor", "virginica"),
        ("setosa", "virginica"),
    ],
)
ax.set_title("Petal Length by Species")
ax.set_xlabel("Species")
ax.set_ylabel("Petal Length (cm)")
 
cns.savefig("16_box_plot.jpg")
print("Saved 16_box_plot.jpg")

from scipy.stats import mannwhitneyu

pairs = [
    ("setosa", "versicolor"),
    ("versicolor", "virginica"),
    ("setosa", "virginica"),
]

print("OUTPUT")
n_counts = " / ".join(
    f"{len(df[df.species == sp])}" for sp in species_order
)
print(f"n = {n_counts}")

for a, b in pairs:
    group_a = df[df.species == a]["petal_length"]
    group_b = df[df.species == b]["petal_length"]
    stat, p = mannwhitneyu(group_a, group_b, alternative="two-sided")
    stars = "****" if p < 0.0001 else "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
    print(f"{a} vs {b}: Mann-Whitney p = {p:.2e} ({stars})")