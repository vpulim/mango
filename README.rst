Installation
============

Make sure you have the latest version of pymongo_ installed.

.. _pymongo: http://api.mongodb.org/python

To install mango::

   sudo python setup.py install

Usage
=====
To use mango with your Django project, just add these lines to your settings.py file::

   SESSION_ENGINE = 'mango.session'
   AUTHENTICATION_BACKENDS = ('mango.auth.Backend',)
   MONGODB_HOST = 'localhost'  # enter your MongoDB hostname here
   MONGODB_PORT = None         # enter your MongoDB port here (None for default port)
   MONGODB_NAME = 'mydb'       # enter your MongoDB database name here

Also, make sure 'MIDDLEWARE_CLASSES' contains the session and authentication middleware classes::

   MIDDLEWARE_CLASSES = (
      ...
      'django.contrib.sessions.middleware.SessionMiddleware'
      'django.contrib.auth.middleware.AuthenticationMiddleware'
      ...
   )
