import tkinter as tk
from tkinter import filedialog

# to open a text file and load its content into the Text widget
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_widget.delete("1.0", tk.END)  
            text_widget.insert(tk.END, file.read())  

# to save the content of the Text widget to a text file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_widget.get("1.0", tk.END))  

# to create a new blank document
def new_file():
    text_widget.delete("1.0", tk.END)  

def cut_text():
    text_widget.event_generate("<<Cut>>")


def copy_text():
    text_widget.event_generate("<<Copy>>")

def paste_text():
    text_widget.event_generate("<<Paste>>")

root = tk.Tk()
root.title("Text Editor")

text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack(fill=tk.BOTH, expand=True)

#"Open File" button
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(side=tk.LEFT, padx=5, pady=5)

#"Save" button
save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack(side=tk.LEFT, padx=5, pady=5)

#"New" button 
new_button = tk.Button(root, text="New", command=new_file)
new_button.pack(side=tk.LEFT, padx=5, pady=5)

#"Cut" button
cut_button = tk.Button(root, text="Cut", command=cut_text)
cut_button.pack(side=tk.LEFT, padx=5, pady=5)

#"Copy" button
copy_button = tk.Button(root, text="Copy", command=copy_text)
copy_button.pack(side=tk.LEFT, padx=5, pady=5)

#"Paste" button 
paste_button = tk.Button(root, text="Paste", command=paste_text)
paste_button.pack(side=tk.LEFT, padx=5, pady=5)



root.mainloop()

