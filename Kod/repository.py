import sqlite3


class Repository:
    DATABASE_PATH = 'doors.db'

    @staticmethod
    def get_connection():
        # type: () -> sqlite3.Connection
        return sqlite3.connect(Repository.DATABASE_PATH)

    @staticmethod
    def add_card(name, serial):
        # type: (str, str) -> bool
        query = '''
            INSERT INTO registeredCards(name, serial)
            VALUES (:name,:serial)
        '''
        connection = Repository.get_connection()
        cursor = connection.cursor()
        params = {
            'name': name,
            'serial': serial,
        }

        try:
            cursor.execute(query, params)
            connection.commit()
            connection.close()
            return True
        except sqlite3.IntegrityError as e:
            connection.rollback()
            connection.close()
            Repository.log_message(
                'error',
                'sqlite3.IntegrityError: ' + str(e))
            return False

    @staticmethod
    def is_authorized(serial):
        # type: (str) -> bool
        query = '''
            SELECT count(*)
            FROM registeredCards
            WHERE serial=:serial
        '''

        connection = Repository.get_connection()
        cursor = connection.cursor()
        params = {
            'serial': serial,
        }

        cursor.execute(query, params)
        count_of_serials = cursor.fetchone()
        connection.close()

        return count_of_serials[0] == 1

    @staticmethod
    def update_last_used(serial):
        # type: (str) -> bool
        query = '''
            UPDATE registeredCards
            SET last_used = datetime('now','localtime')
            WHERE serial=:serial
        '''

        connection = Repository.get_connection()
        cursor = connection.cursor()
        params = {
            'serial': serial,
        }

        cursor.execute(query, params)
        connection.commit()
        connection.close()

        return True

    @staticmethod
    def log_message(msg_type, message):
        # type: (str, str) -> bool
        types = ['add', 'open', 'reject', 'error']

        query = '''
            INSERT INTO logs(type, message)
            VALUES (:type,:message)
        '''
        connection = Repository.get_connection()
        cursor = connection.cursor()
        params = {
            'type': msg_type if msg_type in types else 'unknown',
            'message': message,
        }

        cursor.execute(query, params)
        connection.commit()
        connection.close()

        return True

    @staticmethod
    def get_name(serial):
        # type: (str) -> str
        query = '''
            SELECT name
            FROM registeredCards
            WHERE serial=:serial
        '''

        connection = Repository.get_connection()
        cursor = connection.cursor()
        params = {
            'serial': serial,
        }

        cursor.execute(query, params)
        name = cursor.fetchone()
        connection.close()

        return name[0]
