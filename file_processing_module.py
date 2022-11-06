from tkinter import filedialog
 

def save_file(save_data):
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        with open(f"{filepath}.txt", "w") as file:
            for text in save_data:
                file.write(f"{text}\n")