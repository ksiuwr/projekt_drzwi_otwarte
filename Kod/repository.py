import sqlite3
DATABASE_PATH = 'doors.db'


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def add_card(name, serial):
    query = '''
        INSERT INTO registeredCards(name, serial)
        VALUES (:name,:serial)
    '''
    connection = get_connection()
    cursor = connection.cursor()
    params = {
        'name': name,
        'serial': serial,
    }

    try:
        cursor.execute(query, params)
    except sqlite3.IntegrityError as e:
        print(e)
        return False
    connection.commit()
    connection.close()
    return True


def is_authorized(serial):
    query = '''
        SELECT count(*)
        FROM registeredCards
        WHERE serial=:serial
    '''
    connection = get_connection()
    cursor = connection.cursor()
    params = {
        'serial': serial,
    }
    cursor.execute(query, params)
    count_of_serials = cursor.fetchone()
    connection.close()
    return count_of_serials[0] == 1


def update_last_used(serial):
    query = '''
        UPDATE registeredCards
        SET last_used = datetime('now','localtime')
        WHERE serial=:serial
    '''
    connection = get_connection()
    cursor = connection.cursor()
    params = {
        'serial': serial,
    }
    cursor.execute(query, params)
    connection.commit()
    connection.close()
    return True
    