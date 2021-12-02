
DATABASE = './db/app.db'

VERSION = 'v1'
SUB_URL = f'/{VERSION}/app'

PREFIX_APP01 = 'app01'
TABLE_NAME_APP01 = 'app01'
CREATE_DB_APP01 = f'''create table if not exists {TABLE_NAME_APP01}(
id integer primary key autoincrement,
name text unique not null,
passwd text not null);'''
