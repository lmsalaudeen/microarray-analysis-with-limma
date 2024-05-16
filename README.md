---
---
---

# Differential Gene Expression

This repository contains a workflow for analysing microarray and RNA-Seq data from the GEO database. It contains Rmd files for mircoarray analysis with Limma and RNA-Seq analysis with DESeq2; and a python script for dealing with metadata.

A brief introduction to gene expression analysis is presented below.

# Introduction

The goal of gene expression investigations is to study the amount of mRNA that is transcribed in a biological system. There are several techniques are available for measuring gene expression, with microarray and RNA-Seq analysis being two of the most popular.

A gene expression array (microarray) quantifies RNA transcripts using the principle of nucleic acid hybridization (or matching) of fluorescently labelled complementary DNA (cDNA) strands attached to the surface of the array (Tonya et al., 2022). RNA-Seq on the other hand quantifies the levels of various types of RNA in a sample by sequencing the RNA directly and counting the number of sequences (Singh et al., 2018). RNA-Seq is advantageous over microarray in that it has the capability to quantify a greater range of transcripts.

The outcome of gene expression analysis is usually represented by a long list of genes termed differentially expressed genes. The goal is to discover the molecular mechanisms that underlie certain phenotypes, and as such, expression changes of individual genes are analysed for enrichment in functional gene sets (Geistlinger et al., 2021).

These sets may represent biological processes, molecular functions and cellular components as defined by the Gene Ontology (GO) database (The Gene Ontology Consortium et al., 2023), pathway databases such as KEGG (Kanehisa et al., 2014) and Reactome (Gillespie et al., 2022) or experimentally derived gene sets such as available in the MSigDB (Liberzon et al., 2015).

# Selection of Differentially Expressed Genes

The Linear Models for Microarray Data (limma) package in R (Ritchie et al., 2015), and the DESeq2 package in R (Love, Huber and Anders, 2014) are two popular methods used to analyse microarray and RNA-Seq data. The outcome of these are usually a list of upregulated and downregulated genes.

The selection of differentially expressed genes falls under interpretation of two values: the fold change and false discovery rate. The fold change (FC) shows the change of expression levels of a gene between two groups (e.g. case and control). It is calculated as a ratio of the expression level and scaled to logarithm base (Zhao, Erwin and Xue, 2018). A positive FC implies an increase in expression while a negative FC implies a decrease.\
The false discovery rate (FDR) is the expected proportion of false positives among all positives which rejected the null hypothesis (Jafari and Ansari-Pour, 2018).

In studies where there are multiple tests (e.g. multiple genes with their own calculated raw p values), there is a tendency for the p values to become inflated, hence it is necessary to make some form of adjustments to the p values to control the error rate (Jafari and Ansari-Pour, 2018). One popular method is the use of the Benjamini and Hochberg method to control the false discovery rate. This method re-calculates p value by ranking the raw p values in an ascending order and multiplying by m/k, where m is the number of independent tests and k is the position of the p value in the sorted list (Benjamini and Hochberg, 1995).

# Limma

A workflow for microarray analysis with Limma

# DESeq2

A workflow for RNA-Seq Analysis with DESeq2

## References

-   Benjamini, Y. and Hochberg, Y. (1995) 'Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing', Journal of the Royal Statistical Society: Series B (Methodological), 57(1), pp. 289--300. Available at: <https://doi.org/10.1111/j.2517-6161.1995.tb02031.x>.

-   Geistlinger, L. et al. (2021) 'Toward a gold standard for benchmarking gene set enrichment analysis', Briefings in Bioinformatics, 22(1), pp. 545--556. Available at: <https://doi.org/10.1093/bib/bbz158>.

-   Gillespie, M. et al. (2022) 'The reactome pathway knowledgebase 2022', Nucleic Acids Research, 50(D1), pp. D687--D692. Available at: <https://doi.org/10.1093/nar/gkab1028>. Jafari, M. and Ansari-Pour, N. (2018) 'Why, When and How to Adjust Your P Values?', Cell Journal (Yakhteh), 20(4). Available at: <https://doi.org/10.22074/cellj.2019.5992>.

-   Kanehisa, M. et al. (2014) 'Data, information, knowledge and principle: back to metabolism in KEGG', Nucleic Acids Research, 42(Database issue), pp. D199-205. Available at: <https://doi.org/10.1093/nar/gkt1076>.

-   Liberzon, A. et al. (2015) 'The Molecular Signatures Database (MSigDB) hallmark gene set collection', Cell systems, 1(6), pp. 417--425. Available at: <https://doi.org/10.1016/j.cels.2015.12.004>.

-   Love, M.I., Huber, W. and Anders, S. (2014) 'Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2', Genome Biology, 15(12), p. 550. Available at: <https://doi.org/10.1186/s13059-014-0550-8>.

-   Ritchie, M.E. et al. (2015) 'limma powers differential expression analyses for RNA-sequencing and microarray studies', Nucleic Acids Research, 43(7), p. e47. Available at: <https://doi.org/10.1093/nar/gkv007>.

-   Singh, K.P. et al. (2018) 'Mechanisms and Measurement of Changes in Gene Expression', Biological Research For Nursing, 20(4), pp. 369--382. Available at: <https://doi.org/10.1177/1099800418772161>.

-   The Gene Ontology Consortium et al. (2023) 'The Gene Ontology knowledgebase in 2023', Genetics, 224(1), p. iyad031. Available at: <https://doi.org/10.1093/genetics/iyad031>.

-   Tonyan, Z.N. et al. (2022) 'Overview of Transcriptomic Research on Type 2 Diabetes: Challenges and Perspectives', Genes, 13(7), p. 1176. Available at: <https://doi.org/10.3390/genes13071176>.

-   Zhao, B., Erwin, A. and Xue, B. (2018) 'How many differentially expressed genes: A perspective from the comparison of genotypic and phenotypic distances', Genomics, 110(1), pp. 67--73. Available at: <https://doi.org/10.1016/j.ygeno.2017.08.007>.
