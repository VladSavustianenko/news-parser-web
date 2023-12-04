docker build -t parser .
docker run parser
web: gunicorn -w 1 "app:app" -t 120