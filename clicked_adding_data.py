from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from add_database_queries import adding_worker
from add_tab import page_fill_add


def adding_data(combobox_list, entry_list, add_tab):
    # проверка бланка на полное заполнение
    combobox_name = {'family_status': '', 'residence_status': '', 'number_status': '', 
                     'type_employment': '', 'post': ''}
    entry_name = {'name': '', 'surname': '', 'patronymic': '', 
                      'year_birth': '', 'month_birth': '',
                      'day_birth': '', 'passport_number': '', 
                      'passport_series': '', 'snils': '', 'issued_by': '', 
                      'having_children': '', 'city': '', 'street': '', 
                      'street_number': '', 'floor': '', 'apartament_number': '', 
                      'phone_number': '', 'email': '', 
                      'salary': '', 'expirience': ''}
                      
    check_list = []
    for obj in entry_list:
        if obj.get()=='':
            obj.configure(background="lightcoral")
        check_list.append(obj.get())
    if '' in check_list:
        messagebox.showerror('Неверно', 'Для добавления в базу данных необходимо заполнить все поля')
        return False
    else:
        entry_dict = {key:check_list[i] for i, key in enumerate(entry_name)}
        combobox_dict = {key:combobox_list[i].get() for i, key in enumerate(combobox_name)}
        data_dict = entry_dict|combobox_dict
        print(data_dict)
        adding_worker(data_dict)
        messagebox.showinfo('Успешно', 'Запись добавлена')
        return True