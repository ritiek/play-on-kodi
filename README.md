# play-on-kodi

Stream your local/network content directly on Kodi without having to
setup FTP, SMB or anything else.

## Installation

Install the latest release with:
```
$ npm install -g playonkodi
```

If you plan to hack on the code, you can instead install the development version with:
```
$ git clone https://github.com/ritiek/play-on-kodi
$ cd play-on-kodi
$ npm install -g .
```

Also make sure you have
[youtube-dl](https://github.com/rg3/youtube-dl/blob/master/README.md#installation) installed.

## Usage

```
usage: playonkodi.js [-h] [-v] -s SERVER -p PORT [-u USER] [-P PASS] [-i INTERFACE_IP] MEDIA

Stream your local/network content directly on Kodi.

Positional arguments:
  MEDIA                 Path to media file

Optional arguments:
  -h, --help            Show this help message and exit.
  -v, --version         Show program's version number and exit.
  -s SERVER, --server SERVER
                        Kodi's local ip address
  -p PORT, --port PORT  Kodi's web interface port
  -u USER, --username USER
                        [Optional] Kodi's web interface username
  -P PASS, --password PASS
                        [Optional] Kodi's web interface password
  -i INTERFACE_IP, --interface-ip INTERFACE_IP
                        [Optional] Interface IP to send to Kodi server
```

### Examples

Stream a local video to Kodi
```
$ playonkodi -s 192.168.0.108 -p 6050 /path/to/local/media/file
```

Stream a video from the internet to Kodi
```
$ playonkodi -s 192.168.0.108 -p 6050 http://path/to/media
```

Since this tool now uses the youtube-dl backend to resolve URLs, so you should
be able to media content from most websites (including YouTube, HotStar, and many more).
Just pass the URL, and you'll know if it plays on Kodi.

Send local IP address to Kodi server manually (useful if script cannot find out
the correct network interface IP automatically)
```
$ playonkodi -s 192.168.0.108 -p 6050 -i 192.168.0.105 /path/to/local/media/file
```

## Loading External Subtitles

There maybe cases where you would want to link your local media content with external
subtitles (.srt, etc.). Due to a limitation in Kodi, it cannot be done automatically
(check out [issue #3](https://github.com/ritiek/play-on-kodi/issues/3)).

However you can install `mkvtoolnix` (`$ sudo apt install mkvtoolnix`) to embed
external subtitles in the container itself and pass this new container to Kodi.

**For example:**
```
$ mkvmerge -o output.mkv input.mp4 subtitles.srt
$ playonkodi -s 192.168.0.108 -p 6050 output.mkv
```

## Why?

This tool is supposed is supposed to be very minimal way to play local and
network files on Kodi. It was made to quickly be able to play your local media
content to Kodi server. You don't want to setup FTP/SMB (if not already), add it
as a network source on Kodi and locate the media to just make the thing play


## How it works?

- For local media, it makes your media content available locally to the devices
  on the same network. Otherwise it just uses youtube-dl to resolve the passed URL.

- It then attempts to figure out your PC's local IP address.

- And lastly, it makes a network request to Kodi's jsonrpc server to play the
  hosted media content.



# License

`[![License](https://img.shields.io/github/license/ritiek/play-on-kodi.svg)](https://github.com/ritiek/play-on-kodi/blob/master/LICENSE)
