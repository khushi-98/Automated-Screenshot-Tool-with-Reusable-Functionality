import os
import pyautogui
import tkinter as tk
from tkinter import messagebox
import keyboard
import time

# Function to get the default Downloads folder path
def get_downloads_path():
    return os.path.join(os.path.expanduser("~"), "Downloads")

# Function to take a screenshot
def take_screenshot():
    # Wait for the user to press 's' before taking the screenshot
    keyboard.wait('s')
    
    # Take a screenshot
    ss = pyautogui.screenshot()

    # Automatically save the screenshot to the Downloads folder
    downloads_path = get_downloads_path()
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    default_file_path = os.path.join(downloads_path, f"screenshot_{timestamp}.png")
    ss.save(default_file_path)

    # Notify the user that the screenshot is saved
    messagebox.showinfo("Screenshot Saved", f"Screenshot automatically saved to {default_file_path}")
    print(f"Screenshot saved to {default_file_path}")

# Initialize Tkinter root
root = tk.Tk()
root.withdraw()  # Hide the root window

# Notify the user to navigate to the desired screen and press 's' to take a screenshot
messagebox.showinfo("Prepare for Screenshot", "Navigate to the screen you want to capture, then press 's' to take a screenshot. Press 'q' to quit.")

# Main loop to take multiple screenshots
while True:
    if keyboard.is_pressed('q'):
        print("Exiting screenshot tool.")
        break
    take_screenshot()

root.mainloop()
