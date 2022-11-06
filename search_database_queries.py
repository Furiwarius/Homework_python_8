import sqlite3


def data_formation(cursor, received_id): 

    requests = [f"""SELECT id, name, surname, patronymic, email, 
               birthday, having_children, employment_date,
               date_dismissal, expeirience, salary 
               FROM general_information_employers WHERE id = '{received_id}'""", 
               f"""SELECT city, street, street_number, floor, 
               apartament_number, residence_status 
               FROM address_place_residense WHERE worker_id = '{received_id}'""", 
               f"""SELECT passport_number, passport_series,
               snils, issued_by FROM employce_documents WHERE worker_id = '{received_id}'""", 
               f"""SELECT number, status FROM phone_numbers WHERE worker_id = '{received_id}'""",
               f"""SELECT status FROM family_status
               WHERE id = (SELECT status_id FROM general_information_employers WHERE id = '{received_id}')""",
               f"""SELECT title FROM job_title WHERE 
               id = (SELECT post_id FROM general_information_employers WHERE id = '{received_id}')""",
               f"""SELECT type_contract FROM type_employment 
               WHERE id = (SELECT type_employment_id 
               FROM general_information_employers WHERE id = '{received_id}')"""
               ]
    data_dict = {'worker':None, 'address':None, 'documents':None,
                 'phone':None, 'family_status':None, 'post':None,
                 'type_contract':None}

    for req, key in zip(requests, data_dict):
        cursor.execute(req)
        data_dict[key] = cursor.fetchall()
    
    return data_dict


def search_worker(entry_value):
    # поиск работника в БД
    records_dict = {'full_name': None, 'number': None, 'email': None}
    try:
        sqlite_connection = sqlite3.connect('Database\sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        if entry_value['surname_name_patronymic']!='':
            # если нужно искать по ФИО
            worker_name = entry_value['surname_name_patronymic'].split()
            if len(worker_name)==3:
                name_query = f"""SELECT id from general_information_employers where surname = 
                              '{worker_name[0]}' and name = '{worker_name[1]}' and patronymic = '{worker_name[2]}'"""
                cursor.execute(name_query)
                data_return = cursor.fetchall()
                if data_return!=[]:
                    records_dict['full_name'] = data_formation(cursor, data_return[0][0])
                else:
                    print('В БД таких данных нет')
            else:
                print('данные должны вводится через пробел Ф И О')

        if entry_value['phone_number']!='':
            # если нужно искать по номеру телефона
            number_query = f"""SELECT worker_id from phone_numbers where number = '{entry_value['phone_number']}'"""
            cursor.execute(number_query)
            data_return = cursor.fetchall()
            if data_return!=[]:
                records_dict['number'] = data_formation(cursor, data_return[0][0])
            else:
                print("В БД накого номера нет")

        if entry_value['email']!='':
            # если нужно искать по email
            email_query = f"""SELECT id from general_information_employers where email = '{entry_value['email']}'"""
            cursor.execute(email_query)
            data_return = cursor.fetchall()
            if data_return!=[]:
                records_dict['email'] = data_formation(cursor, data_return[0][0])
            else:
                print("В БД такого email нет")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
            return records_dict