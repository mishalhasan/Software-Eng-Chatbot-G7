from flask import Flask
from flask import request
from textblob import TextBlob
import random
import json
import os

os.environ['NLTK_DATA'] = '~/nltk_data'
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up", "hi there")
GREETING_RESPONSES = ["What can I get you?", "Hello stranger, what can I serve up for you?", "Need a drink?", "Hi, hope you're thirsty. What can I get you?"]
HEDGE_RESPONSES = ["I have no idea what you're asking", "I'm not sure", "Can you re-phrase that?", "Pardon?", "Sorry I can't do that", "I'm confused"]
DRINKS = ("vodka", "beer", "whiskey", "wine")
chat_log = {}


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


def respond(input_msg, senderId):
    if input_msg.lower() == 'clear':
        chat_log[senderId]['times_contacted'] = 0
        return "Session cleared"
    times_con = how_many_messages(senderId)
    if check_for_greeting(input_msg) and times_con == 1:
        return random.choice(GREETING_RESPONSES)
    pronoun, noun, adjective, verb = get_speech_parts(input_msg)
    num_drinks = chat_log[senderId]['drinks_served']
    if num_drinks > 3:
        return "You are too drunk I am unable to serve you any more drinks. You can type 'clear' to tell me that you're sober again"
    if noun:
        if noun in DRINKS:
            #increment drink counter
            chat_log[senderId]['drinks_served'] = num_drinks + 1
            if num_drinks > 1:
                return "One {0} coming right up!".format(noun)
            if num_drinks > 1:
                return "Heres your {0}! Wow you've already had {1} drinks!".format(noun, num_drinks)
    return random.choice(HEDGE_RESPONSES)


def check_for_greeting(sentence):
    for word in sentence.words:
        if word.lower() in GREETING_KEYWORDS:
            return True
    return False


def get_speech_parts(input_msg):
    pronoun = None
    noun = None
    adjective = None
    verb = None
    for s in input_msg.sentences:
        pronoun = find_pronoun(s)
        noun = find_noun(s)
        adjective = find_adjective(s)
        verb = find_verb(s)
    return pronoun, noun, adjective, verb


def find_pronoun(sent):
    pronoun = None
    for word, part_of_speech in sent.pos_tags:
        if part_of_speech == 'PRP' and word.lower() == 'you':
            pronoun = 'I'
        elif part_of_speech == 'PRP' and word == 'I':
            pronoun = 'You'
    return pronoun


def find_verb(sent):
    verb = None
    pos = None
    for word, part_of_speech in sent.pos_tags:
        if part_of_speech.startswith('VB'):  # This is a verb
            verb = word
            pos = part_of_speech
            break
    return verb, pos


def find_noun(sent):
    noun = None
    if not noun:
        for w, p in sent.pos_tags:
            if p == 'NN' and w != 'i':  # This is a noun
                #textblob detecting 'i' as a noun
                noun = w
                break
    return noun


def find_adjective(sent):
    adj = None
    for w, p in sent.pos_tags:
        if p == 'JJ':  # This is an adjective
            adj = w
            break
    return adj


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
