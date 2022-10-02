from genericpath import isfile
from operator import gt
from tkinter import filedialog
from PyPDF2 import PdfFileReader
import tkinter as tk
import ebooklib
from ebooklib import epub
from gtts import gTTS
from bs4 import BeautifulSoup
import sys

# Initialise GUI for File Dialog
root = tk.Tk()
root.withdraw()

# Open File Path
fileObjPath = filedialog.askopenfilename()


def convert_txt_tts():
    file_obj = open('output.txt', 'rt', encoding='utf-8').read().replace('\n', ' ')
    tts = gTTS(file_obj, lang='en')
    tts.save('output.mp3')


def open_book():
    if fileObjPath.lower().endswith('.epub'):
        book = epub.read_epub(fileObjPath)
        content = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
        page_store = []
        for chapter in content:
            soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
            text = soup.text.replace('/n', ' ').strip()
            page_store.append(text)
        with open('output.txt', 'a', encoding='utf-8') as f:
            f.write(' '.join(page_store))
        return None
    if fileObjPath.lower().endswith('.pdf'):
        book = PdfFileReader(fileObjPath)
        number_of_pages = len(book.pages)
        page_store = []
        for page in range(number_of_pages):
            page_store.append(book.pages[page].extract_text())
        with open('output.txt', 'a', encoding='utf-8') as f:
            f.write(' '.join(page_store))
        return None
    return None


def main():
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write('')
    print('Opening Book...')
    open_book()
    print('Converting output.txt to .mp3....')
    convert_txt_tts()
    sys.exit('Completed Conversion!')


if __name__ == "__main__":
    main()