## Website Setup

# Go to the project root
cd ..

# Install website dependencies
pip install -r requirements.txt
npm install

# Go to the source folder
cd src

# Build static files
tsc
python3 manage.py collectstatic

# Migrate database
python3 manage.py makemigrations
python3 manage.py migrate
