#!/usr/bin/env node

var ArgumentParser = require('argparse').ArgumentParser;
var http = require('http');
var request = require('request');

var finalhandler = require('finalhandler');
var serveStatic = require('serve-static');
var path = require('path');
var os = require('os');


function parse_args() {
    var parser = new ArgumentParser({
        version: '0.1.11',
        addHelp: true,
        description: 'Stream your local/network content directly on Kodi.',
    });
    parser.addArgument(
        [ 'media' ], {
        metavar: 'MEDIA',
        type: 'string',
        help: 'Path to media file'
        }
    );
    parser.addArgument(
        [ '-s', '--server' ], {
        type: 'string',
        required: true,
        help: "Kodi's local ip address"
        }
    );
    parser.addArgument(
        [ '-p', '--port' ], {
        type: 'int',
        required: true,
        help: "Kodi's web interface port"
        }
    );
    parser.addArgument(
        [ '-i', '--interface-ip' ], {
        type: 'string',
        help: "[Optional] Interface IP to send to Kodi server"
        }
    );
    return parser;
}


function get_localip() {
    var ifaces = os.networkInterfaces();
    var localip = '';

    Object.keys(ifaces).forEach(function (ifname) {
        ifaces[ifname].forEach(function (iface) {
            if ('IPv4' !== iface.family || iface.internal !== false) {
                // skip over internal (i.e. 127.0.0.1) and non-ipv4 addresses
                return;
            }
            localip = iface.address;
        });
    });

    return localip;
}


function serve_directory(directory, port) {
    var serve = serveStatic(directory);

    var server = http.createServer(function(req, res) {
        var done = finalhandler(req, res);
        serve(req, res, done);
    });

    server.listen(port);
}


function kodi_post(network_file, server, port) {
    var dataString = '{"id":519,"jsonrpc":"2.0","method":"Player.Open","params":{"item":{"file":"' + network_file + '"}}}';

    var options = {
        url: 'http://' + server + ':' + port + '/jsonrpc',
        method: 'POST',
        body: dataString
    };

    return request(options);
}


var parser = parse_args();
var args = parser.parseArgs();

const filepath = args.media
const server_ip = args.server
const server_port = args.port


if (filepath.indexOf('://') == -1) {

    var local_ip = args.interface_ip;
    if (local_ip == null) {
        local_ip = get_localip();
    }
    const local_port = '15000';
    console.log(local_ip);

    var directory = path.dirname(filepath);
    var network_file = 'http://' + local_ip + ':' + local_port + '/' + encodeURIComponent(path.basename(filepath));

    console.log('Hosting media content on:')
    console.log(network_file + '\n');

    serve_directory(directory, local_port);

    console.log('Commanding jsonrpc on ' + server_ip + ':' + server_port + ' to listen for media content on the hosted URL')
    kodi_post(network_file, server_ip, server_port);
    console.log('The media content should play now')

    console.log('\nHit Ctrl+C to kill the local stream server');

} else {

    console.log('Commanding jsonrpc on ' + server_ip + ':' + server_port + ' to listen for media content on the hosted URL')
    kodi_post(filepath, server_ip, server_port);
    console.log('The media content should play now')
}
