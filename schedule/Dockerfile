FROM node:lts-slim

WORKDIR /srv/app/

ENV PATH /srv/app/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./
RUN npm install

EXPOSE 5173

COPY . ./