# Software-Eng-Chatbot	# Software-Eng-Chatbot
## 310 Assignment 2: CHAT BOT	## 310 Assignment 3: CHAT BOT
## USER GUIDE	## USER GUIDE
Aaron Mahnic,	Mishal Hasan
Ansa Erturk,	
Mishal Hasan,	
Raphael Chevallier,	
Tyrel Narciso	


 ## Introduction	## Introduction
For this assignment, we built a chat bot to mimic basic bartending needs. Built with basic functionality that can accept a text entry and respond with a logical statement. Our bot uses pattern matching and recognizes “aggressive” words instead of adapting a more complex contextual recognition approach. The app is accessible through Facebook and can be easily interacted with through the messenger.	For this assignment, we built a chat bot to mimic basic bartending needs. Built with basic functionality that can accept a text entry and respond with a logical statement. Our bot uses pattern matching and recognizes “aggressive” words instead of adapting a more complex contextual recognition approach. The app was initially accessible through Facebook and can be easily interacted with through the messenger. As of now, it is using a simple input form as messenger regulations on number of people has caused a change in interface. 


 ## Infrastructure	## Infrastructure
The bartender chatbot uses facebook as a front-end.  Communication with facebook is done through a nodeJS webhook that passes the message data to a python service (flask) which processes the user's message and responds accordingly. In order to readily communicate with facebook, the chatbot is currently installed and running on a dedicated linux server. The flask chatbot bartenderChatbot.py can run as a stand-alone chatbot service and hook into any kind of front end interface with minimal changes. Chat flow when user messages the bot follows the steps below.	The bartender chatbot uses python as the backend with a combination of other libraries.       
* User messages chatbot on facebook	
* Facebook API	
* Nginx Forward proxy (for SSL termination) 	
* Node JS	
* Flask chatbot receives message and the reply is taken back up the chain	


 ## Libraries	## Libraries
* NLTK/TextBlob - Python framework used for natural language processing	* NLTK/TextBlob - Python framework used for natural language processing
* Flask - Python web framework used to communicate with POST requests	* Flask - Python web framework used to communicate with POST requests


 ## Gain Permission to Access Chatbot	
As facebook requires for any app on their services to be reviewed, our chatbot app is not accessible to the public. Awaiting facebook to review an app may take a while so for the meantime we need to authorize test users to access the chatbot through messenger. If you wish to test our app please contact raphaelchevallier@hotmail.com and pass your facebook ID or username. Once approved we will send back an invite to that facebook id/username and you will need to direct yourself to https://developers.facebook.com/ and accept the invite to be a tester. Once accepted, travel to https://www.facebook.com/Bartender-Chatbot-310-594256287663533/	
and message the page. The chatbot will respond back to you and will be fully functional to you.	

 ## Potential Improvements	## Potential Improvements
Although the system’s functionality is efficient as a basic bot, it can be improved by adding data outside the context of a bar and by populating the existing categories (eg. drinks). More elaborate methods can be added to detect false positives after an advanced contextual recognition algorithm is implemented. 	Although the system’s functionality is efficient as a basic bot, it can be improved by adding data outside the context of a bar and by populating the existing categories (eg. drinks). More elaborate methods can be added to detect false positives after an advanced contextual recognition algorithm is implemented. The chatbot is still very restrictive but adding more responses has resulted in more flexibility. Beforehand, the bot was barely able to answer responses and much was hardcoded in. The bot is now able to answer a little more complex responses but is still restrictive. 


 # Install Chatbot to own server	## New Features 
## Prerequisites
