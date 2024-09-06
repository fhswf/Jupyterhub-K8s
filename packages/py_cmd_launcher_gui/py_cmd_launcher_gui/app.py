import logging
import json
import os
import requests
from flask import Flask, jsonify, render_template_string
import subprocess
#import signal
#import threading
from argparse import ArgumentParser

# Prozess-Handler
process = None
#env for apps:
#export JUPYTER_COMMAND_LAUNCHER_APPS='{"app1": "http://external-api-url/app1", "app2": "http://external-api-url/app2"}'

def create_app():
    app = Flask(__name__)
    apps_config = os.getenv('JUPYTER_COMMAND_LAUNCHER_APPS', "{}")
    apps = json.loads(apps_config)

    # HTML template for the UI
    HTML_TEMPLATE = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Control Panel</title>
        <style>
            body { font-family: Arial, sans-serif; }
            button { padding: 10px 20px; margin: 5px; }
            #response, #status { margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>Control Panel</h1>
        <div id="controls"></div>
        <h2>Status Report</h2>
        <div id="status"></div>

        <script>
            const appNames = {{ app_names|tojson }};
            
            // Function to create control buttons dynamically
            function createButtons() {
                const controlsDiv = document.getElementById('controls');
                appNames.forEach(app => {
                    const startButton = document.createElement('button');
                    startButton.innerText = `Start ${app}`;
                    startButton.onclick = () => sendRequest(`/start/${app}`);
                    
                    const stopButton = document.createElement('button');
                    stopButton.innerText = `Stop ${app}`;
                    stopButton.onclick = () => sendRequest(`/stop/${app}`);

                    // Append the buttons to the controls div
                    controlsDiv.appendChild(startButton);
                    controlsDiv.appendChild(stopButton);
                    controlsDiv.appendChild(document.createElement('br')); // Line break for clarity

                    // Add a status placeholder for each app
                    const statusDiv = document.createElement('div');
                    statusDiv.id = app;
                    controlsDiv.appendChild(statusDiv);
                });
            }

            function sendRequest(endpoint) {
                fetch(endpoint)
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }
                        return response.json();
                    })
                    .then(data => {
                        document.getElementById('status').innerText = data.message;
                    })
                    .catch(error => {
                        document.getElementById('status').innerText = 'Error: ' + error.message;
                    });
            }

            function getStatus() {
                appNames.forEach(app => {
                    fetch(`/status/${app}`)
                        .then(response => {
                            if (!response.ok) {
                                throw new Error('Network response was not ok');
                            }
                            return response.json();
                        })
                        .then(data => {
                            document.getElementById(app).innerText = `Status of ${app}: ${data.status}`;
                        })
                        .catch(error => {
                            document.getElementById(app).innerText = `Error fetching status of ${app}: ${error.message}`;
                        });
                });
            }

            // Automatically refresh status every 10 seconds
            setInterval(getStatus, 10000);
            // Initial status fetch
            createButtons();  // Create buttons dynamically
            getStatus();      // Initial status fetch
        </script>
    </body>
    </html>
    '''

    @app.route('/')
    def home():
        return render_template_string(HTML_TEMPLATE, app_names=list(apps.keys()))

    @app.route('/start/<app_name>', methods=['GET'])
    def start(app_name):
        app_url = apps.get(app_name)
        if not app_url:
            return jsonify({"message": "App not found!"}), 404
        
        try:
            response = requests.get(f"{app_url}/start")
            response.raise_for_status()
            return jsonify({"message": f"Start command for {app_name} executed!"})
        except requests.exceptions.RequestException as e:
            return jsonify({"message": f"Error triggering start command for {app_name}: {str(e)}"}), 500

    @app.route('/stop/<app_name>', methods=['GET'])
    def stop(app_name):
        app_url = apps.get(app_name)
        if not app_url:
            return jsonify({"message": "App not found!"}), 404
        
        try:
            response = requests.get(f"{app_url}/stop")
            response.raise_for_status()
            return jsonify({"message": f"Stop command for {app_name} executed!"})
        except requests.exceptions.RequestException as e:
            return jsonify({"message": f"Error triggering stop command for {app_name}: {str(e)}"}), 500

    @app.route('/status/<app_name>', methods=['GET'])
    def status(app_name):
        app_url = apps.get(app_name)
        if not app_url:
            return jsonify({"status": "App not found!"}), 404

        try:
            response = requests.get(f"{app_url}/status")
            response.raise_for_status()
            status_data = response.json()
            return jsonify({"status": status_data.get("status", "Unknown")})
        except requests.exceptions.RequestException as e:
            return jsonify({"status": f"Error fetching status for {app_name}: {str(e)}"}), 500
    return app

def main():
    logging.captureWarnings(True)
    log = logging.getLogger("py_cmd_launcher_gui_main")
    exit_code=0
    try:
        parser = ArgumentParser(description='Config')
        parser.add_argument('--host', type=str, default='127.0.0.1',
                            help='Host (default is 127.0.0.1)')
        parser.add_argument('--port', type=int, default=4900,
                            help='Port (default is 4900)')
        #parser.add_argument(name_or_flags='--server', help="api server to talk to  (default is None => config via json env JUPYTER_COMMAND_LAUNCHER_APPS)", default=None)
        parser.add_argument(name_or_flags='--debug', help="debug", default=False, type=bool)
        
        args = parser.parse_args()
        
        app = create_app()
        app.run(host=args.host, port=args.port,debug=args.debug)
        
    except Exception as e: 
        exit_code = 1 # generic error
    if exit_code is not None and exit_code > 0:
        log.error(f"Exited with Status Code: {str(exit_code)}")
        exit(exit_code)
    log.info(f"Exited with Status Code: {str(exit_code)}")

if __name__ == "__main__":
    main()