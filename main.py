from tkinter import filedialog
from PyPDF2 import PdfFileReader
import tkinter as tk
import ebooklib
from ebooklib import epub
from gtts import gTTS

# Initialise GUI for File Dialog
root = tk.Tk()
root.withdraw()

# Open File Dialog
fileObjPath = filedialog.askopenfilename()
print(fileObjPath)

if fileObjPath.lower().endswith('.epub'):
    book = epub.read_epub(f"{fileObjPath}")
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            print(item.get_body_content())
# if fileObjPath.lower().endswith('.pdf'):
