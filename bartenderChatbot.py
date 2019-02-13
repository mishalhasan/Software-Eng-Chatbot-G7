from flask import Flask
from flask import request
from textblob import TextBlob
import json

def createMessage(input): #change this method and anything to create the message wanted to facebook. input paramter is message coming in
    input_msg = TextBlob(input['text'])
    data = respond(input_msg)
    #print("what the input is: ") #testing the input and doing some processes to see if we can respond correctly. We can!
    #print(data)
    #print(type(data))
    #data = data + " I am echoing what you say!"
    #data = data + " I am doing some processes on the input rn! This works so well"

    return data  #this will return the wanted message back out to messenger



GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)
GREETING_RESPONSES = ["What can I get for ya?", "You again?"]


def respond(input_msg):
    if check_for_greeting(input_msg):
        return random.choice(GREETING_RESPONSES)
    else:
        return input_msg


def check_for_greeting(sentence):
    for word in sentence:
        if word.lower() in GREETING_KEYWORDS:
            return True
    return False


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

