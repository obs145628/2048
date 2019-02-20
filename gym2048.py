from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import inspect
import os

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
    
    '''
    @app.route('/api', methods=['POST'])
    def api_handler():
        content = request.json
        res = requesthandler.handle_api(content)    
        return jsonify(res)
    '''

    @socketio.on('g2048')
    def msg_2048_cb(data):
        print('received data:', data)
        emit('g2048', {'ab': ['cd', 'ef']})
        
    socketio.run(app, host='0.0.0.0', port=int(port), debug=True)


    

if __name__ == '__main__':
    run_server('8080', 'public', 'static/index.html')
