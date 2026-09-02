import pandas as pd
import scanpy as sc
import cnsplots as cns
 
# Load data from CSV: genes are rows, samples are columns
df = pd.read_csv("heatmap_data.csv").set_index("gene")
print(df.head())
 
# Transpose so samples become observations (rows) and genes become
# variables (columns), which is what AnnData / heatmapplot expects.
adata = sc.AnnData(df.T)
 
# Add a sample-group annotation derived from the sample names
adata.obs["group"] = [
    "Treatment" if s.startswith("Treatment") else "Control"
    for s in adata.obs_names
]
 
# Bigger canvas gives cnsplots room to lay out the dendrograms, row
# annotation bar, gene labels, and legend without overlapping/truncating.
cns.figure(400, 280)
cmp = cns.heatmapplot(
    adata,
    label="Expression",
    xlabel="Genes",
    ylabel="Samples",
    row_annotation=["group"],
    row_cluster=True,
    col_cluster=True,
    row_dendrogram=True,
    col_dendrogram=True,
    show_rownames=True,
    show_colnames=True,
    xticklabels_fontsize=7,
    yticklabels_fontsize=8,
    cmap="BuRd_custom",       # sequential colormap - better for all-positive data
                          # other good options: "gnuplot", "viridis", "magma"
    legend_hpad=6,        # push legend further right, away from the plot
    legend_vpad=10,        # push legend down, away from the column dendrogram
    legend_width=28,      # wider legend box so "Treatment" isn't truncated
)
 
cns.savefig("13_heatmap.jpg")
print("Saved 13_heatmap.jpg")
 