from distutils.core import setup
setup(name='pyglog',
      version='1.2',
      py_modules=['pyglog'],
      author="Jason Riesa",
      author_email="riesa@isi.edu",
      url="http://www.isi.edu/~riesa/software/pyglog",
      description="A logging facility for Python based on google-glog",
      license="GPL",
      package_data={'pyglog': ['COPYING']}
      )
