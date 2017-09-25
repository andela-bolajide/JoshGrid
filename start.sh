#!/bin/bash

set -e

yarn start:dev & python manage.py runserver
