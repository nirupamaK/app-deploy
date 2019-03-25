FROM python:3
RUN mkdir /backend-challenge
WORKDIR /backend-challenge
COPY backend-challenge ./
RUN pip install -r requirements.txt
RUN python manage.py migrate
EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
