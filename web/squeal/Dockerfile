FROM node:16-buster

ENV NODE_ENV production

WORKDIR /app
COPY package.json /app/
RUN npm install

COPY public/ /app/public
COPY index.js /app/index.js

ENV USERNAME=admin \
	PASSWORD=5a6c186d4d4aa527e20496fcb977f43dd6ec3c3c88deb8f6cbcff07e05fff83f \
	FLAG=flag{squ34l_n0t_sql}

ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

CMD [ "node","index.js" ]

EXPOSE 3000