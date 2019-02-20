from flask import Flask, request, jsonify
import inspect
import os

def script_dir():
    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def run_server(port, data_dir, index):
    data_dir = os.path.join(script_dir(), data_dir)
    
    app = Flask(__name__,
                static_folder=data_dir,
            static_url_path='/static')

    '''
    @app.route('/api', methods=['POST'])
    def api_handler():
        content = request.json
        res = requesthandler.handle_api(content)    
        return jsonify(res)
    '''

    url='http://0.0.0.0:' + port + '/' + index
    print('App runing at:', url)
    app.run(host='0.0.0.0', port=port, debug=True)


    

if __name__ == '__main__':
    run_server('8080', 'public', 'static/index.html')
