import json

import web

urls = (
    '/list', 'TestList',
    '/base', 'TestBase',
)
app_demo = web.application(urls, globals())


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

    def POST(self):
        return

    def DELETE(self):
        return 
