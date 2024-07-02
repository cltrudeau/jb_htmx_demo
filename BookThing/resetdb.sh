#!/bin/bash

find . -name "*.pyc" -exec rm {} \;
rm db.sqlite3

# django db and test data process
python manage.py makemigrations books
python manage.py migrate

echo "=== Creating Test Data ==="
python manage.py create_test_data
