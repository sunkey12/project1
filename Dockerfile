FROM python:3.10.0-alpine
WORKDIR /usr/src
COPY  *.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
