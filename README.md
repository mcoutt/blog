# blog

# Run redis server
`redis-server`

# Run celery worker
`pipenv run celery -A blog worker -B -l INFO`

# Run browser agent flower for celery
`pipenv run celery -A blog flower --port=6379`

# For run tests use next command
`pipenv run python blog/manage.py test news.tests`
