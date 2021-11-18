import json

import web

urls = (
    '/', 'Index',
    '/list', 'TestList',
    '/base', 'TestBase',
    '/admin', 'Admin',
    '/add', 'Add'
)
app = web.application(urls, globals())
render = web.template.render('templates/', base='layout', globals={})


class Index:
    def GET(self):
        return render.index()


class TestList:
    def GET(self):
        data = {"data": [
            {
                "id": 1,
                "uiSref": "base",
                "imgUrl": "static/imgs/ts.jpg",
                "title": "基础模板",
                "content": "版块内容描述"
            },
            {
                "id": 2,
                "uiSref": "app",
                "imgUrl": "static/imgs//ts.jpg",
                "title": "APP应用",
                "content": "1"
            }]}
        return json.dumps(data)


class TestBase:
    def GET(self):
        data = {
            "title": "基础模板",
            "subtitle": "副标题！",
            "data": [
                {
                    "id": 1,
                    "name": "【分类】名称",
                    "num": 1,
                    "descr": "既然选择了远方，便只顾风雨兼程！",
                    "link": "https://liboo0731.github.io/"
                }]}
        return json.dumps(data)


class WebDB:
    def __init__(self):
        self.db = web.db.database(dbn='sqlite', db='hello.db')


class Admin(WebDB):
    def GET(self):
        todos = self.db.select('todos')
        data = [dict(x) for x in todos]
        return render.admin(data)


class Add(WebDB):
    def POST(self):
        i = web.input()
        print(i)
        try:
            self.db.insert('todos', name=i.name, title=i.title, num=i.num)
        except Exception as e:
            print(e)
        raise web.seeother('/admin')


if __name__ == "__main__":
    web.config.debug = False
    app.run()
