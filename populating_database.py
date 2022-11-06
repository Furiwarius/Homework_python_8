"""
Модуль необходим, если необходимо заполнить таблицы
со статичными значениями в случаее пересоздания БД

"""

import sqlite3


def filling_table_job_title():
    # Заполнение данными таблицы job_title
    try:
        sqlite_connection = sqlite3.connect('Database\sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        table_with_param = """INSERT INTO job_title
                                  (id, title, salary)
                                  VALUES (?, ?, ?);"""

        positions = {'Стажер': 30000, 'Тестировщик':50000, 'Системный администратор':60000, 'Frontend-разработчик':70000, 
                     'Backend-разработчик':70000, 'Fullstack-разработчик':80000, 'DevOps-инженер':90000,
                     'Системный аналитик':95000, 'Data Engineer':100000, 'Data Analyst':110000, 'Data Scientist':120000, 'ML-инженер':120000}                          
        values = [(i, val, positions[val]) for i, val in enumerate(positions,1)]      
        
        cursor.executemany(table_with_param, values) 
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу job_title")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def filling_table_family_status():
    # Заполнение данными таблицы family_status
    try:
        sqlite_connection = sqlite3.connect('Database\sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        table_with_param = """INSERT INTO family_status
                                  (id, status)
                                  VALUES (?, ?);"""
                       
        values = [(1, 'Холост'),(2, 'Состоит в браке'),(3 , 'Разведен')]       
        cursor.executemany(table_with_param, values) 
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу family_status")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def filling_table_emplouyment():
    # Заполнение данными таблицы employment
    try:
        sqlite_connection = sqlite3.connect('Database\sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        table_with_param = """INSERT INTO type_employment
                                  (id, type_contract)
                                  VALUES (?, ?);"""
                       
        values = [(1, 'Бессрочный договор'), (2, 'Срочный договор')]       
        cursor.executemany(table_with_param, values) 
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу employment")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")





filling_table_emplouyment()
filling_table_family_status()
filling_table_job_title()     
