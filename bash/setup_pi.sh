echo "Change the Default Password"
sudo :passwd

echo "Change the hostname"
sudo nano /etc/hostname

#Update the PI
echo "Updating the Raspberry PI"
sudo rpi-update

echo "Install Avahi Daemon to make SSH easier"
#allows ssh@hostname.local instead of ip address
sudo apt-get install avahi-daemon

#Setup bash and VI so backspace/delete work properly
echo "Setup BASH/VI"

#Set keyboard to English (US)
echo "You need to set keyboard to English(US)"
sudo raspi-config

#Install SimpleCV
echo "Installing SimpleCV"
sudo apt-get install ipython python-opencv python-scipy python-numpy python-setuptools python-pip



#Install PiCamera
echo "Install PiCamera"
sudo apt-get install python-picamera


echo "Install TightVNC for Remote Desktop"
sudo apt-get install tightvncserver
echo "Set TightVNC password"
/usr/bin/tightvncserver
echo "Set autostart TightVNC
#get script from github
sudo mv tightvncserver-init.txt /etc/init.d/tightvncserver
sudo chown root:root /etc/init.d/tightvncserver
sudo chmod 755 /etc/init.d/tightvncserver
sudo upddate-rc.d tightvncserver defaults
echo "make sure host connects to pi with ssh and tunnels L5901 localhost:5901"


