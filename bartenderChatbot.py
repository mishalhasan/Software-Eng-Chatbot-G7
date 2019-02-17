from flask import Flask
from flask import request
from textblob import TextBlob
import random
import json

def createMessage(input): #change this method and anything to create the message wanted to facebook. input paramter is message coming in
    input_msg = TextBlob(input['text'])
    senderId = input['sid']
    data = respond(input_msg, senderId)
    print(chat_log)
    #print("what the input is: ") #testing the input and doing some processes to see if we can respond correctly. We can!
    #print(data)
    #print(type(data))
    #data = data + " I am echoing what you say!"
    #data = data + " I am doing some processes on the input rn! This works so well"
    return str(data)  #this will return the wanted message back out to messenger


def how_many_messages(senderId):
    if senderId not in chat_log:
        log = {'times_contacted': 1, 'context': 'null', 'drinks_served': 0}
        chat_log[senderId] = log
        return 1
    else:
        times_con = chat_log[senderId]['times_contacted'] + 1
        chat_log[senderId]['times_contacted'] = times_con
        return times_con


GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up", "hi there")
GREETING_RESPONSES = ["What can I get you?", "Hello stranger, what can I serve up for you?", "Need a drink?", "Hi, hope you're thirsty. What can I get you?"]
chat_log = {}


def respond(input_msg, senderId):
    if input_msg.lower() == 'clear':
        chat_log[senderId]['times_contacted'] = 0
        return "Session cleared"
    times_con = how_many_messages(senderId)
    if check_for_greeting(input_msg) and times_con == 1:
        return random.choice(GREETING_RESPONSES)
    if times_con > 3:
        return "You are too drunk I am unable to serve you any more drinks. You can type 'clear' to tell me that you're sober again"
    else:
        return input_msg


#all code above this created API
app = Flask(__name__) #create the app server to recieve json

@app.route('/givenMessage', methods = ['POST'])
def postJsonHandler():
    print (request.is_json)
    content = request.get_json()
    print (content)
    message = createMessage(content)
    #return 'JSON posted'
    return message

app.run(host = '0.0.0.0', port = 8090)

