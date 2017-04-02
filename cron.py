import sys, os, getpass
from crontab import CronTab

# command: 'python autoset.py' 
AUTOSET = '/usr/bin/python ' + os.getcwd() + '/autoset.py'

username = getpass.getuser()


# Schedule the command
cronjob = CronTab(user = username)
job = cronjob.new(command = AUTOSET)
job.setall('* * * * *')  # every minute (just for testing purposes)
cronjob.write()


# Print info about the cronjob
print('Cronjob created:')
os.system('crontab -l')
