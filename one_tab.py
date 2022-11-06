from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def page_fill_one(one_tab):
    direction_1 = Label(one_tab, text= 'Введите данные для поиска.\nПоиск можно производить по ФИО, номеру телефона или email.',
                        font=('Calibri', 12), relief="flat")
    direction_1.grid(row=0, column=0, columnspan=4, ipadx=20, ipady=3, padx=2, pady=2)

    vidget_position = {'Фамилия Имя Отчество:': [1, 0], 
                      'Номер телефона:': [2, 0], 'Ел. почта:': [3, 0]}
    
    help_text = Label(one_tab, text='Вводить ФИО необходимо через пробел')
    help_text.grid(row=1, column=3, padx=1, pady=1)

    label_list=[]
    for i, key in enumerate(vidget_position):
        label_list.append(Label(one_tab, text=key, justify=RIGHT))
        label_list[i].grid(row=vidget_position[key][0], column=vidget_position[key][1], padx=1, pady=1)

    entry_list = []
    for i, key in enumerate(vidget_position):
        entry_list.append(Entry(one_tab, width=30))
        entry_list[i].grid(row=vidget_position[key][0], column=vidget_position[key][1]+1)  
          
    return label_list, entry_list