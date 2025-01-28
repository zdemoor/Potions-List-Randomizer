import random
import tkinter as tk
from tkinter import ttk

# Database of Potions
database = [
    "Bottled Flame",
    "Claw Potion",
    "Diminish",
    "Shield Potion",
    "Winged Potion",
    "Toxic Droplet",
    "Angel Elixir",
    "Running Shoe Potion",
    "Pacifist Juice",
    "Steel Potion",
    "Totem Shot",
    "Vitamins",
    "Blue Brain Juice",
    "Blue Mist",
    "Negate Potion",
    "Hostile Intent",
    "Bolster Up",
    "Right Angle Potion",
    "Bottled Whiplash",
    "Invulnerability Potion",
    "Mist Me",
    "Growth and Decay"
]

# Function to update displayed potions
def generate_potions():
    selected_items = random.sample(database, 3)
    for i, potion_label in enumerate(potion_labels):
        potion_label.config(text=selected_items[i])

# This creates the main window
root = tk.Tk()
root.title("Random Potion Selector")
root.geometry("400x300")
root.config(bg="#2b2b2b")  # Dark background

# Title Label
title_label = tk.Label(
    root,
    text="Random Potion Selector",
    font=("Helvetica", 18, "bold"),
    fg="#ffcc00",
    bg="#2b2b2b"
)
title_label.pack(pady=10)

# This creates and displays potion labels
potion_labels = []
for i in range(3):
    label = tk.Label(
        root,
        text="",
        font=("Helvetica", 14),
        fg="#ffffff",
        bg="#2b2b2b"
    )
    label.pack(pady=5)
    potion_labels.append(label)

# This generates the button
generate_button = ttk.Button(
    root,
    text="Generate Potions",
    command=generate_potions
)
generate_button.pack(pady=20)

# This initializes with the first set of potions
generate_potions()

# This runs the application
root.mainloop()
