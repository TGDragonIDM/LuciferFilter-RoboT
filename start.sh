if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/PR0FESS0R-TG/LuciferFilter-RoboT.git /LuciferFilter-RoboT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /LuciferFilter-RoboT
fi
cd /LuciferFilter-RoboT
pip3 install -U -r requirements.txt
echo "Starting Lucifer Filter RoboT..."
python3 bot.py
