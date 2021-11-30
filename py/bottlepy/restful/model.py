
import sqlite3


class AppDB:
    def __init__(self, database):
        self._connection = sqlite3.connect(database)

    @staticmethod
    def _dict_factory(cursor, row):
        d = dict()
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def execute(self, sql, args=None, result_dict=True, commit=True):
        if args is None:
            args = list()

        if result_dict:
            self._connection.row_factory = self._dict_factory
        else:
            self._connection.row_factory = None
        _cursor = self._connection.cursor()
        _cursor.execute(sql, args)
        if commit:
            self._connection.commit()
        data = _cursor.fetchall()
        _cursor.close()
        return data


if __name__ == '__main__':
    db = AppDB('app.db')
    db.execute('''CREATE TABLE IF NOT EXISTS APP(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NAME TEXT UNIQUE NOT NULL,
PASSWD TEXT NOT NULL);''')
    db.execute('delete from app where name=?', ['name'])
    db.execute('insert into app(id, name, passwd) values (?,?,?)', [None, 'name', '123456'])
    print(db.execute('select * from app', result_dict=False))
    print(db.execute('select * from app'))
