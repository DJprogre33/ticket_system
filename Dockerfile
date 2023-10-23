FROM python:3.11

WORKDIR /ticket_system

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["gunicorn", "--config", "app/gunicorn.conf.py", "app.main:app"]
