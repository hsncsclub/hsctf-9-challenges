FROM tiangolo/uwsgi-nginx-flask:python3.9

RUN apt-get update && apt-get -y upgrade && apt-get -y install sudo gcc cron

COPY ./shell.c /shell.c
RUN gcc -Wall -Wextra /shell.c -o /usr/local/bin/shell && rm /shell.c


RUN apt-get -y remove imagemagick imagemagick-6-common && apt-get -y autoremove \ 
	&& echo "deb [trusted=yes] https://snapshot.debian.org/archive/debian/20160104T164437Z/ jessie main" > /etc/apt/sources.list \
	&& apt-get autoclean && apt-get -o Acquire::Check-Valid-Until=false update \
	&& apt-get -y install imagemagick=8:6.8.9.9-5

COPY ./app /app
COPY ./flag.txt /app/flag.txt
COPY ./policy.xml /etc/ImageMagick-6/policy.xml

RUN groupadd -r ctf && useradd -M -r -g ctf ctf && \
	groupadd -r sub && useradd -M -r -g sub sub && \
	mkdir -p /upload/ && chown root:ctf /upload && chmod 773 /upload/ && \
	chmod 744 /app/flag.txt && \
	echo "ctf  ALL=(sub) NOPASSWD: ALL" >> /etc/sudoers && \
	echo "Defaults !requiretty" >> /etc/sudoers && \
	echo "sub hard nproc 64" >> /etc/security/limits.conf && \
	echo "session    required     pam_limits.so" >> /etc/pam.d/sudo && \
	echo "*/20 * * * * ctf rm -f /upload/*" >> /etc/crontab



ENV LISTEN_PORT=8000
EXPOSE 8000
