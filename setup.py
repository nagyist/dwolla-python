from distutils.core import setup

setup(
    name='dwolla',
    version='2.0.0',
    packages=['dwolla'],
    install_requires=[
        'requests',
        'mock'
    ],
    url='http://developers.dwolla.com',
    license='MIT',
    author='Dwolla Inc, David Stancu',
    author_email='david@dwolla.com',
    description='An official requests based wrapper for the Dwolla API'
)
