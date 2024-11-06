import tkinter as tk
from tkinter import messagebox
import subprocess

# Function to run the selected Python file based on mode
def run_mode(mode):
    try:
        if mode == "Not Blind":
            subprocess.Popen(["python", "recall-notblinded.py"])
        elif mode == "Blind":
            subprocess.Popen(["python", "recall-blinded.py"])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start the selected mode: {e}")

# Initialize the main window
root = tk.Tk()
root.title("Face Recognition Mode Selector")
root.geometry("400x300")
root.configure(bg="#333333")  # Dark background for contrast

# Header label
header = tk.Label(root, text="Face Recognition Mode Selector", font=("Helvetica", 16, "bold"), fg="white", bg="#333333")
header.pack(pady=20)

# Mode selection instructions
instructions = tk.Label(root, text="Please choose a mode to continue:", font=("Helvetica", 12), fg="#AAAAAA", bg="#333333")
instructions.pack(pady=10)

# Styling for buttons
button_style = {
    "font": ("Helvetica", 14),
    "fg": "#FFFFFF",
    "bg": "#4444AA",
    "activebackground": "#5555DD",
    "width": 15,
    "height": 2,
    "borderwidth": 0,
}

# Blind mode button
blind_button = tk.Button(root, text="Blind", command=lambda: run_mode("Blind"), **button_style)
blind_button.pack(pady=10)

# Not Blind mode button
not_blind_button = tk.Button(root, text="Not Blind", command=lambda: run_mode("Not Blind"), **button_style)
not_blind_button.pack(pady=10)

# Footer for exit instructions
footer = tk.Label(root, text="Press 'q' in the video window to exit", font=("Helvetica", 10), fg="#888888", bg="#333333")
footer.pack(side="bottom", pady=20)

# Run the GUI event loop
root.mainloop()
