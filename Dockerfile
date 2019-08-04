FROM python:3.7

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY env_config.py ./config.py
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "./run.py" ]

