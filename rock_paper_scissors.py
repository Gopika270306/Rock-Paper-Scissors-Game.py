import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer = random.choice(choices)

    if user_choice == computer:
        result = "Tie!"
    elif (
        (user_choice == "Rock" and computer == "Scissors") or
        (user_choice == "Paper" and computer == "Rock") or
        (user_choice == "Scissors" and computer == "Paper")
    ):
        result = "You Win!"
    else:
        result = "You Lose!"

    output.config(text=f"Computer: {computer}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

tk.Label(root, text="Choose One", font=("Arial", 14)).pack(pady=10)

for choice in choices:
    tk.Button(root, text=choice, command=lambda c=choice: play(c)).pack(pady=5)

output = tk.Label(root, text="", font=("Arial", 12))
output.pack(pady=20)

root.mainloop()