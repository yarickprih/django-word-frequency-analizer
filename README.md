# Word frequency analizer written on Django
It analizes given text and output the result of frequency analisys in 3 columns.
1) Most frequent words
2) Words with average frequency
3) Least frequent words

# Instalation and Setup
1) Clone this repository with `git clone https://github.com/yarickprih/django-word-frequency-analizer`
2) Create and activate virtual environment with `python3 -m venv env` and `source env/bin/activate`
3) Switch to project directory with `cd django-word-frequency-analizer/`
4) Install dependencies with `pip install -r requirements.txt`
5) Make and run migrations with `python manage.py makemigrations && python manage.py migrate`
6) Go to `127.0.0.1:8000` in a browser
