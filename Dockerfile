FROM python:3.8.5-alpine
COPY ./project /app
WORKDIR /app
RUN pip install -r requirements.txt

ENV FLASK_APP=app.py
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]