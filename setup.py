from setuptools import setup, find_packages
import os

DESCRIPTION = "Simple, thread safe, config storage. The config object is serialized, which makes it better (at the very least more obvious) than ConfigObj at saving simple Python datastructure. For the same reason however, the resulting config files are not as readable as ConfigObj ini files."

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass


setup(name='config',
      version='0.1.0',
      packages=find_packages(),
      author='Nick Zalutskiy',
      author_email='pacemkr@{nospam}gmail.com',
      url='https://github.com/pacemkr/config',
      include_package_data=True,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      platforms=['any'],
)
