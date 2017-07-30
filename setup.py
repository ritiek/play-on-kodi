#!/usr/bin/env python

from setuptools import setup, find_packages
import playonkodi

with open("README.rst", "r") as f:
    long_description = f.read()

setup(name='playonkodi',
      version=playonkodi.__version__,
      description='Stream your local/network content directly on Kodi.',
      long_description=long_description,
      author='Ritiek Malhotra',
      author_email='ritiekmalhotra123@gmail.com',
      packages = find_packages(),
      entry_points={
            'console_scripts': [
                  'playonkodi = playonkodi.playonkodi:command_line',
            ]
      },
      url='https://www.github.com/ritiek/play-on-kodi',
      keywords=['kodi', 'url', 'local', 'files', 'media'],
      license='MIT',
      download_url='https://github.com/ritiek/play-on-kodi/archive/v' + playonkodi.__version__ + '.tar.gz',
      classifiers=[],
      install_requires=[
            'requests',
      ]
)
