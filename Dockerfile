FROM python:3.10
WORKDIR /api

RUN apt-get update && apt-get install -y libpq-dev
RUN pip install Flask Flask-RESTful Flask-SQLAlchemy Flask-Cors 
RUN pip install psycopg2

COPY . .

CMD python server.py