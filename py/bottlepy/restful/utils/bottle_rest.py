
import json

from utils.bottle import request
from utils.bottle import response

from utils.model import DBTools


def result_data(data):
    return json.dumps({'code': response.status_code, 'data': data})


def bottle_rest(database, table_name, col_name, col_value):
    db = DBTools(database)
    table_header = db.get_table_header(table_name)
    data = list()
    if request.method == 'POST':
        input_data = list()
        if col_value:
            for col in table_header:
                if request.forms.get(col):
                    input_data.append(f'{col}="{request.forms.get(col)}"')
            if not input_data:
                return result_data(data)
            db.execute(f'update from {table_name} set {",".join(input_data)} where {col_name}=?', [col_value])
        else:
            for col in table_header:
                input_data.append(request.forms.get(col))
            print(input_data)
            print(f'insert from {table_name} values ({",".join(["?"] * len(table_header))})')
            db.execute(f'insert into {table_name} values ({",".join(["?"] * len(table_header))})', input_data)
    elif request.method == 'DELETE':
        db.execute(f'delete from {table_name} where {col_name}=?', [col_value])
    else:
        if col_value:
            data = db.execute(f'select * from {table_name} where {col_name}=?', [col_value])
        else:
            data = db.execute(f'select * from {table_name}')

    return result_data(data)
