import sqlite3
DATABASE_PATH = 'doors.db'
TABLE_NAME = 'registeredCards'

def getConnection():
    return sqlite3.connect(DATABASE_PATH)

def executeSql(query, params):
    connection = getConnection()
    cursor = connection.cursor()

    cursor.execute(query, params)
    connection.commit()
    connection.close()
    return True

def addCard(name, serial):
    query = f'''
        INSERT INTO {TABLE_NAME}(name, serial) 
        VALUES (:name,:serial)
    '''
    connection = getConnection()
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

def checkCard(serial):
    query = f'''
        SELECT count(*)
        FROM {TABLE_NAME}
        WHERE serial=:serial
    '''
    connection = getConnection()
    cursor = connection.cursor()
    params = {
        'serial': serial,
    }
    cursor.execute(query, params)
    count_of_serials = cursor.fetchone()
    connection.close()
    return count_of_serials[0] == 1
