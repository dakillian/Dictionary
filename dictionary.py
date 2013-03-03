#!/usr/bin/env python

"""At some point change the StringVar() a to something more relevant, and change the variable wordd to newword to make the code easier for someone else to read""" 

from Tkinter import *
from Tkconstants import *
import os, getpass, pickle

savedir = "Save"
usrname = getpass.getuser()
OS = os.name

"""check() checks for a directory called /home/someones_username/Save/ and if it is found, the program continues and if not found creates directory /home/someones_username/Save/ and creates an empty dictionary which is written to /home/someones_username/Save/save and then the program continues""" 
def check():
	if OS == "posix":
		if not os.path.isdir("/home/" + usrname + "/" + savedir + "/"):
			os.mkdir("/home/" + usrname + "/" + savedir + "/")
			save = {}
			pickle.dump(save, open("/home/" + usrname + "/Save/save", "wb"))

	elif OS == "Windows 7" or "Windows 8":
		if not os.path.isdir("C:\\program_files\\" + savedir + "\\"):
			os.mkdir("C:\\program_files\\" + savedir + "\\")
			save = {}
			pickle.dump(save, open("C:\\program_files\\Save/save", "wb"))
	
check()

theDict = pickle.load(open("/home/" + usrname + "/Save/save", "rb"))

def search(*ignore):
		word = searchbox.get()
		searchbox.delete(0, END)
			
		if word in theDict:
			"""I may have to wrap the text for some longer definitions"""
			a.set("Definition for \"%s\": %s" % (word, theDict[word]))

		elif word == "":
			a.set("Please enter a word in the searchbox") 
				
		elif word not in theDict:
			a.set("\"%s\" is not in the dictionary" % word)
			

def addWord():
	def getword(*ignore):
		global wordd
		wordd = searchbox.get()		

		if wordd == "":
			a.set("Please enter a word in the searchbox")
		else:		
			searchbox.delete(0, END)
			addDef()
	
	searchbox.bind(sequence="<Return>", func=getword)
	a.set("Enter new word in the text entry box above.")
	
	
def addDef():
	def getdef(*ignore):
		definition = searchbox.get()

		if definition == "":
			a.set("Please enter definition in the searchbox above")
		else:		
			a.set("Enter a word in the text entry box above to get it's definition")
			theDict[wordd] = definition
        		pickle.dump(theDict, open("/home/" + usrname + "/Save/save", "wb"))
			searchbox.delete(0, END)
			searchbox.bind(sequence="<Return>", func=search)

	searchbox.bind(sequence="<Return>", func=getdef)
	a.set("Enter definition for \"%s\":" % wordd)


root = Tk()
			
searchbox = Entry(root)
searchbox.pack()
searchbox.bind(sequence="<Return>", func=search)

a = StringVar()
a.set("Enter a word in the text entry box above to get it's definition")
display = Label(root, wraplength=400, textvariable=a)
display.pack()

add_word_btn = Button(root, text="Add new word to the dictionary", command=addWord)
add_word_btn.pack(side=BOTTOM)

root.title("Dictionary v0.1")

"""I had to get a bit of help online to try and use the geometry method"""
width = root.winfo_screenwidth() 
height = root.winfo_screenheight()
x = (width / 2) - (400 / 2)
y = (height / 2) - (80 / 2)

root.geometry("400x80+%d+%d" % (x, y))

root.mainloop()
