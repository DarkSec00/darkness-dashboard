# 🌑 Darkness Dashboard

A tactical OSINT, network, and security dashboard for cyber professionals and red teamers. This self-hosted tool empowers users to run advanced offensive and defensive tools in a web-based interface.

---

## 🔧 Installation Guide

Tested on: Ubuntu 22.04+ / Debian-based distros

### 1. Install system dependencies

sudo apt update && sudo apt install -y python3 python3-pip python3-venv nginx git

### 2. Clone and enter the project

git clone https://github.com/YOUR_USERNAME/darkness-dashboard.git  
cd darkness-dashboard

### 3. Create Python virtual environment

python3 -m venv venv  
source venv/bin/activate

### 4. Install Python dependencies

pip install -r requirements.txt

### 5. (Optional) Configure `.env` file

Copy the sample and edit:  
cp .env.sample .env

### 6. Run the app (development mode)

python app.py

Or deploy with Gunicorn & Nginx for production (see below).

---

## 🌐 Nginx Sample Configuration

Refer to `nginx.conf.sample` to configure your reverse proxy.

---

## 🛡️ Legal Disclaimer

This software is provided for legal and ethical use only. You are fully responsible for how you use the Darkness Dashboard.

⚠️ Use only on systems/networks you **own** or have **explicit permission** to test.  
⚠️ The authors are **not liable** for misuse, damages, or violations of law.

© Darkness Security • August 4, 2025

---

## 2. install.sh

#!/bin/bash

echo "🌑 Darkness Dashboard Installer"

# Exit on error  
set -e

# System dependencies  
echo "[+] Installing system packages..."  
sudo apt update  
sudo apt install -y python3 python3-pip python3-venv nginx git

# Clone repository  
echo "[+] Cloning repository..."  
git clone https://github.com/YOUR_USERNAME/darkness-dashboard.git  
cd darkness-dashboard

# Python virtual environment setup  
echo "[+] Setting up virtual environment..."  
python3 -m venv venv  
source venv/bin/activate

# Python dependencies  
echo "[+] Installing Python requirements..."  
pip install --upgrade pip  
pip install -r requirements.txt

echo ""  
echo "🎉 Installation complete!"  
echo "➡️ Your dashboard is ready to run:"  
echo "   - Activate the environment: source venv/bin/activate"  
echo "   - Launch the app (dev mode): python app.py"  
echo ""  
echo "⚠️ For production use, configure Gunicorn + Nginx with the nginx.conf.sample."

---

## 3. requirements.txt

Flask==2.3.3  
requests

(Only list the Python packages required by your application — no CLI tools or setup instructions.)

---

## 4. nginx.conf.sample

# Darkness Dashboard Nginx Sample Config

server {  
    listen 80;  
    server_name dashboard.example.com;

    location / {  
        proxy_pass http://127.0.0.1:550;  
        proxy_set_header Host $host;  
        proxy_set_header X-Real-IP $remote_addr;  
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  
        proxy_set_header X-Forwarded-Proto $scheme;  
    }

    # Uncomment the following for automatic HTTPS redirect (Certbot recommended)  
    # return 301 https://$host$request_uri;  
}

(Change `dashboard.example.com` to your actual subdomain)

---

## 5. .env.sample

# Darkness Dashboard Environment Variables

FLASK_SECRET_KEY=changeme123  
ENABLE_LOGGING=true

Encourage users to copy this to `.env` and customize as needed.

---