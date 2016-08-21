echo "Hello! This shell file will setup your system with"
echo "some programs! Let's begin!"
echo ""
echo "Setting keyboard to US format..."
setxkbmap us
echo "Done!"
echo ""
echo "Updating all files..."
sudo apt-get update
echo "Update complete!"
echo ""
echo "Installing Iceweasel web browser..."
sudo apt-get install iceweasel
echo "Install of Iceweasel complete!"