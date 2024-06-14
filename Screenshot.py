# import pyautogui
# from tkinter import *

# def take_ss():
#     add=entry.get()
#     path=add+"\\ss1.png"
#     ss=pyautogui.screenshot()
#     print(path)

#     ss.save(r"C:\Users\bansa\Desktop\python_projects\ss1.png")




# win=Tk()
# win.title("TakeScreenshot")
# win.geometry("400x300")
# win.config(bg="orange")
# win.resizable(False,False)

# entry=Entry(win, font=('TIME NEW ROMAN',15))
# entry.place(x=20,height=50,width=350,y=50)

# button=Button(win, text="Done", font=('TIME NEW ROMAN',25),bg="red")
# button.place(x=150,y=130,h=60,width=100)





# win.mainloop()



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
