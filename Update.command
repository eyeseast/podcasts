#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

VENV="${SCRIPT_DIR}/.venv"
PYTHON="${VENV}/bin/python3"
SCRIPT="${SCRIPT_DIR}/update.py"
FEEDS="${SCRIPT_DIR}/feeds.txt"
PODCASTS="${SCRIPT_DIR}/podcasts"

mkdir -p $PODCASTS

$PYTHON $SCRIPT $FEEDS $PODCASTS
