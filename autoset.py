import urllib, sys, os

# Random image url
IMG_URL = "https://source.unsplash.com/random"

# System script
SYS_SCRIPT = "gsettings set org.gnome.desktop.background picture-uri file://"+ os.getcwd() +"/img.jpg"

# Retrieve the image and execute the script
urllib.urlretrieve (IMG_URL, "img.jpg")
os.system(SYS_SCRIPT)
