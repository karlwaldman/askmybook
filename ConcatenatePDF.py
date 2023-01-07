import os
import pdfkit

# Set the input and output directories
input_dir = "/mnt/c/Users/User/OneDrive/Documents/GitHub/askmybook/pdf"
output_dir = "/mnt/c/Users/User/OneDrive/Documents/GitHub/askmybook"

# Create a list to store the input PDF files
input_files = []

# Iterate over all PDF files in the input directory
for file in os.listdir(input_dir):
    if file.endswith(".pdf"):
        # Add the PDF file to the input files list
        input_files.append(f"{input_dir}/{file}")

# Concatenate the input PDF files into a single output PDF
#pdfkit.concat(input_files, f"{output_dir}/concatenated.pdf")
pdfkit.from_file(input_files, f"{output_dir}/concatenated.pdf")
