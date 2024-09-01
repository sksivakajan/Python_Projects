import tkinter as tk
import random

class DragonGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Dragon Catch the Prey")

        # Set up canvas
        self.canvas = tk.Canvas(root, width=600, height=400, bg="skyblue")
        self.canvas.pack()

        # Create the dragon (a green circle)
        self.dragon = self.canvas.create_oval(290, 190, 310, 210, fill="green", outline="black")

        # Create prey (a red dot)
        self.prey = self.canvas.create_oval(0, 0, 0, 0, fill="red")

        # Score and time left
        self.score = 0
        self.time_left = 30  # Game lasts for 30 seconds

        # Labels for score and time left
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Helvetica", 14))
        self.score_label.pack()

        self.time_label = tk.Label(root, text=f"Time left: {self.time_left}", font=("Helvetica", 14))
        self.time_label.pack()

        # Keyboard bindings to move the dragon
        root.bind("<Up>", self.move_up)
        root.bind("<Down>", self.move_down)
        root.bind("<Left>", self.move_left)
        root.bind("<Right>", self.move_right)

        # Start the game
        self.place_prey()
        self.update_time()

    def place_prey(self):
        """Place prey at a random location."""
        x = random.randint(20, 580)
        y = random.randint(20, 380)
        self.canvas.coords(self.prey, x-10, y-10, x+10, y+10)

    def move_up(self, event):
        self.canvas.move(self.dragon, 0, -10)
        self.check_collision()

    def move_down(self, event):
        self.canvas.move(self.dragon, 0, 10)
        self.check_collision()

    def move_left(self, event):
        self.canvas.move(self.dragon, -10, 0)
        self.check_collision()

    def move_right(self, event):
        self.canvas.move(self.dragon, 10, 0)
        self.check_collision()

    def check_collision(self):
        """Check if the dragon catches the prey."""
        dragon_coords = self.canvas.coords(self.dragon)
        prey_coords = self.canvas.coords(self.prey)

        if (dragon_coords[0] < prey_coords[2] and dragon_coords[2] > prey_coords[0] and
                dragon_coords[1] < prey_coords[3] and dragon_coords[3] > prey_coords[1]):
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.place_prey()

    def update_time(self):
        """Update the remaining time."""
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"Time left: {self.time_left}")
            self.root.after(1000, self.update_time)
        else:
            self.canvas.create_text(300, 200, text="Game Over!", font=("Helvetica", 24), fill="red")
            self.canvas.unbind_all("<Up>")
            self.canvas.unbind_all("<Down>")
            self.canvas.unbind_all("<Left>")
            self.canvas.unbind_all("<Right>")

# Create the GUI application
root = tk.Tk()
game = DragonGame(root)
root.mainloop()
