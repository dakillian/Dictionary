#!/usr/bin/env python

"""Still need to test the Windows directory portion of the code to see if it works""" 

from Tkinter import *
from Tkconstants import *
import os, getpass, pickle

savedir = "Save"
usrname = getpass.getuser()
OS = os.name

"""check() checks for a directory called /home/someones_username/Save/ and if it is found, the program continues and if 
not found creates directory /home/someones_username/Save/ and creates an empty dictionary which is written to /home/someones_username/Save/save 
and then the program continues. It also checks which operating system the script is running on and if it's Windows 7 or
8 it changes the path to something more Windows friendly""" 
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
			pickle.dump(save, open("C:\\program_files\\Save\\save", "wb"))
	
check()

if OS == "posix":
	theDict = pickle.load(open("/home/" + usrname + "/Save/save", "rb"))
	
elif OS == "Windows 7" or "Windows 8":
	theDict = pickle.load(open("C:\\program_files\\Save\\save", "rb"))

def search(*ignore):
		word = searchbox.get()
		searchbox.delete(0, END)
			
		if word in theDict:
			"""I may have to wrap the text for some longer definitions"""
			display_string.set("Definition for \"%s\": %s" % (word, theDict[word]))

		elif word == "":
			display_string.set("Please enter a word in the searchbox") 
				
		elif word not in theDict:
			display_string.set("\"%s\" is not in the dictionary" % word)
			

def addWord():
	def getword(*ignore):
		global newword
		newword = searchbox.get()		

		if newword == "":
			display_string.set("Please enter a word in the searchbox")
		else:		
			searchbox.delete(0, END)
			addDef()
	
	searchbox.bind(sequence="<Return>", func=getword)
	display_string.set("Enter new word in the text entry box above.")
	
	
def addDef():
	def getdef(*ignore):
		definition = searchbox.get()

		if definition == "":
			display_string.set("Please enter definition in the searchbox above")
		else:		
			display_string.set("Enter a word in the text entry box above to get it's definition")
			theDict[newword] = definition
			
			if OS == "posix":
        			pickle.dump(theDict, open("/home/" + usrname + "/Save/save", "wb"))
        		
        		elif OS == "Windows 7" or "Windows 8":
        			pickle.dump(theDict, open("C:\\program_files\\Save\\save", "wb"))
        			
			searchbox.delete(0, END)
			searchbox.bind(sequence="<Return>", func=search)

	searchbox.bind(sequence="<Return>", func=getdef)
	display_string.set("Enter definition for \"%s\":" % wordd)


root = Tk()
			
searchbox = Entry(root)
searchbox.pack()
searchbox.bind(sequence="<Return>", func=search)

display_string = StringVar()
display_string.set("Enter a word in the text entry box above to get it's definition")
display = Label(root, wraplength=400, textvariable=display_string)
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
