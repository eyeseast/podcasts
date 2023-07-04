#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

VENV="${SCRIPT_DIR}/.venv"
PIP="${VENV}/bin/pip"
REQUIREMENTS="${SCRIPT_DIR}/requirements.txt"

if [ -d $VENV ]; then
    echo "Deleting old dependencies ..."
    rm -r $VENV
fi

echo "Creating virtual environment ..."
python3 -m venv $VENV
source $VENV/bin/activate

echo "Installing dependencies ..."
$PIP install -U pip wheel
$PIP install -r $REQUIREMENTS
