from flask import Flask, request, jsonify
from flask_socketio import SocketIO
import inspect
import os

g_req_idx = [0]
g_req_res = dict()

def script_dir():
    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def run_server(port, data_dir, index):
    data_dir = os.path.join(script_dir(), data_dir)
    url='http://0.0.0.0:' + port + '/' + index
    print('App runing at:', url)
    
    app = Flask(__name__,
                static_folder=data_dir,
            static_url_path='/static')
    app.config['SECRET_KEY'] = 'secret!'
    socketio = SocketIO(app)
    
    
    @app.route('/req', methods=['POST'])
    def req_handler():
        content = request.json
        idx = g_req_idx[0]
        g_req_idx[0] += 1
        
        socketio.emit('req', [idx, content], namespace='/')
        return jsonify(idx)

    @app.route('/getres', methods=['POST'])
    def getres_handler():
        idx = request.json
        if idx in g_req_res:
            val = g_req_res[idx]
            del g_req_res[idx]
            return jsonify(['ok', val])
        else:
            return jsonify(['no', None])
    
    
    @socketio.on('req')
    def msg_2048_cb(data):
        idx = data[0]
        res = data[1]
        g_req_res[idx] = res
        
    socketio.run(app, host='0.0.0.0', port=int(port), debug=True)

if __name__ == '__main__':
    run_server('8080', 'public', 'static/index.html')

    #reset
    #seed
    #step
