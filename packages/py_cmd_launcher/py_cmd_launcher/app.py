import logging
from flask import Flask, jsonify
import subprocess
#import signal
#import threading
from argparse import ArgumentParser

# Prozess-Handler
process = None

def create_app(script_path):
    app = Flask(__name__)
    #def run_script():
    #    global process
    #    process = subprocess.Popen(script_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    @app.route('/start', methods=['GET'])
    def start():
        global process
        if process is None:
            # Start the script (in a new thread?)
            #thread = threading.Thread(target=run_script)
            #thread.start()
            process = subprocess.Popen(script_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return jsonify({'status': 'Script started!'}), 201
        else:
            return jsonify({'status': 'Script is already running!'}), 204

    @app.route('/stop', methods=['GET'])
    def stop():
        global process
        if process is not None:
            # Terminate the process
            #os.kill(process.pid, signal.SIGTERM)
            process.terminate()
            process.wait()
            process = None
            return jsonify({'status': 'Script stopped!'}), 200
        else:
            return jsonify({'status': 'No script is running!'}), 204
        
    @app.route('/status', methods=['GET'])
    def status():
        global process
        if process is not None:
            return jsonify({'status': 'Live'}), 200
        else:
            return jsonify({'status': 'Process was lost'}), 204
        
    return app

def main():
    logging.captureWarnings(True)
    log = logging.getLogger("py_cmd_launcher_main")
    exit_code=0
    try:
        parser = ArgumentParser(description='Config')
        parser.add_argument('--host', type=str, default='127.0.0.1',
                            help='Host (default is 127.0.0.1)')
        parser.add_argument('--port', type=int, default=4990,
                            help='Port (default is 4990)')
        parser.add_argument(name_or_flags='--script', help="command inside PATH to launch", default="bash -c 'echo no_command'")
        parser.add_argument(name_or_flags='--debug', help="debug", default=False, type=bool)
        
        args = parser.parse_args()
        
        app = create_app(args.script)
        app.run(host=args.host, port=args.port,debug=args.debug)
        
    except Exception as e: 
        exit_code = 1 # generic error
    if exit_code is not None and exit_code > 0:
        log.error(f"Exited with Status Code: {str(exit_code)}")
        exit(exit_code)
    log.info(f"Exited with Status Code: {str(exit_code)}")

if __name__ == "__main__":
    main()