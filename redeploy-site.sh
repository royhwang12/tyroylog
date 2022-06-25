#!/bin/bash

tmux kill-server

git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate

pip install -r requirements.txt

dnf install tmux
tmux new-session -d -s my_session
tmux send-keys -t new_session 'source python3-virtualenv/bin/activate' C-m
tmux send-keys 'flask run --host=0.0.0.0' C-m