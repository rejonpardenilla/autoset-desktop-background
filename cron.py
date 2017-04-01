import sys, os, getpass
from crontab import CronTab

# command: 'python autoset.py' 
AUTOSET = '/usr/bin/python ' + os.getcwd() + '/autoset.py'


username = getpass.getuser()


# Schedule the command
# TODO: Obtain the hour of the day diffetently
cronjob = CronTab(user = username)
job = cronjob.new(command = AUTOSET)
job.setall('0 */4 * * *')  # every 4 hours
cronjob.write()