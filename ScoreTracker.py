# football code
from tkinter import *
import tkinter as tk

root = Tk()
root.title("Score tracker")

# Teams
HomeTeam = Label(root, text="Home Team score:", fg="blue")
VisitTeam = Label(root, text="Visiting Team score:", fg="red")

score1 = Label(root, text="0")
score2 = Label(root, text="0")


def home_tracker(num):
    counter = int(str(score1['text']))
    counter += num
    score1.config(text=str(counter))


def visit_tracker(num):
    counter = int(str(score2['text']))
    counter += num
    score2.config(text=str(counter))

# Grid
HomeTeam.grid(row=0, column=0)
VisitTeam.grid(row=1, column=0)
score1.grid(row=0, column=1)
score2.grid(row=1, column=1)

# Field Goal
field_goal1 = tk.Button(root, text="Field Goal", width=20, command=lambda: home_tracker(3), fg="blue")
field_goal1.grid(row=2, column=0)

field_goal2 = tk.Button(root, text="Field Goal", width=20, command=lambda: visit_tracker(3), fg="red")
field_goal2.grid(row=2, column=1)

# Touch Down
Touchdown1 = tk.Button(root, text="Touch Down", width=20, command=lambda: home_tracker(6), fg="blue")
Touchdown1.grid(row=3, column=0)

Touchdown2 = tk.Button(root, text="Touch Down", width=20, command=lambda: visit_tracker(6), fg="red")
Touchdown2.grid(row=3, column=1)

# Field Kick
field_kick1 = tk.Button(root, text="Field Kick", width=20, command=lambda: home_tracker(1), fg="blue")
field_kick1.grid(row=4, column=0)

field_kick2 = tk.Button(root, text="Field Kick", width=20, command=lambda: visit_tracker(1), fg="red")
field_kick2.grid(row=4, column=1)

def reset_score():
  score1.config(text="0")
  score2.config(text="0")
  
reset_button = tk.Button(root, text="RESET", width=5, command=lambda: reset_score(), fg="green")
reset_button.grid(row=7, column=0)

quit = Button(text = "Quit", width=5, command = root.destroy, fg = "green")
quit.grid(row = 7, column = 1)
mainloop()
