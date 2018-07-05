FROM tiagoantao/skates
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update && apt-get -y upgrade && apt-get install -y \
    ldap-account-manager \
    nginx-full \
    php-fpm \
    && rm -rf /var/lib/apt/lists


RUN mkdir /run/php
COPY copy/etc/supervisor/conf.d/web.conf /etc/supervisor/conf.d
COPY authorized_keys /root/.ssh
COPY copy/etc/nginx/cert.key /etc/nginx
COPY copy/etc/nginx/cert.pem /etc/nginx
COPY copy/etc/nginx/nginx.conf /etc/nginx
#COPY copy/etc/phpldapadmin/config.php /etc/phpldapadmin

VOLUME ["/var/log"]

EXPOSE 443

