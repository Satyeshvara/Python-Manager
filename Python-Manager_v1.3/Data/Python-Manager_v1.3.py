import sys
import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import subprocess
import webbrowser

def Check_For_Packages():
    try:
        Packages = subprocess.run(['pip', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if Packages.returncode == 0:
            return Packages.stdout.splitlines()[2:]
        else:
            return ['Error: Failed to view installed Packages!']

    except FileNotFoundError:
        return ['Error: PIP is not installed or not in the PATH']

def Show_Packages():
    InstalledPackages = Check_For_Packages()
    List_InstalledPackages = '\n'.join(InstalledPackages)
    Window_Packages = tk.Toplevel(root)
    Window_Packages.title("Packages (Installed)")
    Text_Packages = tk.Text(Window_Packages, height=20, width=50)
    Text_Packages.pack()
    Text_Packages.insert(tk.END, List_InstalledPackages)
    Text_Packages.config(state=tk.DISABLED)
    
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

def Python_LatestVersion():
    try:
        webbrowser.open("https://www.python.org/downloads/")
    except Exception as e:
        messagebox.showerror("Error", "Please visit https://www.python.org/downloads/ manually.")

def PyPI():
    try:
        webbrowser.open("https://pypi.org/")
    except Exception as e:
        messagebox.showerror("Error", "Please visit https://pypi.org/ manually.")

def About():
    messagebox.showinfo("About", "Python Manager (v1.3)\nDeveloped by Satish Kumar Singh")

def Refresh():
    CurrentVersion_Label.config(text="Current Version: " + sys.version)

def Exit():
    root.destroy()

# Main Window
root = tk.Tk()
root.title("Python Manager (v1.3)")

# Top Navigation Bar
Menu = tk.Menu(root)
root.config(menu=Menu)

# Menu 'Home'
Home_Menu = tk.Menu(Menu, tearoff=0)
Menu.add_cascade(label="Home", menu=Home_Menu)
Home_Menu.add_command(label="Exit", command=Exit)

# Menu 'View'
View_Menu = tk.Menu(Menu, tearoff=0)
Menu.add_cascade(label="View", menu=View_Menu)
View_Menu.add_command(label="Packages", command=Show_Packages)

# Menu 'Downloads'
Downloads_Menu = tk.Menu(Menu, tearoff=0)
Menu.add_cascade(label="Downloads", menu=Downloads_Menu)
Downloads_Menu.add_command(label="Python (Check for Update)", command=Check_For_Update)
Downloads_Menu.add_command(label="Python (Check for Latest Version)", command=Python_LatestVersion)
Downloads_Menu.add_command(label="Python Package Index (PyPI)", command=PyPI)

# Menu 'Help'
Help_Menu = tk.Menu(Menu, tearoff=0)
Menu.add_cascade(label="Help", menu=Help_Menu)
Help_Menu.add_command(label="About", command=About)

# Display the Current Version
CurrentVersion_Label = tk.Label(root, text="Current Version: " + sys.version)
CurrentVersion_Label.pack(pady=10)

# Button 'Refresh'
Refresh_Button = tk.Button(root, text="Refresh", command=Refresh)
Refresh_Button.pack(pady=5)

# Run
root.mainloop()