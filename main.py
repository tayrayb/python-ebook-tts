from operator import gt
from tkinter import filedialog
from PyPDF2 import PdfFileReader
import tkinter as tk
import ebooklib
from ebooklib import epub
from gtts import gTTS
from bs4 import BeautifulSoup

# Initialise GUI for File Dialog
root = tk.Tk()
root.withdraw()

# Open File Path
fileObjPath = filedialog.askopenfilename()
print(fileObjPath)

def convert_txt_tts():
    fileObj = open('output.txt', 'r').read().replace('\n', ' ')
    tts = gTTS(fileObj, lang='en')
    tts.save('output.mp3')

def open_book():
    if fileObjPath.lower().endswith('.epub'):
        book = epub.read_epub(fileObjPath)
        content = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
        for chapter in content:
            soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
            text = soup.text.replace('/n', ' ').strip()
            with open('output.txt', 'a') as f:
                f.write(text)

def main():
    with open('output.txt', 'w') as f:
        f.write('')
    open_book()
    convert_txt_tts()


if __name__ == "__main__":
    main()
