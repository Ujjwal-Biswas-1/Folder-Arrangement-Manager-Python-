from main import organise_main
import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title("Folder Organiser",)
window.geometry("960x540")

selected_folder = ""

folder_label = tk.Label(window, text="No Folder Selected", font=(
    "Arial", 20, "bold"), wraplength=400, justify="center",)
folder_label.pack(pady=25)


def choose_button():
    global selected_folder
    folder_path = filedialog.askdirectory()
    if folder_path:
        selected_folder = folder_path
        folder_label.config(text=f"Selected Folder:\n {folder_path}")
    else:
        folder_label.config(text=f"Folder not Found")


select_button = tk.Button(window, text="Choose Folder", command=choose_button)
select_button.pack(pady=20)


def main_click():
    if selected_folder:
        organise_main(selected_folder)
        folder_label.config(text=f"Organised\n {selected_folder}")
    else:
        folder_label.config(text=f"Please Choose folder")


apply = tk.Button(window, text="Apply", command=main_click)
apply.pack(pady=20)


window.mainloop()
