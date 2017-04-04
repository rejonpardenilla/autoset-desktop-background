# Autoset desktop background
A script that gets an image from a url and place it as your desktop background.

*Note: This only works for Linux Gnome

## Usage
First setup your Linux enviroment:
```sh
$ python setup.py
```

Then you can run manually the following command to change your desktop background:
```sh
$ python autoset.py
```

Also you can make a cronjob in your system, this tells your computer to execute autoset.py every 4 hours:
```sh
$ python cron.py
```

To remove the cronjob, simply:
```sh
$ crontab -r
```

## License
MIT
