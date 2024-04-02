import sys
import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import webbrowser

def Refresh():
    CurrentVersion_Label.config(text="Current Version: " + sys.version)

def Check_For_Update():
    try:
        # Fetch the Stable Version from the Official Python Website
        URL = "https://www.python.org/downloads/"
        Response = requests.get(URL)
        Soup = BeautifulSoup(Response.text, "html.parser")
        StableVersion = Soup.select_one(".download-list-widget .list-row-container li .release-number").text.strip()
        
        # Compare the Stable Version with the Current Version
        if StableVersion != sys.version.split()[0]:
            messagebox.showinfo("Update Available", "Stable Version (Latest): " + StableVersion)
        else:
            messagebox.showinfo("Up to Date", "You are using the Stable Version (Latest).")
    except Exception as e:
        messagebox.showerror("Error", "Failed to Check for Update.")

def Download():
    try:
        webbrowser.open("https://www.python.org/downloads/")
    except Exception as e:
        messagebox.showerror("Error", "Please visit https://www.python.org/downloads/ manually.")

def About():
    messagebox.showinfo("About", "Python Manager (v1.2)\nDeveloped by Satish Kumar Singh")

# Main Window
root = tk.Tk()
root.title("Python Manager (v1.2)")

# Top Navigation Bar
Menu = tk.Menu(root)
root.config(menu=Menu)

# Menu 'Help'
Help_Menu = tk.Menu(Menu, tearoff=0)
Menu.add_cascade(label="Help", menu=Help_Menu)
Help_Menu.add_command(label="Check for Update", command=Check_For_Update)
Help_Menu.add_command(label="Download (Latest Version)", command=Download)
Help_Menu.add_command(label="About", command=About)

# Display the Current Version
CurrentVersion_Label = tk.Label(root, text="Current Version: " + sys.version)
CurrentVersion_Label.pack(pady=10)

# Button 'Refresh'
Refresh_Button = tk.Button(root, text="Refresh", command=Refresh)
Refresh_Button.pack(pady=5)

# Run
root.mainloop()