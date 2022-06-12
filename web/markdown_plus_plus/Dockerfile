FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine

RUN pip install --upgrade pip
COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY ./app /app

RUN addgroup -S ctf && adduser -S ctf -G ctf

ENV FLAG=flag{waterfall_bfutsftfejpk} \
SECRET=0b752ed24ec5b5fc814541f0f3b789ea910e693e0b79c1db4b71296a9c177b2e \
LISTEN_PORT=8000
EXPOSE 8000
