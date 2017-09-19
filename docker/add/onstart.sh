#!/bin/bash

if [ -d "/opt/add/vhosts" ];
then
	for i in $(ls "/opt/add/vhosts");
	do 
		cp "/opt/add/vhosts/${i}" "/etc/apache2/sites-available/${i}"
		ln -s "/etc/apache2/sites-available/${i}" "/etc/apache2/sites-enabled/${i}"
	done

	rm -rf /opt/add/vhosts
	cd /var/www/app
	composer create-project --prefer-dist laravel/laravel .
fi


