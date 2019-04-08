FROM python:3.5.7-slim-jessie
COPY . /src
CMD ["python", "/src/lcd.py"]