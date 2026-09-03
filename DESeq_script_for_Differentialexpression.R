#Step 1 — Set up your RStudio working directory
#Create a folder for the DESeq2 analysis and place these two files inside it:
  
#RNAseq_DESeq2/
  ├── countdata.csv
  └── metadata.csv

#1.1: Set your working directory
  
  setwd("path/to/your/RNAseq_DESeq2")

#1.2: Check the working directory
getwd()

#1.3 List files in the directory
list.files()

#You should see:
"countdata.csv"
"metadata.csv"

#Step 2 — Import and check your input data
#2.1 Read the count matrix

countData <- read.csv(
  "countdata.csv",
  header = TRUE,
  row.names = 1,
  check.names = FALSE
)

head(countData)
dim(countData)

#2.2 Read the sample metadata
metaData <- read.csv(
  "metadata.csv",
  header = TRUE,
  row.names = 1,
  check.names = FALSE
)

metaData

#2.3 Check that sample names match
#This is very important before running DESeq2.

colnames(countData)
rownames(metaData)

#They should contain the same sample names and in the same order.
#Then check:
  
all(colnames(countData) == rownames(metaData))

#Step 3 — Load DESeq2
library(DESeq2)
library(ggplot2)

#If DESeq2 is not installed, install it through Bioconductor:
  
  if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("DESeq2")

#Step 4 — Create the DESeq2 dataset
dds <- DESeqDataSetFromMatrix(
  countData = countData,
  colData = metaData,
  design = ~ dex
)
#Set the control condition as the reference:
  
  dds$dex <- relevel(dds$dex, ref = "control")

#Check:
  
  dds
  
  
#Step 5 — Run DESeq2
  dds <- DESeq(dds)
  
#Now DESeq2 has performed:
    
   
#Step 6 — Obtain normalized counts
 
normalized_counts <- counts(dds, normalized = TRUE)
  
head(normalized_counts)
  
write.csv(
    normalized_counts,
    file = "Normalizedcounts.csv"
    
  )
#Step 7 — VST transformation for clustering
  
#For PCA and sample clustering, use variance-stabilized data:
    
vsdata <- vst(dds, blind = FALSE)
  
vst_counts <- assay(vsdata)
  
head(vst_counts)
  
write.csv(
    vst_counts,
    file = "VST_counts.csv"
  )  

#Step 8 — PCA plot
pcaData <- plotPCA(
  vsdata,
  intgroup = c("id", "dex"),
  returnData = TRUE
)

percentVar <- round(
  100 * attr(pcaData, "percentVar")
)

ggplot(
  pcaData,
  aes(PC1, PC2, color = id, shape = dex)
) +
  geom_point(size = 3) +
  scale_shape_manual(
    values = c(7, 8, 9, 10, 15, 16, 17, 18)
  ) +
  xlab(paste0("PC1: ", percentVar[1], "% variance")) +
  ylab(paste0("PC2: ", percentVar[2], "% variance")) +
  coord_fixed()

#Step 9 — Sample-to-sample distance heatmap

install.packages("pheatmap")   # only if not already installed

library(pheatmap)
library(RColorBrewer)

sampleDists <- dist(t(assay(vsdata)))

sampleDistMatrix <- as.matrix(sampleDists)

rownames(sampleDistMatrix) <- colnames(vsdata)
colnames(sampleDistMatrix) <- colnames(vsdata)

pheatmap(
  sampleDistMatrix,
  clustering_distance_rows = sampleDists,
  clustering_distance_cols = sampleDists,
  col = colorRampPalette(
    rev(brewer.pal(9, "Blues"))
  )(255),
  main = "Sample-to-Sample Distance Heatmap"
)

#Step 10 — Differential expression comparison
  
  res_1 <- results(
    dds,
    contrast = c("dex", "treated", "control"),
    alpha = 0.05
  )

levels(dds$dex)
summary(res_1)

#Save the results:
  
write.csv(
    as.data.frame(res_1),
    file = "DESeq2_results.csv"
  )

#Step 11 — Sort significant results
res_1 <- res_1[order(res_1$padj), ]
head(res_1)

#Save:
  
write.csv(
    as.data.frame(res_1),
    file = "DESeq2_results_sorted.csv"
  )

#Step 12 — MA plot
plotMA(
  res_1,
  main = "Differential Expression",
  ylim = c(-5, 5)
)

#Step 13 — Volcano plot

with(
  res_1,
  plot(
    log2FoldChange,
    -log10(pvalue),
    pch = 20,
    main = "Differential Expression",
    xlab = "log2 Fold Change",
    ylab = "-log10(p-value)"
  )
)

with(
  subset(res_1, padj < 0.05),
  points(
    log2FoldChange,
    -log10(pvalue),
    pch = 20,
    col = "blue"
  )
)

with(
  subset(res_1, padj < 0.05 & abs(log2FoldChange) > 1.5),
  points(
    log2FoldChange,
    -log10(pvalue),
    pch = 20,
    col = "red"
  )
)