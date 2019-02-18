# Software-Eng-Chatbot
## 310 Assignment 2: CHAT BOT
## USER GUIDE
Aaron Mahnic
Ansa Erturk
Mishal Hasan
Raphael Chevallier
Tyrel Narciso

## Introduction
For this assignment, we built a chat bot to mimic basic bartending needs. Built with basic functionality that can accept a text entry and respond with a logical statement. Our bot uses pattern matching and recognizes “aggressive” words instead of adapting a more complex contextual recognition approach. The app is accessible through Facebook and can be easily interacted with through the messenger.

# Install Chatbot to own server
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
