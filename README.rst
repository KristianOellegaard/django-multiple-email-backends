django-multiple-email-backends
==============================

An easy solution to send your email to more than one backend, e.g. if you want to send it to the user via SMTP but also log it to keep the record of send' emails.

Usage
-----

This example.py will output your emails to the console and save it in a folder on your filesystem. You could ofcourse combine this as you want, e.g. the SMTP backend and the filebackend.

::

  EMAIL_BACKEND = "django_multiple_email_backends.backend.CombinedEmailBackend"
  EMAIL_BACKEND_LIST = ['django.core.mail.backends.console.EmailBackend',
                        'django.core.mail.backends.filebased.EmailBackend']


License
-------

BSD