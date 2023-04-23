#stage 1
FROM python:3.9-slim-buster as linting
WORKDIR /app
RUN pip install pylint
COPY *.py ./
RUN pylint *.py > check.txt  || exit 0


FROM python:3.10.0-alpine as building
WORKDIR /app
COPY  *.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
