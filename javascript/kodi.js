var http = require('http');
var request = require('request');

var finalhandler = require('finalhandler');
var serveStatic = require('serve-static');
var path = require('path');


function serve_directory(directory, port) {
    let serve = serveStatic(directory);

    let server = http.createServer(function(req, res) {
        let done = finalhandler(req, res);
        serve(req, res, done);
    });

    server.listen(port);
}


function kodi_post(network_file, server, port) {
    //let data = '{"id":200,"jsonrpc":"2.0","method":"Player.Open","params":{"item":{"file":"' + network_file + '"}}}';
    let data = {"id":"200","jsonrpc":"2.0","method":"Player.Open","params":{"item":{"file":"' + network_file + '"}}};
    let response = request.post('http://' + server + ':' + port + '/jsonrpc', data);
    console.log('file posted');
    return response;
}


const filepath = '/home/ritiek/Videos/TV Shows/Tsuki Ga Kirei [1080p]/[HorribleSubs] Tsuki ga Kirei - 01 [1080p].mkv'

const directory = path.dirname(filepath);
console.log(directory);
const network_file = path.basename(filepath);
console.log(network_file);

serve_directory(directory, port=15000);

setTimeout(kodi_post, 5000, network_file, 'localhost', '8050');
//response = request.post('http://service.com/upload', {form:{key:'value'}})
