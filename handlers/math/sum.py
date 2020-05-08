import tornado.web


class SumHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("2+2={}".format(2+2))
