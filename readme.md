# Let's start selenium chrome browser with tor
## Instructions to run the project in Linux
### Install tor
> sudo apt-get install tor

### Install pip3
> python3 -m pip install --user --upgrade pip

### Installing virtualenv
> python3 -m pip install --user virtualenv

### Creating a virtual environment¶
> python3 -m venv env

### Activating a virtual environment¶
> source env/bin/activate

### Installing packages
> python3 -m pip install -r requirements.txt

## RUN PROJECT
> python3 main.py
### Chrome browser will be run three times to check IP addresses is changed and it really works!

# ATTENTION:
### `You can also specify countr IP addresses if you want to you to make some changes into tor files `
> sudo nano /etc/tor/torrc
#### for example if you want to make it france add the following code in the end of torrc file, also you can use multiple countrys ip {fr,gr} ....
> EntryNodes {fr} StrictNodes 1
> ExitNodes {fr} StrictNodes 1  

### Make sure you you have `log` folder where your script `main.py` is located
### Make sure you you secret information/credentials is correct and inserted in `.env` file and this file located where your script `main.py`
### Make Sure you completed all the steps before the script was executed

#### This chromedriver is for `101.0.4951.64` chrome browser. if your chrome browser dont support, you need to install same version of Chrome
> https://chromedriver.chromium.org/downloads

## GOOD LUCK !