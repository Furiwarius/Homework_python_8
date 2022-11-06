from tkinter import *
from tkinter.ttk import Combobox  
from tkinter import ttk

def page_fill_add(add_tab, entry_list=[], combobox_list=[]):
    # создание бланка для заполнения
    if entry_list and combobox_list != []:
        for vidget in entry_list:
            vidget.destroy()
        for vidget in combobox_list:
            vidget.destroy()
    combobox_position = {'Семейное положение:': [[0, 6], ['Холост', 'Состоит в браке', 'Разведен']], 
                         'Статус жилья:': [[0, 9], ['Постоянное', 'Временное']], 
                         'Статус номера:': [[3, 10], ['Личный', 'Рабочий', 'Запасной']], 
                         'Вид трудового договора:': [[0, 12], ['Бессрочный договор', 'Срочный договор']], 
                         'Должность:': [[0, 13], ['Стажер', 'Тестировщик', 'Системный администратор', 
                         'Frontend-разработчик', 'Backend-разработчик', 'DevOps-инженер', 
                         'Системный аналитик', 'Data Engineer', 'Data Analyst', 
                         'Data Scientist', 'ML-инженер']]}

    entry_position = {'Имя:': [0, 2], 'Фамилия:': [3, 2], 'Отчество:': [5, 2], 
                      'Год рождения:': [0, 3], 'Месяц рождения:': [3, 3],
                      'День рождения:': [5, 3], 'Номер паспорта:': [0, 4], 
                      'Серия паспорта:': [3, 4], 'Снилс:': [0, 5], 'Кем выдан:': [3, 5], 
                      'Дети:': [3, 6], 'Город:': [0, 7], 'Улица:': [3, 7], 
                      'Номер улицы:': [5, 7], 'Этаж:': [0, 8], 'Номер квартиры:': [3, 8], 
                      'Номер телефона:': [0, 10], 'Ел. почта:': [0, 11], 
                      'Зарплата:': [3, 13], 'Опыт работы:': [0, 14]}
    
    frame = ttk.Frame(add_tab, borderwidth=1, relief=SOLID, padding=[8, 10])
    fill_fields = Label(add_tab, text='Заполните поля', font=('Calibri', 12), relief="flat")  
    fill_fields.grid(row=0, column=0, ipadx=20, ipady=3, padx=1, pady=1)
    frame.grid(row=0, column=0, padx=5, pady=5)

    combobox_list=[]
    for key in combobox_position:
        new_label = Label(add_tab, text=key, justify=RIGHT)
        new_label.grid(column=combobox_position[key][0][0], row=combobox_position[key][0][1])
        combo = Combobox(add_tab)  
        combo['values'] = combobox_position[key][1]  
        combo.current(0)
        combo.grid(column=combobox_position[key][0][0]+1, row=combobox_position[key][0][1]) 
        combobox_list.append(combo)

    for key in entry_position:
        new_label = Label(add_tab, text=key, justify=RIGHT)
        new_label.grid(column=entry_position[key][0], row=entry_position[key][1], padx=1, pady=1)
    entry_list = []
    for i, key in enumerate(entry_position):
        entry_list.append(Entry(add_tab,width=20))
        entry_list[i].grid(column=entry_position[key][0]+1, row=entry_position[key][1])

    info_fields = Label(add_tab, text='Для добавления в базу данных все поля дожны быть заполнены', font=('Calibri', 12), relief="flat")  
    info_fields.grid(row=16, column=0, columnspan=5, ipadx=20, ipady=3, padx=1, pady=1)     
    
    return combobox_list, entry_list