#!/bin/sh

# Stop Daemons
# service motion stop
killall motion
service lighttpd stop

# Clear DB and record files
# rm -f /var/lib/motion/*.jpg /var/lib/motion/*.avi
rm -rf /var/lib/motion/*
mysql -u www_data -phogehoge motion_db -e "truncate table sleep_check;"

# Restart Daemons
motion -b
service lighttpd start
