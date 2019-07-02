#!/bin/sh
exec gunicorn -b :5000 --timeout 300 --access-logfile - --error-logfile - neural_network:app