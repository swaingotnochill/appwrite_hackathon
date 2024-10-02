FROM python:3.10-alpine
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 6969
COPY . .
CMD ["python3", "main.py"]
