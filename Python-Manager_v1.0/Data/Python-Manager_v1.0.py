import sys
import tkinter as tk

def Refresh():
    CurrentVersion_Label.config(text="Current Version: " + sys.version)

# Main Window
root = tk.Tk()
root.title("Python Manager (v1.0)")

# Display the Current Version
CurrentVersion_Label = tk.Label(root, text="Current Version: " + sys.version)
CurrentVersion_Label.pack(pady=10)

# Button 'Refresh'
Refresh_Button = tk.Button(root, text="Refresh", command=Refresh)
Refresh_Button.pack(pady=5)

# Run
root.mainloop()