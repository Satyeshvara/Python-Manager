import sys
import tkinter as tk
import requests
from bs4 import BeautifulSoup

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
            StableVersion_Label.config(text="Stable Version (Latest): " + StableVersion)
        else:
            StableVersion_Label.config(text="You are using the Stable Version (Latest).")
    except Exception as e:
        StableVersion_Label.config(text="Error: Failed to Check for Update.")

# Main Window
root = tk.Tk()
root.title("Python Manager (v1.1)")

# Display the Current Version
CurrentVersion_Label = tk.Label(root, text="Current Version: " + sys.version)
CurrentVersion_Label.pack(pady=10)

# Button 'Refresh'
Refresh_Button = tk.Button(root, text="Refresh", command=Refresh)
Refresh_Button.pack(pady=5)

# Button 'Check for Update'
Update_Button = tk.Button(root, text="Check for Update", command=Check_For_Update)
Update_Button.pack(pady=5)

# Display the Stable Version (Latest)
StableVersion_Label = tk.Label(root, text="")
StableVersion_Label.pack(pady=10)

# Run
root.mainloop()