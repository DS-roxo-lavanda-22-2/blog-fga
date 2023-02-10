FROM python:3.8-slim-buster

WORKDIR /app
RUN pip3 install Django

COPY . /app

# RUN python3 manage.py migrate

# RUN python3 manage.py makemigrations fga


ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]