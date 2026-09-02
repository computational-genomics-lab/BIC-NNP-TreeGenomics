
import numpy as np
import pandas as pd
import cnsplots as cns
 
df = pd.read_csv("volcano_data.csv")
 
df["-log10(adjp)"] = -np.log10(df["padj"].clip(lower=1e-300))
print(df.head())
 
# Genes to label on the plot (e.g. known markers of interest)
genes_of_interest = ["TP53", "MYC", "BRCA1", "EGFR", "VEGFA", "CDKN2A"]
 
cns.figure(200, 200)
ax = cns.volcanoplot(
    df,
    x="log2FoldChange",
    y="-log10(adjp)",
    symbol="gene",
    show_list=genes_of_interest,
)
ax.set_title("Differential Expression: Treatment vs Control")
 
cns.savefig("12_volcano_plot.jpg")
print("Saved 12_volcano_plot.jpg")
 