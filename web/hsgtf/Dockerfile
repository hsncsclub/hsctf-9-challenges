FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine

RUN pip install --upgrade pip
COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY ./app /app

RUN addgroup -S ctf && adduser -S ctf -G ctf

ENV FLAG=flag{guessgod_nkdtcfpoghau} \
USER_FLAG=flag{fake_flag} \
ADMIN_SECRET=003db352756e870182e7360ed9d1bb3df2add8989374927a42ef39688c89304d \
LISTEN_PORT=8000
EXPOSE 8000
