FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install psycopg2
RUN pip install gunicorn
COPY truckLocator/uszips.csv /app/
COPY . .




