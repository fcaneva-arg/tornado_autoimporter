Tornado Auto-importer
=====================

About
-----

This project shows how to create an [Tornado](https://www.tornadoweb.org/en/stable/) automatic handler importer.
It was inspired by how [Nuxt.js](https://nuxtjs.org/) imports [Vue.js](https://vuejs.org) pages from a
given directory tree, and serves them automagically. This creates a flexible Web API where refactoring of routes
can be as easy as adding/moving/renaming/deleting files. The only restriction is that there must be only one class per file.

_Warning:_ this project is not intended to be a library. Rather than that, it is like a template
to show up how auto loading of handlers can be pefromed without manual updating; just by looking up
Python files inside a given folder tree, importing the classes and converting the file path into its
correspoding URL.

How it works
------------

The library works in two phases:
1. The first phase (`regen_handlers()`) traverses the `handlers` directory and:
   1. Deletes the `__pycache__` directories
   2. Recreates the `__init__.py` file by adding all Python files at current level
   3. Adds to `__init__.py` the subfolders at current level which contains Python files
  
   After all `__init__.py` files are regnerated, `from handlers import *` is executed, 
   gathering all the files contained at the package.

2. The second phase (`load_handlers()`) works by scanning all classes that are subclass of 
`tornado.web.RequestHandler`. Since in Python all classes have stored their origin file, it's relatively easy to get
the relative path from the `handlers` folder. Once we get this relative path, we strip out the `.py` extension and, 
if the name is exactly `index`, we remove it as well. Finally, we make a list of tuples required for the
`tornado.web.Application` class (in order: path, handler class, and `kwargs = {}`) and return it.

Notice that `regen_handlers` can be also run apart from the `main` application.

How to try it
-------------

1. Install Python (3.5.2 or newer, as required by Tornado 6.0+).
2. Install Tornado 6.0.
3. Clone this repo.
4. Add/modify/move/rename handlers (_to taste_).
5. Run the `main.py` file, then run your Web browser at `localhost:8888`.
6. Tinker around with the paths, play with different combinations of URLs.
