# Software-Eng-Chatbot
## 310 Assignment 2: CHAT BOT
## USER GUIDE
Aaron Mahnic,
Ansa Erturk,
Mishal Hasan,
Raphael Chevallier,
Tyrel Narciso

## Introduction
For this assignment, we built a chat bot to mimic basic bartending needs. Built with basic functionality that can accept a text entry and respond with a logical statement. Our bot uses pattern matching and recognizes “aggressive” words instead of adapting a more complex contextual recognition approach. The app is accessible through Facebook and can be easily interacted with through the messenger.

## Infrastructure
The bartender chatbot uses facebook as a front-end.  Communication with facebook is done through a nodeJS webhook that passes the message data to a python service (flask) which processes the user's message and responds accordingly. In order to readily communicate with facebook, the chatbot is currently installed and running on a dedicated linux server. The flask chatbot bartenderChatbot.py can run as a stand-alone chatbot service and hook into any kind of front end interface with minimal changes. Chat flow when user messages the bot follows the steps below.
* User messages chatbot on facebook
* Facebook API
* Nginx Forward proxy (for SSL termination) 
* Node JS
* Flask chatbot receives message and the reply is taken back up the chain

## Libraries
* NLTK/TextBlob - Python framework used for natural language processing
* Flask - Python web framework used to communicate with POST requests

## Gain Permission to Access Chatbot
As facebook requires for any app on their services to be reviewed, our chatbot app is not accessible to the public. Awaiting facebook to review an app may take a while so for the meantime we need to authorize test users to access the chatbot through messenger. If you wish to test our app please contact raphaelchevallier@hotmail.com and pass your facebook ID or username. Once approved we will send back an invite to that facebook id/username and you will need to direct yourself to https://developers.facebook.com/ and accept the invite to be a tester. Once accepted, travel to https://www.facebook.com/Bartender-Chatbot-310-594256287663533/
and message the page. The chatbot will respond back to you and will be fully functional to you.

## Potential Improvements
Although the system’s functionality is efficient as a basic bot, it can be improved by adding data outside the context of a bar and by populating the existing categories (eg. drinks). More elaborate methods can be added to detect false positives after an advanced contextual recognition algorithm is implemented. 

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
