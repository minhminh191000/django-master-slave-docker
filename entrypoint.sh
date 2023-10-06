#!/bin/bash
action=$1

case $action in
init)
  echo "Init Django service..."
  python manage.py makemigrations
  python manage.py migrate
  python manage.py collectstatic
  ;;

migrate)
  echo "Migrate DB..."
  python manage.py makemigrations
  python manage.py migrate
  ;;

collectstatic)
  echo "Collect all statics file..."
  python manage.py collectstatic
  ;;

createsuperuser)
  echo "Create super user..."
  python manage.py createsuperuser
  ;;

runserver)
  echo "Start django service..."
  echo "Current working dir: $(pwd)"
  echo "Migrate DB..."
  python manage.py makemigrations
  python manage.py migrate
  echo "Done"
  echo "Start server..."
  python manage.py runserver 0.0.0.0:8000 --noreload
  ;;
attach)
  /bin/bash
  ;;
*)
  echo "Invalid arguments"
  echo $1
  ;;
esac
