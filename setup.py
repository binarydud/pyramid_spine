import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'pytz',
    'sqlalchemy',
    'pyramid_jinja2',
    'pyramid_mailer',
    'passlib',
    'wtforms'
]
try:
    import wsgiref
except ImportError:
    requires.append('wsgiref')

setup(name='pyramid_spine',
      version='0.1',
      description='pyramid_spine',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      license="MIT",
      author='Matt George',
      maintainer='Matt George',
      author_email='mgeorge@gmail.com',
      url='https://github.com/binarydud/pyramid_spine',
      download_url='https://github.com/binarydud/pyramid_spine',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="pyramid_spine",
      entry_points = """\
      [paste.app_factory]
      main = pyramid_spine:main
      """,
      )

