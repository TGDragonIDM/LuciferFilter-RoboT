echo "Cloning Repo, Please Wait..."
git clone -b main https://github.com/PR0FESS0R-TG/LuciferFilter-RoboT.git /LuciferFilter-RoboT
cd /LuciferFilter-RoboT
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
