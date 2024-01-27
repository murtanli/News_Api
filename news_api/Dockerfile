FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/news_api

COPY ./req.txt /usr/src/req.txt
RUN pip install -r /usr/src/req.txt

COPY . /usr/src/news_api

EXPOSE 8000
#RUN python manage.py makemigrations
#RUN python manage.py migrate
CMD ["python manage.py runserver 0.0.0.0:8100"]
