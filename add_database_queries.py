import sqlite3

import datetime


def finding_id(cursor, table, desired=0, quest=0):
    if desired==0:
        search_id = f"""select id from {table}"""
        cursor.execute(search_id)
        id_list = cursor.fetchall()
        if len(id_list)==0:
            new_id = 1
        else:
            new_id = max(id_list)[0]+1
        return new_id
    else:
        search_id = f"""select id from {table} where {desired}='{quest}'"""
        cursor.execute(search_id)
        desired_id = cursor.fetchall()[0][0]
        return desired_id


def adding_address(cursor, sqlite_connection, data_dict, worker_id):
    # добавление даннх в таблицу адреса
    try:
        filling_address_table = """INSERT INTO address_place_residense
                                    (id, worker_id, city, street, street_number, floor, 
                                    apartament_number, residence_status)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
        
        address_id = finding_id(cursor, "address_place_residense")
        data_tuple_address = (address_id , worker_id, data_dict['city'], data_dict['street'], 
                            int(data_dict['street_number']), int(data_dict['floor']), 
                            int(data_dict['apartament_number']), data_dict['residence_status'])
        
        cursor.execute(filling_address_table, data_tuple_address)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу address_place_residense")
        return address_id

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def adding_employce_documents(cursor, sqlite_connection, data_dict, worker_id):
    # добавление даннх в таблицу документы работника

    try:
        filling_documents_table = """INSERT INTO employce_documents
                                    (id, worker_id, passport_number, passport_series, 
                                    snils, issued_by)
                                    VALUES (?, ?, ?, ?, ?, ?);"""
        
        documents_id = finding_id(cursor, "employce_documents")
        data_tuple_address = (documents_id , worker_id, int(data_dict['passport_number']), 
                              int(data_dict['passport_series']), int(data_dict['snils']), data_dict['issued_by'])
        
        cursor.execute(filling_documents_table, data_tuple_address)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу employce_documents")
        return  documents_id

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def adding_phone_number(cursor, sqlite_connection, data_dict, worker_id):
    # добавление даннх в таблицу номеров

    try:
        filling_number_table = """INSERT INTO phone_numbers
                                    (id, worker_id, number, status)
                                    VALUES (?, ?, ?, ?);"""
        
        phone_id = finding_id(cursor, "phone_numbers")
        data_tuple_number = (phone_id , worker_id, int(data_dict['phone_number']), data_dict['number_status'])
        
        cursor.execute(filling_number_table, data_tuple_number)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу phone_numbers")
        return  phone_id

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def adding_worker(data_dict):
    # добавление нового работника в БД
    try:
        sqlite_connection = sqlite3.connect('Database\sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        new_id = finding_id(cursor, "general_information_employers")
        status_id = finding_id(cursor, "family_status" , desired='status' , quest=data_dict['family_status'])
        post_id = finding_id(cursor, "job_title", desired='title', quest=data_dict['post'])
        type_employment_id = finding_id(cursor, "type_employment", desired='type_contract', quest=data_dict['type_employment'])

        address_id = adding_address(cursor, sqlite_connection, data_dict, new_id)
        documents_id = adding_employce_documents(cursor, sqlite_connection, data_dict, new_id)
        adding_phone_number(cursor, sqlite_connection, data_dict, new_id)

        filling_main_table = """INSERT INTO general_information_employers
                                  (id, name, surname, patronymic, email, birthday, address_id, status_id, having_children, 
                                  documents_id, employment_date, date_dismissal, post_id, expeirience, type_employment_id, salary)
                                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

        data_tuple = (new_id, data_dict['name'], data_dict['surname'], data_dict['patronymic'], 
                      data_dict['email'], datetime.date(int(data_dict['year_birth']), 
                      int(data_dict['month_birth']), int(data_dict['day_birth'])), address_id, status_id, 
                      int(data_dict['having_children']), documents_id, datetime.datetime.now(), 
                      0, post_id, int(data_dict['expirience']), type_employment_id, int(data_dict['salary']))
        cursor.execute(filling_main_table, data_tuple) 

        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу general_information_employers")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
