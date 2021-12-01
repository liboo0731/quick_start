
import sqlite3


class DBTools:
    def __init__(self, database):
        self._connection = sqlite3.connect(database)

    @staticmethod
    def _dict_factory(cursor, row):
        d = dict()
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def get_tables(self):
        table_list = self.execute('select name from sqlite_master where type="table"', result_dict=False)
        return [x[0] for x in table_list if 'sqlite_sequence' not in x]

    def get_table_header(self, table_name):
        table_info = self.execute(f'pragma table_info({table_name})', result_dict=False)
        return [x[1] for x in table_info]

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
    import CONST_APP
    db = DBTools(CONST_APP.DATABASE)
    db.execute(CONST_APP.CREATE_DB_APP01)
    print(db.get_tables())
    print(db.get_table_header(CONST_APP.TABLE_NAME_APP01))
    db.execute(f'delete from {CONST_APP.TABLE_NAME_APP01} where name=?', ['name'])
    db.execute(f'insert into {CONST_APP.TABLE_NAME_APP01} (id, name, passwd) values (?,?,?)', [None, 'name', '123456'])
    print(db.execute(f'select * from {CONST_APP.TABLE_NAME_APP01}', result_dict=False))
    print(db.execute(f'select * from {CONST_APP.TABLE_NAME_APP01}'))
