FROM tiangolo/uwsgi-nginx-flask:python3.9

COPY ./app /app
COPY ./images /images
COPY flag.txt /flag.txt
RUN chmod 744 /flag.txt && chmod 755 /images
RUN groupadd -r ctf && useradd -M ctf -g ctf

ENV LISTEN_PORT=8000
EXPOSE 8000
