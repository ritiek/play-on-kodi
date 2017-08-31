var http = require('http');
var request = require('request');

var finalhandler = require('finalhandler');
var serveStatic = require('serve-static');
var path = require('path');
var os = require('os');


function get_localip() {
    let ifaces = os.networkInterfaces();
    let localip = '';

    Object.keys(ifaces).forEach(function (ifname) {
        ifaces[ifname].forEach(function (iface) {
            if ('IPv4' !== iface.family || iface.internal !== false) {
                // skip over internal (i.e. 127.0.0.1) and non-ipv4 addresses
                return;
            }
        localip += iface.address;
        });
    });

    return localip;
}


function serve_directory(directory, port) {
    let serve = serveStatic(directory);

    let server = http.createServer(function(req, res) {
        let done = finalhandler(req, res);
        serve(req, res, done);
    });

    server.listen(port);
}


function kodi_post(network_file, server, port) {
    var dataString = '{"id":519,"jsonrpc":"2.0","method":"Player.Open","params":{"item":{"file":"' + network_file + '"}}}';

    let options = {
        url: 'http://' + server + ':' + port + '/jsonrpc',
        method: 'POST',
        body: dataString
    };

    return request(options);
}


//const filepath = 'test.mkv';
const filepath = '/home/ritiek/Videos/TV Shows/Tsuki Ga Kirei [1080p]/[HorribleSubs] Tsuki ga Kirei - 01 [1080p].mkv'
const localip = get_localip();
const port = '15000';

const directory = path.dirname(filepath);
const network_file = 'http://' + localip + ':' + port + '/' + encodeURIComponent(path.basename(filepath));
console.log(network_file);

serve_directory(directory, port);

//setTimeout(kodi_post, 5000, network_file, 'localhost', '8050');
const response = kodi_post(network_file, 'localhost', '8050');
console.log(response.body);
