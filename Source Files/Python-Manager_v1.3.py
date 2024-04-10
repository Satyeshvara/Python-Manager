import sys
import subprocess
import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import webbrowser

class PythonManager:
    def __init__(self, Window):
        self.Window = Window
        self.Window.title("Python Manager")
        
        self.Menu()
        self.Display()

    def Menu(self):
        # Create Menu 
        self.Menu = tk.Menu(self.Window)
        self.Window.config(menu=self.Menu)

        # Create Menu 'Home'
        self.Home = tk.Menu(self.Menu, tearoff=0)
        self.Menu.add_cascade(label="Home", menu=self.Home)
        self.Home.add_command(label="Exit", command=self.Window.quit)

        # Create Menu 'View'
        self.View = tk.Menu(self.Menu, tearoff=0)
        self.Menu.add_cascade(label="View", menu=self.View)
        self.View.add_command(label="Packages", command=self.Packages)

        # Create Menu 'Downloads'
        self.Downloads = tk.Menu(self.Menu, tearoff=0)
        self.Menu.add_cascade(label="Downloads", menu=self.Downloads)
        self.Downloads.add_command(label="Python (Check for Updates)", command=self.Python_CheckForUpdates)
        self.Downloads.add_command(label="Python (Check for Latest Version)", command=self.Python_CheckForLatestVersion)
        self.Downloads.add_command(label="Python Package Index (PyPI)", command=self.PyPI)

        # Create Menu 'Help'
        self.Help = tk.Menu(self.Menu, tearoff=0)
        self.Menu.add_cascade(label="Help", menu=self.Help)
        self.Help.add_command(label="Check for Updates", command=self.Check_for_Updates)
        self.Help.add_separator()
        self.Help.add_command(label="About", command=self.About)

    def Packages(self):
        InstalledPackages = self.Python_Packages()
        InstalledPackages_List = '\n'.join(InstalledPackages)
        Window_Packages = tk.Toplevel(self.Window)
        Window_Packages.title("Packages (Installed)")
        Display_Packages = tk.Text(Window_Packages, height=20, width=50)
        Display_Packages.pack()
        Display_Packages.insert(tk.END, InstalledPackages_List)
        Display_Packages.config(state=tk.DISABLED)

    def Python_Packages(self):
        try:
            All_Packages = subprocess.run(['pip', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if All_Packages.returncode == 0:
                return All_Packages.stdout.splitlines()[2:]
            else:
                return ['Error: Failed to view installed Packages!']
        except FileNotFoundError:
            return ['Error: PIP is not installed or not in the PATH']
        
    def Python_CheckForUpdates(self):
        try:
            url = "https://www.python.org/downloads/"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            stable_version = soup.select_one(".download-list-widget .list-row-container li .release-number").text.strip()
            if stable_version != sys.version.split()[0]:
                messagebox.showinfo("Update Available", "Stable Version (Latest): " + stable_version)
            else:
                messagebox.showinfo("Up to Date", "You are using the Stable Version (Latest).")
        except Exception as e:
            messagebox.showerror("Error", "Failed to Check for Updates.")

    def Python_CheckForLatestVersion(self):
        try:
            webbrowser.open("https://www.python.org/downloads/")
        except Exception as e:
            messagebox.showerror("Error", "Please visit https://www.python.org/downloads/ manually.")

    def PyPI(self):
        try:
            webbrowser.open("https://pypi.org/")
        except Exception as e:
            messagebox.showerror("Error", "Please visit https://pypi.org/ manually.")

    def Check_for_Updates(self):
        webbrowser.open("https://www.github.com/satishkumarsingh2024/Python-Manager/")

    def About(self):
        messagebox.showinfo("About", "Python Manager (v1.3)\nDeveloped by Satish Kumar Singh")

    def Display(self):
        self.CurentVersion = tk.Label(self.Window, text="Current Version: " + sys.version)
        self.CurentVersion.pack(pady=10)

        self.Button_Refresh = tk.Button(self.Window, text="Refresh", command=self.Refresh)
        self.Button_Refresh.pack(pady=5)

    def Refresh(self):
        self.CurentVersion.config(text="Current Version: " + sys.version)

def main():
    root = tk.Tk()
    Application = PythonManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()