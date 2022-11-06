from tkinter import *
from tkinter import ttk

result_key=None


def clicked_choice(window, key):
    global result_key
    result_key=key
    window.destroy()



def dialog_window(dict_keys):
    global result_key
    dialogue = Tk()
    dialogue.title('Внимание')
    dialogue.geometry('400x200')
    inscription_1 = Label(dialogue, text="В результате поиска в системе \nпо этим данным было обнаружено несколько работников")
    inscription_1.pack(anchor='c')
    inscription_2 = Label(dialogue, text="Найденные данне по какому полю вывести?")
    inscription_2.pack(anchor='c')
 
    for key in enumerate(dict_keys):
        add_tab_btn = Button(dialogue, text=key, command=lambda: clicked_choice(dialogue, key))  
        add_tab_btn.pack(anchor='c')
    return result_key


def selection_data_display(data_dict):
    for key in data_dict:
        if data_dict[key]==None:
            data_dict.pop(key)
    else:
        if len(data_dict)!=1:
            data_dict = data_dict[dialog_window(list(data_dict.keys()))]
        else:
            data_dict = list(data_dict.values())[0][0]
    return data_dict


def showing_data(one_tab, data_dict):
    print(data_dict)
    languages = ["Pythfhdfhdfhdfhdfhhdfhdfhdfhon", "JavaScript", "C#", "Java", "C++", "Rust", "Kotlin", "Swift",
             "PHP", "Visual Basic.NET", "F#", "Ruby", "R", "Go", "C", 
             "T-SQL", "PL-SQL", "Typescript", "Assembly", "Fortran", "JavaScript", "C#", "Java", "C++", "Rust", "Kotlin", "Swift",
             "PHP", "Visual Basic.NET", "F#", "Ruby", "R", "Go", "C", 
             "T-SQL", "PL-SQL", "Typescript", "Assembly", "Fortran"]
    
    languages_var = StringVar(value=languages)
    listbox = Listbox(one_tab, listvariable=languages_var, width=80)
    listbox.grid(column=0, row=5, columnspan=4)

    listbox.yview_scroll(number=1, what="units")

