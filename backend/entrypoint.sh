#!/bin/sh

if [ "$POSTGRES_DB" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 1
    done

    echo "PostgreSQL started"
fi

# Apply Django database migrations
python manage.py migrate

exec "$@"
