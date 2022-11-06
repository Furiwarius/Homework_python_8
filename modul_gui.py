from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from add_tab import page_fill_add
from clicked_adding_data import adding_data

from one_tab import page_fill_one
from clicked_search_data import search_data


add_combobox_list, add_entry_list = [], []
one_label_list, one_entry_list = [], []


def clicked_add_tab(add_tab):
    global add_combobox_list, add_entry_list

    answer = adding_data(add_combobox_list, add_entry_list, add_tab)
    if answer == True:
        add_combobox_list, add_entry_list = page_fill_add(add_tab, add_entry_list, add_combobox_list)


def clicked_one_tab(one_tab):
    global one_label_list, one_entry_list
    answer = search_data(one_tab, one_entry_list)
    if answer == False:
        pass
    elif answer == True:
        pass


def interaction_interface():
    global add_combobox_list ,add_entry_list
    global one_label_list, one_entry_list

    window = Tk()  
    window.title("Information system")  
    window.geometry('800x500+500+300')  

    tab_control = ttk.Notebook(window)  
    find_tab = ttk.Frame(tab_control)  
    add_tab = ttk.Frame(tab_control)
    reference_tab = ttk.Frame(tab_control)  

    tab_control.add(find_tab, text='Найти')  
    tab_control.add(add_tab, text='Добавить')  
    tab_control.add(reference_tab, text='Справка')


    find_control = ttk.Notebook(find_tab)  
    one_tab = ttk.Frame(find_control)  
    some_tab = ttk.Frame(find_control)
    find_control.add(one_tab, text='Одного')  
    find_control.add(some_tab, text='Нескольких')
    find_control.pack(expand=3, fill='both')

    add_combobox_list, add_entry_list = page_fill_add(add_tab)
    add_tab_btn = Button(add_tab, text="Добавить", command=lambda: clicked_add_tab(add_tab))  
    add_tab_btn.grid(column=6, row=16, padx=1, pady=1)

    one_label_list, one_entry_list = page_fill_one(one_tab)
    one_tab_btn = Button(one_tab, text="Найти", command=lambda: clicked_one_tab(one_tab))  
    one_tab_btn.grid(column=6, row=3, padx=1, pady=1)

    new_fields = Label(reference_tab, text='Справочный материал')  
    new_fields.grid(column=0, row=0)


    tab_control.pack(expand=4, fill='both')  
    window.mainloop()
    
