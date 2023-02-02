if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Kuchh-Bhi/rk.git /rk
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /rk
fi
cd /rk
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
