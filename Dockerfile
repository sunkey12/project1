#stage 1
FROM python:3.9-slim-buster as linting
WORKDIR /usr/src
RUN pip install pylint
COPY *.py ./
RUN pylint *.py > check.txt  || exit 0


FROM python:3.10.0-alpine as building
WORKDIR /usr/src
COPY  *.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
