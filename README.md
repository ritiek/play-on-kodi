# play-on-kodi

Stream your local/network content directly on Kodi without having to
setup FTP, SMB or anything else.

## Installation

```
git clone https://github.com/ritiek/play-on-kodi
cd play-on-kodi
pip install -r requirements.txt
python playonkodi.py --help
```

If you want to, you can copy the scripts to PATH if you want a command `playonkodi`. To do so:

```
sudo cp playonkodi.py /usr/bin/playonkodi
sudo cp -rf server/ /usr/bin/server/
sudo chmod -R 755 /usr/bin/playonkodi /usr/bin/server/
playonkodi --help
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

- This tool is supposed is supposed to be very minimal way to play local and network files on Kodi. I made it to end those awkward moments when you are unable to quickly play your local media to Kodi while everybody watches you in awe.

- If you believe your idea could comply with this aim and be interesting at the same time, please [open an issue](https://github.com/ritiek/play-on-kodi/issues) or send a PR!

## License

`The MIT License`
