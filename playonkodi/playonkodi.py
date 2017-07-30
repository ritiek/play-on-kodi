import requests
import os
import random
import socket
import subprocess
import time
import argparse
import sys

KODI_HOST = '127.0.0.1'
KODI_PORT = 8050


def parse_args():
    parser = argparse.ArgumentParser(
        description='Stream your local/network content directly on Kodi.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        'media',
        metavar='MEDIA',
        type=str,
        help='path to file containing media')
    return parser


def get_local_ip():
    local = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local.connect(("8.8.8.8", 80))
    ip = local.getsockname()[0]
    local.close()
    return ip


def parse_filepath(filepath):
    splits = filepath.split('/')
    directory = '/'.join(splits[:-1])
    filename = splits[-1]
    return (filename, directory)


def kodi_post(network_file, KODI_HOST, KODI_PORT):
    data = '{"id":529,"jsonrpc":"2.0","method":"Player.Open","params":{"item":{"file":"' + network_file + '"}}}'
    response = requests.post('http://{0}:{1}/jsonrpc'.format(KODI_HOST, KODI_PORT), data=data)
    return response


def command_line():
    local_ip = get_local_ip()
    local_port = str(random.randint(45000, 50000))

    parser = parse_args()
    raw_args = sys.argv[1:]
    args = parser.parse_args(raw_args)

    filepath = args.media

    if '://' in filepath:
        response = kodi_post(filepath, KODI_HOST, KODI_PORT)
        print(response.text)
    else:
        filename, directory = parse_filepath(filepath)

        command = ['python', 'server.py', directory, local_port]
        server = subprocess.Popen(
                      command,
                      shell=False,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)

        network_file = 'http://{0}:{1}/content/{2}'.format(local_ip, local_port, filename)
        print(network_file)

        time.sleep(2)

        response = kodi_post(network_file, KODI_HOST, KODI_PORT)
        print(response.text)

        print('\nHit CTRL+C to kill the stream webserver')

        try:
            while server.poll() is None:
                time.sleep(1)
        except KeyboardInterrupt:
            server.terminate()
            raise


if __name__ == '__main__':

    command_line()
