play-on-kodi
============

|pypi.python.org|

Stream your local/network content directly on Kodi without having to
setup FTP, SMB and what not.

Installation
------------

::

    pip install playonkodi

or if you like to live on the bleeding edge:

::

    python setup.py install

Usage
-----

::

    usage: playonkodi.py [-h] MEDIA

    Stream your local/network content directly on Kodi.

    positional arguments:
      MEDIA       path to file containing media

    optional arguments:
      -h, --help  show this help message and exit

Stream a video to Kodi Media Center

example:

::

    playonkodi /path/to/media/file

Contributing
------------

This tool is supposed is supposed to be very minimal way to play local
and network files on Kodi. I made this little tool because how annoying
it can be sometimes to play your local media. If you believe your idea
could comply with this and be interesting at the same time, please `open
an issue <https://github.com/ritiek/play-on-kodi/issues>`__ or send a
PR!

License
-------

``The MIT License``

.. |pypi.python.org| image:: https://img.shields.io/pypi/v/playonkodi.svg
   :target: https://pypi.org/project/playonkodi/
