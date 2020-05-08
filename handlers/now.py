import datetime
import tornado.web


class NowHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
