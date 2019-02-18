# Software-Eng-Chatbot
=============
## Prerequisites
* NodeJS
* Python 3
* Flask

## Installing
Example commands for installing the Chatbot on an Ubuntu or Debian server. Flask can be installed using pip. It would be good practice to use a python virtualenv if installing on a shared computer.
```console
user@server:~$ apt install nodejs 
user@server:~$ apt install npm
user@server:~$ apt install python3-pip
user@server:~$ pip3 install flask
user@server:~$ apt install git
user@server:~$ git clone https://github.com/RaphaelChevallier/Software-Eng-Chatbot-G7.git
user@server:~$ cd Software-Eng-Chatbot-G7/
user@server:~$ npm install
```
## Running
Once installed, run flask and node as background processes.
```console
user@server:~$ node webhook.js &
user@server:~$ python3 bartenderChatbot.py &
```
