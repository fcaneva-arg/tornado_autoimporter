import inspect
from os.path import join, relpath, abspath, splitext, sep
import sys

import tornado.ioloop
import tornado.web

from regen_handlers import regen_handlers
regen_handlers()
from handlers import *


def load_handlers():
    def make_url_path(class_path):
        # Get the path of the python file, relative to the handlers folder,
        # and stripping the '.py'
        class_rel_path = splitext(relpath(class_path, abspath('handlers')))[0]
        # In the case the index file is present, drop the 'index' name
        if class_rel_path.endswith('index'):
            class_rel_path = class_rel_path[:class_rel_path.rfind('index')]
        # Return the new path, prepending the slash, and replacing all directory
        # separators by slashes (useful if slashes are not directory separators
        # (e.g. in Windows)
        return join('/', class_rel_path.replace(sep, '/'))

    # Find all classes imported
    clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    # Return a list with all subclasses of Request handler with its correct web path
    return [
        (make_url_path(inspect.getfile(c[1])), c[1])
        for c in clsmembers
        if issubclass(c[1], tornado.web.RequestHandler)
    ]


if __name__ == "__main__":
    app = tornado.web.Application(load_handlers())
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
