:: Website Setup

@echo off

:: Go to the project root
cd ..

:: Install website dependencies
pip install -r requirements.txt
npm install

:: Go to the source folder
cd src

:: Build static files
tsc
python manage.py collectstatic

:: Migrate database
python manage.py makemigrations
python manage.py migrate
