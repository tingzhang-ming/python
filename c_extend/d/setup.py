from distutils.core import setup, Extension
setup(name='pylame',
      version='1.0',
      ext_modules=[Extension('pylame',
                             sources=['lame_test.c', 'pylame.c'],
                             include_dirs=['/usr/include/python2.7/',
                                           '/usr/local/include/lame/'],
                             libraries=['mp3lame'],
                             library_dirs=['/usr/local/lib'])])

