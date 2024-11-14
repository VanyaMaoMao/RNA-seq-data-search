#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from pathlib import Path

# Define the file path and gene names
input_file_path = Path(r"C:\Users\User\Example.xlsx")
gene_names = ["abc1", "abc2"]  # Example input list of gene names
output_folder_path = Path(r"C:\Users\User")

# Load the Excel file
df = pd.read_excel(input_file_path)

# Filter rows where 'gene_name' matches any of the genes in the input list
filtered_rows = df[df['gene_name'].isin(gene_names)]

# Find missing genes
missing_genes = set(gene_names) - set(filtered_rows['gene_name'].unique())

# Define the output file path
output_file = output_folder_path / "filtered_genes.txt"

# Save the filtered rows to a text file
filtered_rows.to_csv(output_file, sep='\t', index=False)

# Provide the path to the saved file
print(f"Filtered rows saved to: {output_file}")

# Print message for missing genes
if missing_genes:
    print(f"Gene(s) not found: {', '.join(missing_genes)}")
else:
    print("All genes found successfully.")

