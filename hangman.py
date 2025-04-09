import tkinter as tk
from tkinter import messagebox
import random

# List of words for the game
words = ["python", "hangman", "programming", "computer", "algorithm", "developer", "openai"]

# Debugging: Print the words list
print("Words list:", words)

# Select a random word from the list
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6

# Initialize the main window
root = tk.Tk()
root.title("Test")

# Function to update the display
def update_display():
    word_label.config(text=" ".join(guessed_word))
    attempts_label.config(text=f"Attempts left: {attempts}")

# Function to handle guess
def guess_letter():
    global attempts  
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if len(letter) != 1 or not letter.isalpha():
        messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        return

    if letter in guessed_word:  
        messagebox.showwarning("Already Guessed", "You have already guessed this letter.")
        return

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed_word[i] = letter  
        update_display()
        if "_" not in guessed_word:
            messagebox.showinfo("Congratulations!", "You've guessed the word!")
            root.quit()
    else:
        attempts -= 1
        update_display()
        if attempts == 0:
            messagebox.showinfo("Game Over", f"Out of attempts! The word was: {word}")
            root.quit()

# UI Elements
word_label = tk.Label(root, text=" ".join(guessed_word), font=("Arial", 24))
word_label.pack(pady=20)

attempts_label = tk.Label(root, text=f"Attempts left: {attempts}", font=("Arial", 18))
attempts_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 18))
entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess", command=guess_letter, font=("Arial", 18))
guess_button.pack(pady=10)

tk.Label(root, text="Hello, Tkinter!").pack()

# Start the game
update_display()

# Run the main loop
root.mainloop()
