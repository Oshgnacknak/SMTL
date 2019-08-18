FROM python:3.7

ENV SECRET_KEY ''
ENV SQLALCHEMY_DATABASE_URI 'sqlite:///:memory:'

ENV EMAIL_HOST ''
ENV EMAIL_PORT 587
ENV EMAIL_ADDR ''
ENV EMAIL_USER ''
ENV EMAIL_PASSWORD ''

ENV DEBUG 0
ENV HOST 0.0.0.0
ENV POST 5000

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY env_config.py ./config.py
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT [ "python", "./run.py" ]

