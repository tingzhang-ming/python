from distutils.core import setup, Extension
setup(name='clame',
      version='1.0',
      ext_modules=[Extension('clame',
                             sources=['clame.c'],
                             include_dirs=['/usr/include/python2.7/',
                                           '/usr/local/include/lame/'],
                             libraries=['mp3lame'],
                             library_dirs=['/usr/local/lib'])])

