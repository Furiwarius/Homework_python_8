'''
Создание бд и таблиц 

'''

import sqlite3

try:
    sqlite_connection = sqlite3.connect('Database\sqlite_python.db')
    #----------------------------------
    # запрос для создания таблицы
    general_information_employers = '''CREATE TABLE general_information_employers (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                surname TEXT NOT NULL,
                                patronymic TEXT NOT NULL,
                                email text NOT NULL UNIQUE,
                                birthday datetime NOT NULL,
                                address_id INTEGER NOT NULL,
                                status_id INTEGER NOT NULL,
                                having_children INTEGER,
                                documents_id INTEGER,
                                employment_date date,
                                date_dismissal date,
                                post_id INTEGER NOT NULL,
                                expeirience INTEGER, 
                                type_employment_id INTEGER NOT NULL,
                                salary REAL NOT NULL,
                                FOREIGN KEY (address_id) REFERENCES address_place_residense (id),
                                FOREIGN KEY (status_id) REFERENCES family_status (id),
                                FOREIGN KEY (documents_id) REFERENCES employce_documents (id),
                                FOREIGN KEY (post_id) REFERENCES job_title (id),
                                FOREIGN KEY (type_employment_id) REFERENCES typetype_employment (id));'''

    phone_numbers = '''CREATE TABLE phone_numbers (
                    id INTEGER PRIMARY KEY,
                    worker_id INTEGER NOT NULL,
                    number INTEGER NOT NULL,
                    status TEXT,
                    FOREIGN KEY (worker_id)  REFERENCES general_information_employers (id));'''

    job_title = '''CREATE TABLE job_title (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    salary REAL NOT NULL);'''

    family_status = '''CREATE TABLE family_status (
                    id INTEGER PRIMARY KEY,
                    status TEXT NOT NULL);'''   

    type_employment = '''CREATE TABLE type_employment (
                    id INTEGER PRIMARY KEY,
                    type_contract TEXT NOT NULL);'''   

    address_place_residense = '''CREATE TABLE address_place_residense (
                                id INTEGER PRIMARY KEY,
                                worker_id INTEGER NOT NULL,
                                city TEXT NOT NULL,
                                street TEXT NOT NULL,
                                street_number INTEGER NOT NULL,
                                floor INTEGER,
                                apartament_number INTEGER,
                                residence_status TEXT,
                                FOREIGN KEY (worker_id)  REFERENCES general_information_employers (id));''' 

    employce_documents = '''CREATE TABLE employce_documents (
                            id INTEGER PRIMARY KEY,
                            worker_id INTEGER NOT NULL,
                            passport_number INTEGER NOT NULL,
                            passport_series INTEGER NOTT NULL,
                            snils INTEGER NOT NULL,  
                            issued_by TEXT NOT NULL,
                            FOREIGN KEY (worker_id)  REFERENCES general_information_employers (id));'''  
    #----------------------------------


    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    # создание таблицы
    cursor.execute(general_information_employers)
    cursor.execute(job_title)
    cursor.execute(phone_numbers)
    cursor.execute(family_status)
    cursor.execute(type_employment)
    cursor.execute(address_place_residense)
    cursor.execute(employce_documents)
    sqlite_connection.commit()
    print("Таблица SQLite создана")
    
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")