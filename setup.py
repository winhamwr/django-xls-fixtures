import os
from distutils.core import setup
 
f = open('README.rst')
readme = f.read()
f.close()

def find_packages(root):
    # so we don't depend on setuptools; from the Storm ORM setup.py
    packages = []
    for directory, subdirectories, files in os.walk(root):
        if '__init__.py' in files:
            packages.append(directory.replace(os.sep, '.'))
    return packages
 
setup(
    name = 'django-xls-fixtures',
    version = '0.1dev',
    description = "Excel-based fixtures for Django that don't make you edit id's and that handle dependencies for you",
    long_description=readme,
    author = 'Wes Winham, Trey Peek',
    author_email = 'winhamwr@gmail.com',
    license = 'BSD',
    url = 'http://github.com/winhamwr/django-xls-fixtures/tree/master',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        ],
    packages = find_packages('xls_fixtures'),
    install_requires=['fixture', 'xlrd', 'django-fixtures'],
)
