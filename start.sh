echo "Cloning Repo, Please Wait..."
git clone -b master https://github.com/Pr0fess0r99/LuciferFilter-RoboT.git /Pr0fess0r99 
cd /Pr0fess0r99 
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
