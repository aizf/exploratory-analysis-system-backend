FROM python:alpine

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "gunicorn", "-c", "./gunicorn.py", "app:app"]
EXPOSE 5000