#Update the PI
sudo rpi-update

#Setup bash and VI so backspace/delete work properly

#Set keyboard to English (US)
echo "You need to set keyboard to English(US)"
sudo raspi-config

#Install SimpleCV
sudo apt-get install ipython python-opencv python-scipy python-numpy python-setuptools python-pip

#Install PiCamera
sudo apt-get install python-picamera
