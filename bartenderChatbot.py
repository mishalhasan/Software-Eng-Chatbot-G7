import nltk
import warnings
from textblob import TextBlob
from nltk.tag import pos_tag
from spell import correction
from nltk.corpus import wordnet



warnings.filterwarnings("ignore")

# nltk.download() # for downloading packages

import numpy as np
import random
import string # to process standard python strings
import os 

os.environ['NLTK_DATA'] = '~/nltk_data'
GREETING_INPUTS = ("greetings", "hi", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
GOODBYE_KEYWORDS = ("bye", "good bye", "farewell", "see ya")
GOODBYE_RESPONSES = ["Have a good night", "Drive safe!", "Until next time"]
HEDGE_RESPONSES = ["I have no idea what you're asking", "I'm not sure", "Can you re-phrase that?", "Pardon?", "Sorry I can't do that", "I'm confused"]
DRINKS = ("vodka", "beer", "whiskey", "wine", "sex on the beach", "screwdriver", "green fairy", "whiskey", "absinthe", "acapulco gold", "amaretto", "bacardi", "baileys" "budweiser", "champagne", "daiquiri", "goldschlager" "guinness", "grey goose", "hootch", "jack daniels", "jagermeister", "limoncello", "mezcal", "moonshine", "pina colada", "tequila", "vodka", "zinfandel", "raki", "long island iced tea"  )
DRINKSTYLE = ("on the rocks", "neat")#ask this after they request a drink
BARFOOD = ("nachos","wings","sliders")
YES_KEYWORDS = ("yes", "yeah", "certainly", "true", "yep", "yea", "okay", "exactly", "gladly")
YES_RESPONSES = ["Okay", "Sounds good", "I like it", "Thats great!", "Exciting!"]
NO_KEYWORDS = ("no", "nah", "negative", "not really", "never", "false", "nope")
NO_RESPONSES = ["That's too bad", "Suit yourself", "If you say so", "I insist"]
chat_log = {}

# Checking for greetings
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        word = correction(word)
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
        else:
            #check for synonyms 
            #check if synonym present in sample responses 
            s = getSynyms(word)
            for i in range(len(s)):
                if s[i] in GREETING_INPUTS: 
                    return random.choice(GREETING_RESPONSES)
                
def getSynyms(word):
    synms=[]
    #check for synonyms 
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synms.append(l.name())
    return synms

# checks to see if customer, asked for drink 
def checkForDrink(sent): 
    sentS = sent.split()
    for i in range(len(sentS)):
        sentS[i] = "drink"
        return True 
    return False 

def checkForDrinkRep(sent): 
    sentS = sent.split()
    for i in range(len(sentS)):
        sentS[i] = "drink"
        for i in range(len(DRINKS)):
            print(DRINKS[i])
        return TRUE  
    return False 

def checkForFood(sent): 
    word = sent.split()
    for i in range(len(word)):
        if (word[i] in BARFOOD):
            return True 
    return False 

# Generating response
def response(user_response, num_drinks):
    
    #spellCheck 
    input_words = user_response.split() # convert sentance to a list of words
    #print(input_words)
    word_list = []
    #spell check each word of the input
    for word in input_words:
        word_list.append(correction(word))
    corrected_input = ' '.join(word for word in word_list)
    user_response = corrected_input

    # Break the message into parts and check if aux verb was used 
    pronoun, noun, adjective, verb = getSpeechParts(user_response)
    if (checkAux(user_response) == True):
        return "Enjoy"

    #num_drinks = chat_log[senderId]['drinks_served']
    # Search for a drink in the user input and respond as well as we can
    drink = noun
    if drink not in DRINKS: #checks to see if possible noun, is a drink 
        drink = searchForDrink(user_response)
    if len(user_response) == 1:
        drink = user_response
    if drink in DRINKS:
        if num_drinks > 4:
            return "You are too drunk I am unable to serve you any more drinks. You can type 'clear' to tell me that you're sober again"
        #increment drink counter
        num_drinks = num_drinks + 1
        if num_drinks <= 1:
            return "One {0} coming right up!".format(drink)
        if num_drinks == 2:
            return "{0} for you, enjoy.".format(drink)
        else:
            return "Here is your {0}! Wow you've already had {1} drinks!".format(drink, num_drinks)
 
    #reset drink level for when sober 
    if user_response == "clear":
        num_drinks = 0 
        
    # Look for yes or no responses and respond with a weak hedge
    if checkForYes(user_response):
        return random.choice(YES_RESPONSES)
    if checkForNo(user_response):
        return random.choice(NO_RESPONSES)

    # If someone doesn't want anything
    if noun == "nothing":
        return "There isn't anything I can get for you? I am a master bar tender. You won't find any better."
    
    if  pronoun == "what": 
        checkForDrinkRep(user_response)
        

    #If we have a noun but no drink, we don't know what they want, so we answer with a question
    if noun:
        resp = []
        #if pronoun:
         #   resp.append(pronoun)
        if verb:
            v = verb[0]
            if v is not None:
                resp.append(v)
        if startsWithVowel(noun):
            noun_pronoun = "an"
        else:
            noun_pronoun = "a"
        resp.append(noun_pronoun + " " + noun + "?")
        return " ".join(resp)
    #If nothing caught, return a hedge
    return "I am sorry! I don't understand you " + random.choice( HEDGE_RESPONSES)
    

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent      
        
def createChatLog(senderId):
    '''Keeps track of each session ID in a dictionary'''
    log = {'times_contacted': 1, 'context': None, 'drinks_served': 0}
    chat_log[senderId] = log


def howManyMessages(senderId):
    '''Check the chat log for number of messages and increment accordinly.'''
    if senderId not in chat_log:
        createChatLog(senderId)
        #return value is number of messages received
        return 1
    else:
        times_con = chat_log[senderId]['times_contacted'] + 1
        chat_log[senderId]['times_contacted'] = times_con
        return times_con
def clearSession(senderId):
    '''Delete any data from the user session log'''
    chat_log[senderId]['times_contacted'] = 0
    chat_log[senderId]['drinks_served'] = 0


def CheckForGreeting(sentence):
    '''Return boolean if the user sentence contains a greeting'''
    for word in sentence.words:
        if word.lower() in GREETING_KEYWORDS:
            return True
    return False


def CheckForGoodbye(sentence):
    '''Return boolean if the user wants to leave/end the sesion'''
    for word in sentence.words:
        if word.lower() in GOODBYE_KEYWORDS:
            return True
    return False


def checkForYes(sentence):
    '''Return boolean if the user indicated a yes/true reply'''
    words = sentence.split() 
    for word in words:
        if word.lower() in YES_KEYWORDS:
            return True
    return False


def checkForNo(sentence):
    '''Return boolean if the user indicated a no/false reply'''
    words = sentence.split()
    for word in words:
        if word.lower() in NO_KEYWORDS:
            return True
    return False

def checkAux(sent):
    '''Return common answers for phrases commonly asked at a bar using the AUX present'''
    aux = None
    d = "drink" 
    sent2 = preprocess(sent)
    
    for word, part_of_speech in sent2:
        if part_of_speech == 'MD':
            if word == "can" or word == "may":
                if (checkForDrink(sent) == True):
                    reply = "Yes, we have a wide variety! Anything in partiular?" 
                    print(reply) 
                    return True 

                elif(checkForFood(sent) == True):
                    reply =  "Here is the menu! "
                    print(reply)
                    return True 
                
            return random.choice(YES_RESPONSES)
    return False 

def searchForDrink(sentence):
    '''Return boolean if the user sentence contains a drink'''
    words = sentence.split()
    for word in words:
        checkSynDr(word)
        if word.lower() in DRINKS:
            return word
    return None


def getSpeechParts(user_response):
    '''Use natural language processing to find and categorize each part of the sentance'''
    user_response.split("!")
    pronoun = None
    noun = None
    adjective = None
    verb = None
    s = preprocess(user_response)
    for word, part_of_speech in s: 
        pronoun = findPronoun(s)
        noun = findNoun(s)
        adjective = findAdjective(s)
        verb = findVerb(s)
    return pronoun, noun, adjective, verb


def findPronoun(sent):
    '''Return pronoun (I or You). Determins if the user is talking about
    themselves or the bot.
    Pronoun is represented as PRP in NLTK - check to see if its using who, what, etc. '''
    pronoun = None
    for word, part_of_speech in sent:
        if part_of_speech == 'PRP' and word.lower() == 'you':
            pronoun = 'I'
        elif part_of_speech == 'PRP' and word == 'I' or word == 'i':
            pronoun = 'You'
        elif part_of_speech == 'WP'and (word == "what"):
            pronoun = "what"
            
    return pronoun


def findVerb(sent):
    '''Return verb represended as VB in NLTK'''
    verb = None
    pos = None
    for word, part_of_speech in sent:
        if part_of_speech.startswith('VB'):  # This is a verb
            verb = word
            pos = part_of_speech
            break
    return verb, pos


def findNoun(sent):
    '''Return noun represended as NN in NLTK'''
    noun = None
    if not noun:
        for w, p in sent:
            if p == 'NN' and w != 'i':  # This is a noun
                #textblob detecting 'i' as a noun
                noun = w
                break
    return noun


def findAdjective(sent):
    '''Return adjective represended as JJ in NLTK'''
    adj = None
    for w, p in sent:
        if p == 'JJ':  # This is an adjective
            adj = w
            break
    return adj


def startsWithVowel(word):
    '''Used to check if a noun starts with a vowel
    then we can assign the proper pronoun'''
    return True if word[0] in 'aeiou' else False

def checkSynG(user_response):
    ''' Used to check for goodbye synonyms, as bye is our exit word with spell check 
    '''
    for word in user_response.split():
        word = correction(word)
        s = getSynyms(word)
        for i in range(len(s)):
            if s[i] in GOODBYE_KEYWORDS: 
                word = s[i]
                return word 
    return user_response 

def checkSynDr(word):
#checks to see if synonyms exist for drink 
    s = getSynyms(word)
    for i in range(len(s)):
        if s[i] in DRINKS: 
            word = s[i]
    return word 

flag=True

num_drinks = 0
counter = 0 
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    user_response = checkSynG(user_response)
    
 
    if(user_response not in GOODBYE_KEYWORDS):
        if(greeting(user_response)!=None):
            print(greeting(user_response) + "! I'm the bartender tonight!")

        else:
            resp = response(user_response,num_drinks)
            print(resp)
            num_drinks = num_drinks + counter 

    else:
        flag=False
        print(random.choice(GOODBYE_RESPONSES))    
