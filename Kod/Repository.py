import sqlite3


class Repository:
    def __init__(self, path):
        self.path = path
        self.db = sqlite3.connect(path)

    def add_card(self, name, serial):
        query = '''
            INSERT INTO registeredCards(name, serial)
            VALUES (:name,:serial)
        '''
        params = {
            'name': name,
            'serial': serial,
        }
        try:
            with self.db as con:
                con.execute(query, params)
                return True
        except sqlite3.IntegrityError:
            return False

    def is_authorized(self, serial):
        query = '''
            SELECT count(*)
            FROM registeredCards
            WHERE serial=:serial
        '''
        params = {
            'serial': serial,
        }
        cursor = self.db.execute(query, params)
        count_of_serials = cursor.fetchone()
        return count_of_serials[0] > 0

    def update_last_used(self, serial):
        query = '''
            UPDATE registeredCards
            SET last_used = datetime('now','localtime')
            WHERE serial=:serial
        '''
        params = {
            'serial': serial,
        }
        with self.db as con:
            con.execute(query, params)

    def log_message(self, msg_type, message):
        types = ['add', 'open', 'reject', 'error']

        query = '''
            INSERT INTO logs(type, message)
            VALUES (:type,:message)
        '''
        params = {
            'type': msg_type if msg_type in types else 'unknown',
            'message': message,
        }
        with self.db as con:
            con.execute(query, params)

    def get_name(self, serial):
        query = '''
            SELECT name
            FROM registeredCards
            WHERE serial=:serial
        '''
        params = {
            'serial': serial,
        }
        cursor = self.db.execute(query, params)
        name = cursor.fetchone()
        return name[0]

    def disconnect(self):
        self.db.close()


class TerminalOutput:
    def log_message(self, msg_type, message):
        print("%s: %s" % (msg_type, message))


class Logger:
    def __init__(self, output):
        self.output = output

    def add(self, message):
        self.output.log_message('add', message)

    def open(self, message):
        self.output.log_message('open', message)

    def reject(self, message):
        self.output.log_message('reject', message)

    def error(self, message):
        self.output.log_message('error', message)
