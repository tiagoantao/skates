FROM debian:testing-slim
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    bash \
    libnss-ldap \
    libpam-ldap \
    locales \
    openssh-server \
    python3 \
    supervisor \
    wget \
    && rm -rf /var/lib/apt/lists/*

#You probably also need a /etc/ldap.conf

#Explain prepare magic somewhere

#Install Linking of configuration files and entrypoint
COPY copy/sbin/link_mutable_files.py /sbin/link_mutable_files.py
COPY copy/sbin/server_run.sh /sbin
RUN chmod a+x /sbin/server_run.sh /sbin/link_mutable_files.py
RUN mkdir /traverse

COPY copy/etc/supervisor/conf.d/supervisor.conf /etc/supervisor/conf.d/
COPY copy/etc/supervisor/conf.d/supervisor-sshd.conf /etc/supervisor/conf.d/

RUN mkdir /var/run/sshd
RUN mkdir /root/.ssh

#EXPOSE 22

CMD ["/sbin/server_run.sh"]
