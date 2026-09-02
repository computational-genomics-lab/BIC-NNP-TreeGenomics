import cnsplots as cns
from cnsplots.datasets import get_showcase_data

# Get CNSplots example datasets
data = get_showcase_data()

# Select the volcano-plot dataset
volcano_df = data[4]

# Check the data
print(volcano_df.head())
print(volcano_df.columns)

# Create figure
cns.figure(200, 200)

# Create volcano plot
ax = cns.volcanoplot(
    volcano_df,
    x="log2FoldChange",
    y="-log10(adjp)",
    symbol="symbol",
    n_show=8,
)

# Save the plot
cns.savefig("volcano.png")

print("Volcano plot saved as volcano.png")