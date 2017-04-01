import sys, os
from crontab import CronTab

# command: 'python autoset.py' 
AUTOSET = '/usr/bin/python ' + os.getcwd() + '/autoset.py'

# TODO: Obtain the username differently
username = raw_input('Input yout username: ')

# Schedule the command
# TODO: Obtain the hour of the day diffetently
cronjob = CronTab(user = username)
job = cronjob.new(command = AUTOSET)
job.setall('0 12 * * *')  # every day at 12:00 hrs 
cronjob.write()