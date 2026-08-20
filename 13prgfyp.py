import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime, timedelta
##F7C172 yellow

#def show_input_page():
#    output_page.pack_forget()
#input_page.pack(fill="both", expand=True)

#input_page.pack_forget()    
#    output_page.pack(fill="both", expand=True)

#GUI window
root = tk.Tk()

#title of the window
root.title("")

#size of the window
root.geometry("650x700+10+10")

#prevents resizing of the window 
root.resizable(False, False)

input_page = tk.Frame(root, background="#EE5361", width=600, height=1152)
input_page.pack(fill="both", expand=True)
input_page.pack_propagate(False)

#output_page = tk.Frame(root, background="white", width=600, height=200)
#output_page.pack(fill="both", expand=True)
#output_page.pack_propagate(False)

root.mainloop()
