
import json

from bottle import Bottle
from bottle import request
from bottle import response
from bottle import abort

from utils.model import DBTools
from utils import CONST_APP


app = Bottle()


def error_msg(code):
    return json.dumps({'code': code, 'data': []})


@app.error(404)
def err404(error):
    print(404)
    return error_msg(response.status_code)


@app.error(405)
def err405(error):
    return error_msg(response.status_code)


@app.error(500)
def err500(error):
    return error_msg(response.status_code)


@app.get(CONST_APP.SUB_URL)
@app.post(CONST_APP.SUB_URL)
@app.get(f'{CONST_APP.SUB_URL}/<id:int>')
@app.post(f'{CONST_APP.SUB_URL}/<id:int>')
@app.delete(f'{CONST_APP.SUB_URL}/<id:int>')
def app_restful(id=None):
    db = DBTools(CONST_APP.DATABASE)
    db.execute(CONST_APP.CREATE_DB_APP01)
    table_header = db.get_table_header(CONST_APP.TABLE_NAME_APP01)
    data = list()
    if request.method == 'POST':
        input_data = list()
        if id:
            for col in table_header:
                if request.forms.get(col):
                    input_data.append(f'{col}="{request.forms.get(col)}"')
            if not input_data:
                abort(500)
            db.execute(f'update from {CONST_APP.TABLE_NAME_APP01} set {",".join(input_data)} where id=?', [id])
        else:
            for col in table_header:
                input_data.append(request.forms.get(col))
            db.execute(f'insert from {CONST_APP.TABLE_NAME_APP01} values ({",".join(["?"]*len(table_header))})', input_data)
    elif request.method == 'DELETE':
        db.execute(f'delete from {CONST_APP.TABLE_NAME_APP01} where id=?', [id])
    else:
        if id:
            data = db.execute(f'select * from {CONST_APP.TABLE_NAME_APP01} where id=?', [id])
        else:
            data = db.execute(f'select * from {CONST_APP.TABLE_NAME_APP01}')

        if not data:
            abort(404)

    return json.dumps({'code': response.status_code, 'data': data})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
