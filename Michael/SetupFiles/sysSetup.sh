echo "Hello! This shell file will setup your system with"
echo "some programs! Let's begin!"
echo ""
# keyboard
echo "Setting keyboard to US format..."
setxkbmap us
echo "Done!"
echo ""
#timezone
echo "Changing timezone to US/Arizona..."
echo "see http://www.thegeekstuff.com/2010/09/change-timezone-in-linux/ for info."
cd /etc
sudo rm localtime
cd /etc
sudo ln -s /usr/share/zoneinfo/US/Arizona localtime
cd ~
echo "Timezone changed!"
echo ""
#taskbar
echo "Customizing taskbar to settings in the panel file..."
#cd /var/run/user/1000/gvfs/smb-share\:server\=kesselimac.local\,share\=shared/RasPi/Ethan/SetupFiles/
cd /var/run/user/1000/gvfs/afp-volume\:host\=Kesselimac.local\,volume\=Shared/RasPi/Michael/SetupFiles/
cp -r -i panels/ ~/.config/lxpanel/LXDE-pi/
cd ~
echo "Taskbar setup complete!"
echo ""
#fileupdate
echo "Updating all files..."
sudo apt-get update
echo "Update complete!"
echo ""
#iceweasel
echo "Installing Iceweasel web browser..."
sudo apt-get install iceweasel
echo "Install of Iceweasel complete!"
echo "Installing Tight VNC Server..."
sudo apt-get install tightvncserver
echo "Install of Tight VNC Server complete!"
echo "Installing X11 VNC Server..."
sudo apt-get install x11vnc
echo "Install of X11 VNC Server complete!"
#Download Arduino directly and install
#echo "Installing Arduino..."
#sudo apt-get install arduino
#echo "Install of Arduino complete!"
echo "Copying .bashrc..."
cp -i /var/run/user/1000/gvfs/afp-volume\:host\=Kesselimac.local\,volume\=Shared/RasPi/Michael/SetupFiles/.bashrc ~/.bashrc
#reboot to enact changes
echo ""
echo "All changes finished!!!"
echo "System will now reboot to inact changes..."
sudo reboot