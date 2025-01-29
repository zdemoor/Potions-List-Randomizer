import random
import tkinter as tk
from tkinter import ttk
import csv

# function to ingest potion csv into a list

def read_list(filename):
    listContents = []
    with open(filename) as file:
        reader = csv.reader(file)
        return [row[0] for row in reader if row]

# calls function above, puts potion csv into list called 'potions'
potions = read_list("potions.csv")
relics = read_list("relics.csv")
curse_relics = read_list("curse_relics.csv")

# Function to update displayed potions
def generate_potions():
    selected_items = random.sample(potions, 3)
    for i, potion_label in enumerate(option_labels):
        potion_label.config(text=selected_items[i])

def generate_relics():
    selected_items = random.sample(relics, 3)
    for i, relic_label in enumerate(option_labels):
        relic_label.config(text=selected_items[i])

def generate_curse_relics():
    selected_items = random.sample(curse_relics, 3)
    for i, curse_relic_label in enumerate(option_labels):
        curse_relic_label.config(text=selected_items[i])

# This creates the main window
root = tk.Tk()
root.title("Item Selector")
root.geometry("400x400")
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


# This generates the button
potion_button = ttk.Button(root, text="Generate Potions", command=generate_potions, width=20)
relic_button = ttk.Button(root, text="Generate Relics", command=generate_relics, width=20)
curse_relic_button = ttk.Button(root, text="Generate Curse Relics", command=generate_curse_relics, width=20)

potion_button.pack(pady=10)
relic_button.pack(pady=10)
curse_relic_button.pack(pady=(10, 20))
# padx=20, pady=10
# This initializes with the first set of potions
# generate_potions()


# This creates and displays potion labels
option_labels=[]
for i in range(3):
    label = tk.Label(
        root,
        text="",
        font=("Helvetica", 14),
        fg="#ffffff",
        bg="#2b2b2b"
    )
    label.pack(pady=5)
    option_labels.append(label)

# This runs the application
root.mainloop()
