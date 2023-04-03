from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import random
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 30
def startGame(event):
    if timeleft == 30:
        countdown()
    nextColour()
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft = timeleft-1
        timeLabel.config(text="Time left: "+ str(timeleft))
        timeLabel.after(1000, countdown)
def nextColour():
    global score
    global timeleft
    if timeleft > 0:

        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, END)
        random.shuffle(colours)
        label.config(foreground=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " +str(score))


root = ThemedTk(theme="equilux")
root.configure(themebg="equilux")
root.title("COLORGAME")
root.geometry("375x200")
instructions = ttk.Label(root, text="Type in the color oh the words, and not the word text", font=('Helvetica', 12))
instructions.pack()
scoreLabel = ttk.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()
timeLabel = ttk.Label(root, text="time left: " +str(timeleft), font=('Helvetica', 12))
timeLabel.pack()
label = ttk.Label(root, font=("Comic Sans MS", 60, "bold"))
label.pack()
e = ttk.Entry(root)
root.bind('<Return>', startGame)
e.pack()
root.mainloop()