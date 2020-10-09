python -m pip install -U pip setuptools
pip install -r requirements.txt

python manage.py makemigrations website
python manage.py migrate