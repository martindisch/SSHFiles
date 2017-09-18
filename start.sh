#!/bin/bash

export FLASK_APP=sshfiles
export FLASK_DEBUG=1
. venv/bin/activate
flask run --host=0.0.0.0 --with-threads
