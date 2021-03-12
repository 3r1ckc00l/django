# DJANGO
default django installation

# RUN CONSOLE (PYCHARM)
$pip install Django==3.x.x
$django-admin.py startproject [project_name]
$touch requirements.txt (add: Django==3.x.x)

# RUN MIGRATION
$pip install -r requirements.txt
$./manage.py makemigrations --check
$./manage.py migrate
$./manage.py test => ./manage.py test --settings=project_name.apps.settings (custom setting ci/cd)

# CREATE SUPERUSER
$./manage.py createsuperuser (create custom superadmin)
