import os
import shutit
from flask import Flask, request

app = Flask(__name__)

# just to prove api works
@app.route('/ping', methods=['GET'])
def ping():
    os.system('echo pong')
    return 'OK'

# issue replication
@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    os.system("echo 'healthcheck'")
    # hangs inside create_session
    shell = shutit.create_session(echo=True, loglevel='debug')
    # never shell.send reached 
    shell.send('echo Hello World', echo=True)
    # never returned
    return 'OK'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
