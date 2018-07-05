FROM tiagoantao/skates
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update && apt-get -y upgrade && apt-get install -y \
    ldap-utils \
    slapd \
    && rm -rf /var/lib/apt/lists

COPY copy/etc/supervisor.d/ldap.conf /etc/supervisor.d

COPY authorized_keys /root/.ssh
RUN chmod 0600 /root/.ssh/authorized_keys

VOLUME ["/etc/openldap", "/var/log/", "/var/lib/openldap/", "/var/run/openldap/"]

EXPOSE 636 389
