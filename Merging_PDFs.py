import os
from PyPDF2 import PdfWriter
import tkinter as tk
from tkinter import filedialog

# Create a tkinter root window (hidden)
root = tk.Tk()
root.withdraw()

# Open a file dialog for the user to select the first PDF file
file_path = filedialog.askopenfilename(title="Select First File")
pdfs = [file_path]

# Open a file dialog for the user to select the second PDF file
file_path1 = filedialog.askopenfilename(title="Select Second File")
pdfs.append(file_path1)
print("Selected PDF files:", pdfs)

# Filter out non-PDF files from the list
pdfs = [file for file in pdfs if file.endswith(".pdf")]

# Create a PdfWriter instance to merge PDFs
merger = PdfWriter()
# Making sure both file are pdf
if len(pdfs) == 2:
    # Iterate through the selected PDF files and merge them
    for each_pdf in pdfs:
        with open(fr'{each_pdf}', 'rb') as a:
            if os.path.getsize(fr'{each_pdf}') > 0:
                merger.append(a)

    # Open a file dialog for the user to specify a file path for saving
    save_location = filedialog.asksaveasfilename(title="Save File As", defaultextension=".pdf")
    print("Save location:", save_location)

    # Write the merged PDF to the specified save location
    merger.write(save_location)
    merger.close()

    print("PDFs merged and saved successfully.")
else:
    print('Please only select PDF files')
