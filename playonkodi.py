import requests
import os
import random
import socket
import subprocess
import time
import argparse
import sys

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote


def parse_args():
    parser = argparse.ArgumentParser(
        description='Stream your local/network content directly on Kodi.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        'media',
        metavar='MEDIA',
        type=str,
        help='path to file containing media')
    parser.add_argument(
        '-s',
        '--server',
        default='127.0.0.1',
        type=str,
        help="kodi's local ip address")
    parser.add_argument(
        '-p',
        '--port',
        default=8080,
        type=int,
        help="kodi's web interface port")
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
    filename = quote(splits[-1])
    return (filename, directory)


def kodi_post(network_file, server, port):
    data = '{"id":529,"jsonrpc":"2.0","method":"Player.Open","params":{"item":{"file":"' + network_file + '"}}}'
    response = requests.post('http://{0}:{1}/jsonrpc'.format(server, port), data=data)
    return response


def command_line():
    parser = parse_args()
    raw_args = sys.argv[1:]
    args = parser.parse_args(raw_args)

    filepath = args.media
    server = args.server
    port = args.port

    if '://' in filepath:
        response = kodi_post(filepath, server, port)
        print(response.text)
    else:
        if not os.path.isfile(filepath):
            print('could not locate local media: ' + filepath)
            sys.exit(1)

        filename, directory = parse_filepath(filepath)
        directory = os.path.join(os.getcwd(), directory)
        server_path = os.path.join(sys.path[0], 'server', 'server.py')

        local_ip = get_local_ip()
        local_port = str(random.randint(45000, 50000))

        command = ['python', server_path, directory, local_port]
        server_cmd = subprocess.Popen(
                      command,
                      shell=False,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)

        network_file = 'http://{0}:{1}/content/{2}'.format(local_ip, local_port, filename)
        print(network_file)

        time.sleep(2)

        response = kodi_post(network_file, server, port)
        print(response.text)

        print('\nHit CTRL+C to kill the stream web server')

        try:
            while server_cmd.poll() is None:
                time.sleep(1)
            print('It seems like address already in use or web server was closed. Please try again.')
        except KeyboardInterrupt:
            server_cmd.terminate()
            raise


if __name__ == '__main__':

    command_line()
