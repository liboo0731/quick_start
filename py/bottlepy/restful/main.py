
from bottle import Bottle

from utils import CONST_APP
from app01 import app01
from app02 import app02


root = Bottle()
root.mount(CONST_APP.PREFIX_APP01, app01.app)
root.mount(CONST_APP.PREFIX_APP02, app02.app)


if __name__ == '__main__':
    root.run(host='0.0.0.0', port='8080')
