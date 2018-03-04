#!/bin/sh
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
deactivate
echo ".env was initialized"
echo "type .env/bin/activate to enter the virtual environment"
