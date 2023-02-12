echo "Cloning Repo, Please Wait..."
git clone -b main https://github.com/Pr0fess0r99/LuciferFilter-RoboT.git /LuciferFilter-RoboT
cd /LuciferFilter-RoboT
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
