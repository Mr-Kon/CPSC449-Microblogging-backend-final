users: gunicorn --access-logfile - --capture-output -p $PORT api:__hug_wsgi__
posts: gunicorn --access-logfile - --capture-output -p $PORT posts:__hug_wsgi__
registry: gunicorn --access-logfile - --capture-output -p $PORT registry:__hug_wsgi__