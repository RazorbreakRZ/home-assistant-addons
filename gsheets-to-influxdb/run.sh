#!/usr/bin/with-contenv bashio
echo "Starting add-on"
. .venv/bin/activate
python3 main.py
echo "Add-on stopped"
