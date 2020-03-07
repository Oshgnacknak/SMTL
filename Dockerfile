FROM node:alpine

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install

ENV COOKIE_PASSWORD 'CHANGE ME ASAP'
ENV MONGO_URL 'mongodb://mongo/SMTL'
ENV MINOR_BIRTH_YEAR 2002
ENV SENIOR_BIRTH_YEAR 1961

EXPOSE 3000

COPY . .

CMD [ "node", "index.js" ]
