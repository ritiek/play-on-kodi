# play-on-kodi

Stream your local/network content directly on Kodi without having to
setup FTP, SMB or anything else.

I originally made this [tool in python](https://github.com/ritiek/play-on-kodi/tree/python-old) but python would prevent rest of the script from execution as soon as the web server was started. Ultimately, making it a lot harder to put this up on pypi but hey, Node saves the day!

## Installation

```
npm install -g playonkodi
```

For superhero devs:

```
git clone https://github.com/ritiek/play-on-kodi
cd play-on-kodi
npm install -g .
```

## Usage

```
usage: playonkodi [-h] [-v] [-s SERVER] [-p PORT] MEDIA

Stream your local/network content directly on Kodi.

Positional arguments:
  MEDIA                 Path to media file

Optional arguments:
  -h, --help            Show this help message and exit.
  -v, --version         Show program's version number and exit.
  -s SERVER, --server SERVER
                        Kodi's local ip address
  -p PORT, --port PORT  Kodi's web interface port
```

### Examples

Streaming a local video to Kodi

```
playonkodi -s 192.168.0.108 -p 6050 /path/to/local/media/file
```

Streaming a video from the internet to Kodi

```
playonkodi -s 192.168.0.108 -p 6050 http://raw/path/to/media/file
```

Please make sure the link is an actual path to a video stream which can also be streamed in players like `VLC` and `MPV`.

## Contributing

- This tool is supposed is supposed to be very minimal way to play local and network files on Kodi. I made it to end those awkward moments when you are unable to quickly play your local media to Kodi while everybody watches you in awe.

- If you believe your idea could comply with this aim and be interesting at the same time, please [open an issue](https://github.com/ritiek/play-on-kodi/issues) or send a PR!

## License

`The MIT License`
