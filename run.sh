#!/bin/bash
source venv/bin/activate
pip install -r requirements.txt > null
python3 Main.py
echo "Program exited with exit code:" $?
deactivate