FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y xinetd

COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY ./start.sh /start.sh
COPY ./flag.txt /flag.txt
COPY ./main.py /main.py
RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail

RUN useradd -M ctf && \
	chmod 744 /main.py && \
	chmod 744 /flag.txt && \
	chmod 744 /start.sh

CMD ["/start.sh"]

EXPOSE 9999
