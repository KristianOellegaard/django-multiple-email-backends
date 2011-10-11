import os
from setuptools import setup
from django_multiple_email_backends import __version__

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-multiple-email-backends",
    version = __version__,
    author = "Kristian Ollegaard",
    author_email = "kristian@oellegaard.com",
    description = ("Want to send through more than one interface? E.g. SMTP and database? This is your solution"),
    license = "BSD",
    keywords = "django email backend multiple",
    url = "https://github.com/KristianOellegaard/django-multiple-email-backends",
    packages=['django_multiple_email_backends'],
    long_description=read('README.rst'),
    classifiers=[
        "Topic :: Utilities",
    ],
    install_requires=[
        'Django>=1.3',
    ],
    include_package_data=True,
    zip_safe = False,
)