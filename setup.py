from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='udevadm-monitor',
      version=version,
      description="monitoring udev events directly via udevadm monitor",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='threading events stoppable',
      author='Pavol Vargovčík',
      author_email='pallly.vargovcik@gmail.com',
      url='',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
