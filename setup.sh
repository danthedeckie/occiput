#!/bin/bash

####################################################
# Config:

DIR=.virtualenv
PYTHON=$DIR/bin/python
PIP=$DIR/bin/pip

####################################################
# Actually start doing stuff:

if [[ "$1" == "clean" ]]; then
    rm -rf "$DIR"
fi

if [[ "$1" == "new" ]]; then
    rm -rf .git
    git init .
    git commit -a -m 'initial commit, from flask-basic-bootstrap'
fi

if [[ ! -d "$DIR" ]]; then
    mkdir "$DIR"
fi

if [[ ! -f ".setup/virtualenv-1.9.1/virtualenv.py" ]]; then
    tar -zxC .setup -f .setup/virtualenv-1.9.1.tar.gz
fi

# if there's no python in virtualenv, make one:
[[ -f "$PYTHON" ]] || python ./.setup/virtualenv-1.9.1/virtualenv.py "$DIR"

# get required python modules:
$PIP install -r "requirements.txt"

# install required config files.
if [[ ! -e "config.py" ]]; then
    $PYTHON .setup/make_initial_config_file.py > "config.py"
fi

# setup standard hooks.
if [[ ! -e ".git/hooks/pre-commit" ]]; then
    cp .setup/hooks/pre-commit .git/hooks/pre-commit
fi
