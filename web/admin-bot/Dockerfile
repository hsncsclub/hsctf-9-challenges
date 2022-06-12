FROM node:14.16.0-buster-slim AS build

WORKDIR /app
RUN apt-get update && apt-get install -y \
  g++ make cmake unzip libcurl4-openssl-dev autoconf libtool python3 curl
COPY package.json yarn.lock ./
ENV NODE_ENV production
RUN yarn --frozen-lockfile && yarn cache clean

FROM node:14.16.0-buster-slim

WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
  libglib2.0-0 libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 \
  libxkbcommon0 libxcomposite1 libxdamage1 libxrandr2 libgbm1 libgtk-3-0 \
  libasound2 libxshmfence1 libx11-xcb1 && rm -rf /var/lib/apt/lists/*
COPY --from=build app/node_modules node_modules
COPY --from=build app/chromium chromium
COPY src .
COPY config.js .
USER node

ENV PORT=8080
EXPOSE 8080

CMD ["PORT=8080 node --unhandled-rejections=strict submit.js & PORT=8081 node --unhandled-rejections=strict visit.js"]
ENTRYPOINT [ "/bin/bash" ,"-c"]
# ENTRYPOINT ["node", "--unhandled-rejections=strict"]
