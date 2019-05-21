import sqlite3
DATABASE_PATH = 'doors.db'


def get_connection():
    # type: () -> sqlite3.Connection
    return sqlite3.connect(DATABASE_PATH)


def add_card(name, serial):
    # type: (str, str) -> bool
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
        log_message("error", e)
        return False

    connection.commit()
    connection.close()

    return True


def is_authorized(serial):
    # type: (str) -> bool
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
    # type: (str) -> bool
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


def log_message(type, message):
    # type: (str, str) -> bool
    types = ['add', 'open', 'reject', 'error']

    query = '''
        INSERT INTO logs(type, message)
        VALUES (:type,:message)
    '''
    connection = get_connection()
    cursor = connection.cursor()
    params = {
        'type': type if type in types else 'unknown',
        'message': message,
    }

    cursor.execute(query, params)
    connection.commit()
    connection.close()

    return True


def get_name(serial):
    # type: (str) -> str
    query = '''
        SELECT name
        FROM registeredCards
        WHERE serial=:serial
    '''

    connection = get_connection()
    cursor = connection.cursor()
    params = {
        'serial': serial,
    }

    cursor.execute(query, params)
    name = cursor.fetchone()
    connection.close()
    return name[0]
