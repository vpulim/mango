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
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      ...
   )

Django sessions should now work exactly as described in the Django sessions_ documentation.

.. _sessions: http://docs.djangoproject.com/en/dev/topics/http/sessions/

For the most part, Django authentication should also work as described in the Django authentication_ documentation.  However, since we no longer have Django's ORM model available, you can't use the User model described in the Django documentation to directly manipulate User objects.  Instead, mango provides its own User class that you should use instead.  All of Django's original User class instance methods are available in mango's User class (is_authenticated(), set_password(), check_password(), etc...).  However, there is longer a User.objects attribute.  Instead, many of the administrative function such as create_user() are now class methods of User.

.. _authentication: http://docs.djangoproject.com/en/dev/topics/auth/

For instance, to create a user::

   >>> from mango.auth import User
   >>> user = User.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
   
To find a user::

   >>> from mango.auth import User
   >>> user = User.get({'username': 'john'})

To modify a user's attributes::

   >>> from mango.auth import User
   >>> user = User.get({'username': 'john'})
   >>> user.first_name = 'John'
   >>> user.last_name = 'Lennon'
   >>> user.save()

To delete a user::
   
   >>> from mango.auth import User
   >>> user = User.get({'username': 'john'})
   >>> user.delete()

If you want direct access to the database connection from anywhere in your Django app::

   >>> from mango import database as db
   >>> db.users.find()      
   >>> db.sessions.find()   

Limitations
===========
Support for permissions and groups is not available yet, but is coming soon.
