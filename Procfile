registry: gunicorn --access-logfile - --capture-output -p $PORT registry:__hug_wsgi__
users: gunicorn --access-logfile - --capture-output -p $PORT api:__hug_wsgi__
posts: gunicorn --access-logfile - --capture-output -p $PORT posts:__hug_wsgi__
likes: gunicorn --access-logfile - --capture-output -p $PORT likes:__hug_wsgi__
polls: gunicorn --access-logfile - --capture-output -p $PORT polls:__hug_wsgi__

email: python3 -m smtpd -n -c DebuggingServer localhost:5600
posts_worker: python3 posts_worker.py
polls_consumer: python3 pollsConsumer.py
likes_consumer: python3 likesConsumer.py
