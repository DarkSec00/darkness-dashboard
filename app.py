from flask import Flask, request, jsonify, render_template, abort
import os
import subprocess
import logging

app = Flask(__name__)

AUTH_TOKEN = "800f977c814917440261045111d7af8f"
BASE_DIR = os.path.join(os.path.dirname(__file__), "scripts")

logging.basicConfig(filename='flask_api.log', level=logging.INFO)

@app.before_request
def authenticate():
    token = request.args.get('token')
    if token != AUTH_TOKEN:
        logging.warning(f"Unauthorized access attempt from {request.remote_addr}")
        abort(403)
    logging.info(f"Authorized request from {request.remote_addr}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-osint')
def run_osint():
    script_path = os.path.join(BASE_DIR, 'osint_menu.sh')
    if not os.path.isfile(script_path):
        return jsonify({"error": "Script not found"}), 404
    try:
        output = subprocess.check_output(['bash', script_path], stderr=subprocess.STDOUT)
        return jsonify({"output": output.decode('utf-8')})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": e.output.decode('utf-8')}), 500

@app.route('/run-wifi')
def run_wifi():
    script_path = os.path.join(BASE_DIR, 'wifi_tools_menu.sh')
    if not os.path.isfile(script_path):
        return jsonify({"error": "Script not found"}), 404
    try:
        output = subprocess.check_output(['bash', script_path], stderr=subprocess.STDOUT)
        return jsonify({"output": output.decode('utf-8')})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": e.output.decode('utf-8')}), 500

@app.route('/status')
def status():
    return jsonify({
        "system_name": "Whispering_Shadow",
        "status": "✅ All modules operational",
        "last_updated": "2025-06-29 14:41 CDT"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)