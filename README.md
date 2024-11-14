# RNA-seq-data-search
This repository contains a Python script for filtering specified genes from an Excel file and outputting them to a text file. This script is designed to streamline the analysis of gene expression data by extracting only the genes of interest.

# Gene Filtering Script

This repository contains a Python script for filtering specified genes from an Excel file and outputting them to a text file. This script is designed to streamline the analysis of gene expression data by extracting only the genes of interest.

## Features
- Loads gene expression data from an Excel file.
- Filters rows based on a provided list of gene names.
- Outputs the filtered data to a text file.
- Identifies any genes from the list that are missing in the data.

## Requirements
- **Python 3.x**
- Required Python libraries: `pandas`, `pathlib`

## Usage

1. **Specify Gene Names**: Define the list of genes to be filtered in the `gene_names` list.  
   - Note: Gene names should be written in lowercase (e.g., `adipor1`, `fadd`).

2. **Place the Excel File**: Save your .xlsx file in the path specified by `input_file_path`. You can adjust this path within the script.

3. **Set the Output Folder**: Specify the folder path where the output file will be saved in `output_folder_path`.

4. **Run the Script**: Execute the script with the following command:
   ```bash
   python gene_filtering_script.py

## Output: 
A text file filtered_genes.txt will be generated in the specified output folder, containing only the rows that match the genes in gene_names.

## Notes
1. Ensure that gene names are listed in lowercase. Capitalized names may not match and will be considered missing.
2. Any genes not found in the Excel file will be listed in the console output.
3. Don’t forget to adjust the paths for the input file and output folder based on your file locations.
