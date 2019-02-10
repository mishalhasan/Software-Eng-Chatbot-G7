from flask import Flask
from flask import request

def createMessage(input): #change this method and anything to create the message wanted to facebook. input paramter is message coming in
    return 'JSON posted'  #this will return the wanted message back out to messenger









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

