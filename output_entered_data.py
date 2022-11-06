from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo

result_key=None          # результирующий ключ
dialog_box_state = False # состояние окна диалога

def clicked_choice(window, key):
    global result_key, dialog_box_state
    result_key=key
    dialog_box_state=False
    window.destroy()



def dialog_window(dict_keys):
    global result_key, dialog_box_state
    dialog_box_state=True
    dialogue = Tk()
    dialogue.title('Внимание')
    dialogue.geometry('400x200')
    inscription_1 = Label(dialogue, text="В результате поиска в системе \nпо этим данным было обнаружено несколько работников")
    inscription_1.pack(anchor='c')
    inscription_2 = Label(dialogue, text="Найденные данне по какому полю вывести?")
    inscription_2.pack(anchor='c')
 
    for key in dict_keys:
        add_tab_btn = Button(dialogue, text=key, command=lambda: clicked_choice(dialogue, key))  
        add_tab_btn.pack(anchor='c')
    while True:
        if dialog_box_state==False:
            return result_key


def selection_data_display(data_dict):
    global dialog_box_state
    result_data_dict={}
    for key in data_dict:
        if data_dict[key]!=None:
            result_data_dict[key] = data_dict[key]
    if len(result_data_dict)>1:
        result_key = dialog_window(list(data_dict.keys()))
        result_data_dict = result_data_dict[result_key]
    elif len(result_data_dict)==0:
        showwarning(title="Внимание", message="Такого работника нет")
        return -1
    return list(result_data_dict.values())[0]


def creating_output_list(data_dict):
    output_list = ["Личные данные работника",
                   f"Имя: {data_dict['worker'][0][1]}", f"Фамилия: {data_dict['worker'][0][2]}", f"Отчество: {data_dict['worker'][0][3]}", 
                   f"Дата рождения: {data_dict['worker'][0][5]}", f"Семейное положение: {data_dict['family_status'][0][0]}", 
                   f"Количество детей: {data_dict['worker'][0][6]}", 
                   "Контакты",
                   f"Почта: {data_dict['worker'][0][4]}", f"Номер телефона: {data_dict['phone'][0][0]}", 
                   f"Статус номера: {data_dict['phone'][0][1]}", 
                   "Рабочие данные",
                   f"Должность: {data_dict['post'][0][0]}", f"Опыт работы: {data_dict['worker'][0][-2]}", 
                   f"Дата устройства: {data_dict['worker'][0][-4]}", f"Дата увольнения: {data_dict['worker'][0][-3]}", 
                   f"Тип трудоустройства: {data_dict['type_contract'][0][0]}", f"Зарплата: {data_dict['worker'][0][-1]}", 
                   "Адрес", 
                   f"Город: {data_dict['address'][0][0]}", f"Улица: {data_dict['address'][0][1]}", 
                   f"Номер улицы: {data_dict['address'][0][2]}", f"Этаж: {data_dict['address'][0][3]}", 
                   f"Номер квартиры: {data_dict['address'][0][4]}", f"Статус жилья: {data_dict['address'][0][-1]}", 
                   "Доккументы работника", 
                   f"Номер паспорта: {data_dict['documents'][0][0]}", f"Серия паспорта: {data_dict['documents'][0][1]}", 
                   f"Кем выдан: {data_dict['documents'][0][3]}", f"Номер снилс: {data_dict['documents'][0][2]}"]
    
    return output_list


def showing_data(one_tab, data_dict):
    data_dict=selection_data_display(data_dict)
    if data_dict!=-1:
        output_data = creating_output_list(data_dict)
        
        languages_var = StringVar(value=output_data)
        listbox = Listbox(one_tab, listvariable=languages_var, width=80, height=14)
        listbox.grid(column=0, row=5, columnspan=4)

        listbox.yview_scroll(number=1, what="units")

