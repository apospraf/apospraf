__author__ = 'Apospraf'

import requests
import webbrowser
import DeleteCharacters
from Tkinter import *
from bs4 import BeautifulSoup

top = Tk()

def findMovie(event):
    url = entry.get()
    entry.delete(0, 'end')
    sourceCode = requests.get(url)
    sourceText = sourceCode.text
    soup = BeautifulSoup(sourceText, "html.parser")
    if soup.find('div', class_="originalTitle"):
        title = soup.find('div', class_="originalTitle").text
        titleSplitList = title.split('(original title)')
        titleSplit = DeleteCharacters.delchar(titleSplitList[0]).split()
    elif soup.find('h1', {'itemprop': 'name'}):
        title = soup.find('h1', {'itemprop': 'name'}).text
        titleSplit = DeleteCharacters.delchar(title).split()
    else:
        print("Movie could not be found")
        return 0

    katUrl = 'https://kat.cr/usearch/' + titleSplit[0]
    for i in titleSplit[1:]:
        katUrl += '%20' + i

    webbrowser.open(katUrl)



label = Label(top, text="Give Imdb Url", font='20')
entry = Entry(top, font="12")
button = Button(top, text="Done", font='14')
button.bind("<Button-1>", findMovie)

label.grid(row=0)
entry.grid(row=0, column=1)
button.grid(row=1, columnspan=2)


top.mainloop()

