# Dockerfile
FROM node:14.17.6-alpine3.13

# create destination directory
RUN mkdir -p /usr/src/frontend
WORKDIR /usr/src/frontend

# update and install dependency
RUN apk update && apk upgrade
RUN apk add git

# copy the app, note .dockerignore
COPY . /usr/src/frontend
RUN npm install
RUN npm run build

RUN npm install @nuxtjs/axios
RUN npm install -D tailwindcss@^3 postcss@latest autoprefixer@latest @nuxt/postcss8
# RUN npm install -D @tailwindcss/aspect-ratio @tailwindcss/forms @tailwindcss/line-clamp @tailwindcss/

EXPOSE 3000

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

# For development purposes
CMD [ "npm", "run", "dev" ]

# For production purposes
# RUN npm run build
# CMD [ "npm", "run", "start" ]