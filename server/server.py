from flask import Flask, request, send_from_directory
import sys

app = Flask(__name__, static_url_path='')

@app.route('/content/<path:filename>')
def send_content(filename):
    return send_from_directory(directory, filename)

directory = sys.argv[1]
local_port = sys.argv[2]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=local_port, threaded=True)
