FROM python:3.7

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["gunicorn", "-c", "./gunicorn.py", "app:app"]
EXPOSE 5000