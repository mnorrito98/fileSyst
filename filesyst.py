"""
Program: filesystem.py
Author: Mike Norrito 
Provides a menu driven tool for navigating a file system and gathering information on files
"""
import os, os.path 

# Global constants and vasriables 

QUIT = '7'
COMMANDS = ('1', '2', '3', '4', '5', '6', '7', '8')

MENU = """1. List the current directory 
2. Move up
3. Move down
4. Number of files in the directory 
5. Size of the directory in bytes 
6. Search for a filename 
7. QUIT the program
8. Special Surprise!"""


def main():
	while True:
		print(os.getcwd())
		print(42*"-")
		print(MENU)
		print(42*"-")
		command = acceptComm()
		runComm(command)
		if command == QUIT:
			print(42 * ".")
			print("Have a wonderful day!")
			print(42 * ".")
			break
def acceptComm():
	"""Inputs and returns a legit command number """
	command = input("Enter a number: ")
	if command in COMMANDS:
		return command
	else: 
		print("ERROR: Command NOT Recognized")
		return acceptComm()

def runComm(command):
	"""Selects and runs a command """
	if command == '1':
		listCurrentDir(os.getcwd())
	elif command == '2':
		moveUp()
	elif command == '3':
		moveDown(os.getcwd())
	elif command == '4':
		print("")
		print("The total number of files is", countFiles(os.getcwd()))
		print("")
	elif command == '5':
		print("")
		print("The total number of bytes is", countBytes(os.getcwd()))
		print("")
	elif command == '8':
		print("")
		print("YOU HAVE WON... NOTHINGGGG!!!! HURRAY!!!")
		print("")
	elif command == '6':
		print("")
		target = input("Enter the search string: ")
		fileList = findFiles(target, os.getcwd())
		if not fileList:
			print("")
			print("String not found")
			print("")
		else: 
			for f in fileList:
				print(f)

def listCurrentDir(dirName):
	"""Prints a list of the cwd's contents."""
	lyst = os.listdir(dirName)
	for element in lyst: print(element)

def moveUp():
	"""Moves up to the parent directory """
	os.chdir("..")

def moveDown(currentDir):
	"""Moves down to the named subdirectory if it exists """
	newDir = input("Enter the directory name: ")
	if os.path.exists(currentDir + os.sep + newDir) and os.path.isdir(newDir):
			os.chdir(newDir)
	else:
		print("ERROR: no such name...")

def countFiles(path):
	"""Returns the number of files in the cwd and all it's subdirectories """
	count = 0
	lyst = os.listdir(path)
	for element in lyst:
		if os.path.isfile(element):
			count += 1 
		else: 
			os.chdir(element)
			count += countFiles(os.getcwd())
			os.chdir("..")
	return count

def countBytes(path):
	"""Returns the number of bytes in the cwd and all its subdirectories """
	count = 0 
	lyst = os.listdir(path)
	for element in lyst:
		if os.path.isfile(element):
			count += os.path.getsize(element)
		else:
			os.chdir(element)
			count += countBytes(os.getcwd())
			os.chdir("..")
	return count

def findFiles(target, path): 
	"""Returns a list of the filenames that contain the target string in the cwd and all its subdirectories """
	files = []
	lyst = os.listdir(path)
	for element in lyst:
		if os.path.isfile(element):
			if target in element:
				files.append(path + os.sep + element)
		else:
			os.chdir(element)
			files.extend(findFiles(target, os.getcwd()))
			os.chdir("..")
	return files 


main()