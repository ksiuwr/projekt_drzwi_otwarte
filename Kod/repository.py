import sqlite3
DATABASE_PATH = 'cards.db'
TABLE_NAME = 'registeredCards'

def getCursor():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

def addCard(name, serial):
    query = f'INSERT INTO {TABLE_NAME}(name, serial) VALUES (?,?)'
    result = cursor.execute(query, name, serial)

    return ''


def checkCard(serial):
    return True