import tkinter as tk
import time

class ClickGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Click the Button Game")

        # Set up the score and time variables
        self.score = 0
        self.time_left = 10  # 10 seconds for the game

        # Label to show the score
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Helvetica", 16))
        self.score_label.pack()

        # Label to show the time left
        self.time_label = tk.Label(root, text=f"Time left: {self.time_left}", font=("Helvetica", 16))
        self.time_label.pack()

        # Button to click
        self.click_button = tk.Button(root, text="Click me!", font=("Helvetica", 14), width=20, height=2, command=self.button_clicked)
        self.click_button.pack(pady=20)

        # Start button
        self.start_button = tk.Button(root, text="Start Game", font=("Helvetica", 14), width=20, height=2, command=self.start_game)
        self.start_button.pack(pady=20)

    def button_clicked(self):
        if self.time_left > 0:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")

    def update_time(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"Time left: {self.time_left}")
            self.root.after(1000, self.update_time)
        else:
            self.click_button.config(state="disabled")
            self.time_label.config(text="Game Over!")

    def start_game(self):
        self.score = 0
        self.time_left = 10
        self.score_label.config(text=f"Score: {self.score}")
        self.time_label.config(text=f"Time left: {self.time_left}")
        self.click_button.config(state="normal")
        self.update_time()

# Create the GUI application
root = tk.Tk()
game = ClickGame(root)
root.mainloop()
