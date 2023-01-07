#!/bin/bash

# Concatenate all PDF files in the pdf directory into a single output PDF
pdftk pdf/*.pdf cat output output.pdf
