echo "This Shell Script will copy your present panel setup to the network"
echo "so you can restore it with sysSetup.sh..."
cd ~/.config/lxpanel/LXDE-pi/
cp -r -i panels/ /var/run/user/1000/gvfs/afp-volume\:host\=KesseliMac.local\,volume\=Shared/RasPi/Michael/SetupFiles
cd ~
echo "Copy complete!"