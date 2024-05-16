#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 02:30:54 2023

@author: lmsalaudeen
@description: python script to extract metadata (ID and status) from series matrix
"""


filepath = "Data/GSE20966/GSE20966_series_matrix.txt"
outputPath = "Data/GSE20966/GSE20966_metadata.txt"

with open(filepath, "r") as file:
    for row in file:
        if row.startswith("!Sample_geo_accession") | row.startswith("!Sample_title"):
            with open(outputPath, "a") as outputFile:
                #print(row)
                outputFile.write(row)
