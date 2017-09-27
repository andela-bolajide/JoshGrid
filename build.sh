#!/bin/bash

set -e

npm install -g yarn

yarn install

pip install -r requirements.txt

bower install

yarn start

gunicorn joshgrid.wsgi
