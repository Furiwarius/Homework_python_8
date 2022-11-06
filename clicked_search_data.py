from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from search_database_queries import search_worker
from output_entered_data import showing_data


def search_data(one_tab, entry_list):
    entry_value = {'surname_name_patronymic': '',
                  'phone_number': '', 'email': ''}
    for i, key in enumerate(entry_value):
        entry_value[key] = entry_list[i].get()
    
    for key in entry_value:
        if entry_value[key] !='':
            data_dict = search_worker(entry_value)
            # records_dict = {'full_name': None, 'number': None, 'email': None}  
            # добавить выбор выводимых значений при различных полученных данных по поисковым значениям
            showing_data(one_tab, data_dict)

            break
    else:
        messagebox.showerror('Неверно', 'Для поиска необходимо заполнить хотя бы одно поле')
        return False        
    