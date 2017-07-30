# play-on-kodi

Stream your local/network content directly on Kodi without having to
setup FTP, SMB and what not.

## Installation

```
git clone https://github.com/ritiek/play-on-kodi
cd play-on-kodi
pip install -r requirements.txt
```

## Usage

```
usage: playonkodi.py [-h] [-s SERVER] [-p PORT] MEDIA

Stream your local/network content directly on Kodi.

positional arguments:
  MEDIA                 path to file containing media

optional arguments:
  -h, --help            show this help message and exit
  -s SERVER, --server SERVER
                        kodi's local ip address (default: 127.0.0.1)
  -p PORT, --port PORT  kodi's web interface port (default: 8080)
```

### Examples

Streaming a local video to Kodi

```
python playonkodi.py -s 192.168.0.108 -p 6050 /path/to/local/media/file
```

Streaming a video from the internet to Kodi

```
python playonkodi.py -s 192.168.0.108 -p 6050 http://raw/path/to/media/file
```

Please make sure the link is an actual path to a video stream which can also be streamed in players like `VLC` and `MPV`.

## Contributing

- This tool is supposed is supposed to be very minimal way to play local and network files on Kodi. I made this little tool to stop those annoying moments where you are unable to quickly play your local media to Kodi..

- If you believe your idea could comply with this and be interesting at the same time, please [open an issue](https://github.com/ritiek/play-on-kodi/issues) or send a PR!

## License

`The MIT License`
