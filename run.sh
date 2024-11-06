#!/bin/bash
set -e
gunicorn base.wsgi --log-file -