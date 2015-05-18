# the home nuker
Keep clean your LTSP Server's home folder


# Install

* Copy the script to the LTSP server.
* Setup cron to execute it every few hours.

Cron sample:

`30 */3 * * * python /opt/nuker/the_home_nuker.py > /var/log/nuker.log 2>&1`

