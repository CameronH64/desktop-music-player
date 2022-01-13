import os
import sys
from tkinter import *
import pygame

# Program setup

# Set up the Tkinter window.
root = Tk()
root.geometry("500x300+1100+600")
root.resizable(False, False)         # (x, y)
root.title("Music Player")


def playPauseButtonClicked():
	print("Play/Pause button clicked.")

# def createGUIElements():
#
# 	playButtonImage = PhotoImage(file='assets/play.png')
#
# 	playPauseButton = Button(root,
# 							 text="Play/Pause",
# 							 width=10,
# 							 height=1,
# 							 image=playButtonImage,
# 							 command=playPauseButtonClicked)
#
# 	playPauseButton.place(x=300, y=250)
#
# 	nextSongButton = Button(root,
# 							 text="Next",
# 							 width=10,
# 							 height=1,
# 							 command=playPauseButtonClicked)
#
# 	nextSongButton.place(x=200, y=250)
#
# 	previousSongButton = Button(root,
# 							 text="Previous",
# 							 width=10,
# 							 height=1,
# 							 command=playPauseButtonClicked)
#
# 	previousSongButton.place(x=400, y=250)


def executeInput(userInput):
	if userInput == "play":
		print("You pressed play.")
		pygame.mixer.music.play()
	elif userInput == "exit":
		sys.exit()

def main():
	# root.mainloop()
	programRunning = True
	print("Program start.")

	pygame.mixer.init()
	pygame.mixer.music.load("testingFiles/lon.mp3")
	pygame.mixer.music.set_volume(0.5)

	while programRunning:
		userInput = input("Enter a command: ")
		executeInput(userInput)



if __name__ == "__main__":
	main()