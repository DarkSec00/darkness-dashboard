from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import os
import subprocess
import logging
import secrets

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

LOG_FILE = os.path.join(BASE_DIR, "flask_api.log")
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

AUTH_TOKEN = os.getenv("AUTH_TOKEN")

if not AUTH_TOKEN:
    AUTH_TOKEN = secrets.token_hex(16)
    print(f"[INFO] No auth token set in environment. Generated token: {AUTH_TOKEN}")
    print("Please set this token in your environment variable AUTH_TOKEN for future runs.")

@app.before_request
def authenticate():
    token = request.args.get('token')
    if token != AUTH_TOKEN:
        logging.warning(f"Unauthorized access attempt from IP {request.remote_addr}")
        abort(403)

@app.route("/")
def index():
    logging.info("Accessed root endpoint")
    return jsonify({"message": "API active", "status": "online"})

@app.route("/status")
def status():
    logging.info("Status check requested")
    return jsonify({"system": "Server", "status": "operational"})

@app.route("/run-cmd", methods=["POST"])
def run_cmd():
    data = request.get_json()
    cmd = data.get("command")
    if not cmd:
        logging.error("No command provided")
        return jsonify({"error": "No command provided"}), 400

    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=10)
        logging.info(f"Executed command: {cmd}")
        return jsonify({"output": output.decode("utf-8")})
    except subprocess.CalledProcessError as e:
        logging.error(f"Command error: {e.output.decode('utf-8')}")
        return jsonify({"error": e.output.decode("utf-8")}), 500
    except subprocess.TimeoutExpired:
        logging.error("Command timeout")
        return jsonify({"error": "Command timed out"}), 504

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=550)
    