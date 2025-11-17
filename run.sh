#!/bin/bash
source venv/bin/activate
pip install -r requirements.txt > /dev/null 2>&1
python3 Main.py
echo "Program exited with exit code:" $?
deactivate