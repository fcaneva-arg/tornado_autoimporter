from glob import glob
from os import walk
from os.path import join, relpath, splitext
import shutil


def regen_handlers(log=False):
    for cwd, dirs, files in walk('handlers'):
        if log:
            print('Scanning {}'.format(relpath(cwd, 'handlers')))
        files = list(filter(lambda f: splitext(f)[0] != '__init__', files))
        if '__pycache__' in dirs:
            shutil.rmtree(join(cwd, '__pycache__'), ignore_errors=True)
        with open(join(cwd, '__init__.py'), 'w', encoding='utf8') as init_file:
            init_file.write('#!/usr/bin/env python3\n')
            init_file.write('#\n')
            init_file.write('# Auto-generated file made by regen_handlers\n')
            init_file.write('# All modifications will be lost on next server restart\n')
            init_file.write('#\n')
            for f in files:
                f_name, f_ext = splitext(f)
                if f_ext == '.py':
                    init_file.write('from .{} import *\n'.format(f_name))
            init_file.write('\n')
            for d in dirs:
                if glob('{}/{}/*.py'.format(cwd, d)):
                    init_file.write('from .{} import *\n'.format(d))
            


if __name__ == '__main__':
    regen_handlers(True)
