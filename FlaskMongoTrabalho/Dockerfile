FROM python:3.9.1

WORKDIR /FlaskMongoTrabalho

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]