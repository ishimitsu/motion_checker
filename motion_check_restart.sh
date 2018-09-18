#!/bin/sh

# Stop Daemons
service motion stop
service lighttpd stop

# Clear DB and record files
rm -f /var/lib/motion/*.jpg
mysql -u www_data -phogehoge motion_db -e "truncate table sleep_check;"

# Restart Daemons
motion -b
service lighttpd start
