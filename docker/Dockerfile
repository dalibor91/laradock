FROM debian:9 

MAINTAINER Dalibor Menkovic <dalibor.menkovic@gmail.com>

RUN apt-get update -y && \
	apt-get install -y 

RUN apt-get install -y curl mysql-server \
	apache2 vim build-essential libssl-dev 

#RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.0/install.sh | bash

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -

RUN apt-get install -y nodejs npm

#install php 
RUN apt-get install -y php7.0 \
	php7.0-mysql php-zip php7.0-mbstring php7.0-dom

RUN apt-get install -y libapache2-mod-php7.0
RUN a2enmod php7.0

RUN php -r " file_put_contents('c.php', file_get_contents('https://getcomposer.org/installer')); if (hash_file('SHA384', 'c.php') !== trim(file_get_contents('https://composer.github.io/installer.sig'))) { echo 'Corupted'.PHP_EOL; unlink('c.php'); exit(1); } " && \
    php c.php --install-dir=/usr/local/bin --filename=composer  && \
    rm c.php

RUN composer global require "laravel/installer"

RUN echo "\nPATH=\"\$PATH:\$HOME/.composer/vendor/bin\"" >> $HOME/.bashrc
RUN echo "\n127.0.0.1 laravel.dev" >> /etc/hosts

#custom install 
COPY docker/add /opt/add
RUN chmod +x /opt/add/onstart.sh

CMD ["/usr/sbin/apache2ctl","-DFOREGROUND"]

