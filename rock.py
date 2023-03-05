import tkinter as tk
import random

window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

title_label = tk.Label(window, text="Rock-Paper-Scissors Game", font=("Arial", 20))
title_label.pack()

instruction_label = tk.Label(window, text="Select your move:", font=("Arial", 14))
instruction_label.pack()

result_label = tk.Label(window, text="", font=("Arial", 16))
result_label.pack()

computer_label = tk.Label(window, text="", font=("Arial", 14))
computer_label.pack()

def rock():
    computer_move = random.choice(["Rock", "Paper", "Scissors"])
    if computer_move == "Rock":
        result_label.config(text="Tie", fg="blue")
    elif computer_move == "Paper":
        result_label.config(text="You Lose", fg="red")
    else:
        result_label.config(text="You Win", fg="green")
    computer_label.config(text="Computer's move: " + computer_move)

def paper():
    computer_move = random.choice(["Rock", "Paper", "Scissors"])
    if computer_move == "Paper":
        result_label.config(text="Tie", fg="blue")
    elif computer_move == "Scissors":
        result_label.config(text="You Lose", fg="red")
    else:
        result_label.config(text="You Win", fg="green")
    computer_label.config(text="Computer's move: " + computer_move)

def scissors():
    computer_move = random.choice(["Rock", "Paper", "Scissors"])
    if computer_move == "Scissors":
        result_label.config(text="Tie", fg="blue")
    elif computer_move == "Rock":
        result_label.config(text="You Lose", fg="red")
    else:
        result_label.config(text="You Win", fg="green")
    computer_label.config(text="Computer's move: " + computer_move)

def reset():
    result_label.config(text="")
    computer_label.config(text="")
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")


rock_button = tk.Button(window, text="Rock", command=rock, bg="yellow", fg="Black", font=("Arial", 12))
rock_button.pack(pady=10)

paper_button = tk.Button(window, text="Paper", command=paper, bg="salmon", fg="Black", font=("Arial", 12))
paper_button.pack(pady=10)

scissors_button = tk.Button(window, text="Scissors", command=scissors, bg="pink", fg="Black", font=("Arial", 12))
scissors_button.pack(pady=10)

reset_button = tk.Button(window, text="Reset", command=reset, bg="plum", fg="Black", font=("Arial", 12))
reset_button.pack(pady=10)

window.mainloop()