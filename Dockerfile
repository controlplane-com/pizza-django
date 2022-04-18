FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY pizza_app/requirements.txt .
RUN pip install -r requirements.txt


COPY . .

EXPOSE 8080
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8080" ]