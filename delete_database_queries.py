import sqlite3


def delete_worker(id):
    try:
        sqlite_connection = sqlite3.connect('Database\sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_delete_query = [f"""DELETE from general_information_employers where id = '{id}'""",
                            f"""DELETE from phone_numbers where worker_id = '{id}'""",
                            f"""DELETE from address_place_residense where worker_id = '{id}'""",
                            f"""DELETE from employce_documents where worker_id = '{id}'"""]
        for query in sql_delete_query:
            cursor.execute(query)    
            sqlite_connection.commit()

        print("Запись успешно удалена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")