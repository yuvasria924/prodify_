import tkinter as tk
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")
        
        self.random_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 5
        
        self.label = tk.Label(root, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)
        
        self.submit_button = tk.Button(root, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=5)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
        
        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(pady=5)
    
    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            
            if guess < self.random_number:
                self.result_label.config(text=f"Too low! Attempts left: {self.max_attempts - self.attempts}")
            elif guess > self.random_number:
                self.result_label.config(text=f"Too high! Attempts left: {self.max_attempts - self.attempts}")
            else:
                self.result_label.config(text=f"Correct! You win! It took you {self.attempts} attempts.")
                self.submit_button.config(state=tk.DISABLED)
                return
            
            if self.attempts >= self.max_attempts:
                self.result_label.config(text=f"Game Over! The correct number was {self.random_number}.")
                self.submit_button.config(state=tk.DISABLED)
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
    
    def reset_game(self):
        self.random_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.submit_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()

