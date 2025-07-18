import random
import tkinter as tk
from tkinter import messagebox

# Generate secret number
secret_number = random.randint(1, 100)
attempts = 0

# Function to handle guess checking
def check_guess():
    global attempts
    guess = entry.get()

    if not guess.isdigit():
        feedback_label.config(text="❌ Please enter a valid number.")
        return

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        feedback_label.config(text="🔻 Too low! Try again.")
    elif guess > secret_number:
        feedback_label.config(text="🔺 Too high! Try again.")
    else:
        feedback_label.config(text=f"🎉 Correct! You guessed it in {attempts} attempts.")
        messagebox.showinfo("Congratulations!", f"You guessed it in {attempts} attempts!")
        root.destroy()  # Close the game window

# Set up GUI window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x250")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="🎲 Welcome to the Number Guessing Game!", font=("Arial", 14))
title_label.pack(pady=10)

# Instructions
instruction_label = tk.Label(root, text="I have selected a number between 1 and 100.\nTry to guess it!", font=("Arial", 10))
instruction_label.pack()

# Entry for guess
entry = tk.Entry(root, font=("Arial", 12), justify='center')
entry.pack(pady=10)

# Submit button
submit_button = tk.Button(root, text="Guess", command=check_guess, font=("Arial", 12))
submit_button.pack(pady=5)

# Feedback label
feedback_label = tk.Label(root, text="", font=("Arial", 12))
feedback_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
