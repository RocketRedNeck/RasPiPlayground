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
cd /var/run/user/1000/gvfs/afp-volume:host=KesseliMac.local,volume=Shared/RasPi/Ethan/SetupFiles/
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
#reboot to enact changes
echo ""
echo "All changes finished!!!"
echo "System will now reboot to inact changes..."
sudo reboot