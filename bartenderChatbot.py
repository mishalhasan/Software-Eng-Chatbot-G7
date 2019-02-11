from flask import Flask
from flask import request
import json

def createMessage(input): #change this method and anything to create the message wanted to facebook. input paramter is message coming in
    data = input['text'] #grab the text of the input json. Now the input is just a string 'data' to work with

    print("what the input is: ") #testing the input and doing some processes to see if we can respond correctly. We can!
    print(data)
    print(type(data))
    data = data + " I am echoing what you say!"
    data = data + " I am doing some processes on the input rn! This works so well"
    return data  #this will return the wanted message back out to messenger









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

