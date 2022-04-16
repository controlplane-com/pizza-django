FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY . /code/

RUN python -m pip install Django
# RUN pip install requests xmltodict rest_framework
RUN pip install -r pizza_app/requirements.txt


EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]