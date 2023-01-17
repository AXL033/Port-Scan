# 🔗 Scanning Ports
Good day dear GitHub user, I am glad that you decided to use this tool to check what ports are open on websites 🌐. Let me tell you a little bit about this script, what it has:
+ The script does not scan all ports, but only a certain set of ports (there are 50 of them) 🔴
+ The script works fast enough, and will work for any device, whether it is Termux, Window, or Linux ⚪

And so let's figure out how to install this script on your device ⏯
## 🔗 Termux
To run the script on the Termux terminal, simply copy the commands below:
```
apt update && apt upgrade -y
pkg install git
pkg install python3
git clone https://github.com/AXL033/Port-Scan.git
cd ./Port-Scan
python -m pip install --upgrade pip
pip install -r ./requirements.txt
python3 ./port.py
```
And the program (script) will run in your terminal, then type in the IP address and wait for the scan :)
## 🔗 Windows
In order to install this program (script) on Windows, we need Python version 3. You can download it from [official website 🐍](https://www.python.org/downloads).
Next, we need to download the ZIP archive from GitHub and unzip it, then go to the directory with the script, and install the dependencies with the following command:
```
pip install -r ./requirements.txt
```
Once all dependencies are installed, we can run the script with the command:
```
python ./port.py
```
Hope you found what you were looking for, have fun! 😁
