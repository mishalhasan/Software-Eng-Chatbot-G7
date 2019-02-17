const
  request = require('request');
  express = require('express'),
  port=process.env.PORT || 1337,
  bodyParser = require('body-parser'),
  app = express().use(bodyParser.json()); // creates express http server
  PAGE_ACCESS_TOKEN = "EAACERBMYr2QBACd6IgIbsO1HZAyICJycwakmXUTc5ezZBZCIYivgXeNnx8ZBeH6XHZCU0VnMKPtuomjdtGBHGACZA4DCO1Ir9regtW8JMrRN4EbFW2v5A2cc2htLZCKXyCIcE5MWDY2xgWpV8icxukxZA0RD0DEKdX10zff5wGNSMwZDZD"

  // Sets server port and logs message on success
  app.listen(port, () => console.log('webhook is listening to ' + port));

  // Creates the endpoint for our webhook 
app.post('/webhook', (req, res) => {  
 
    let body = req.body;
  
    // Checks this is an event from a page subscription
    if (body.object === 'page') {
  
      // Iterates over each entry - there may be multiple if batched
      body.entry.forEach(function(entry) {
  
        // Gets the message. entry.messaging is an array, but 
        // will only ever contain one message, so we get index 0
        let webhook_event = entry.messaging[0];
        console.log(webhook_event);

        // Get the sender PSID
        let sender_psid = webhook_event.sender.id;
        console.log('Sender PSID: ' + sender_psid);

        // Check if the event is a message or postback and
        // pass the event to the appropriate handler function
        if (webhook_event.message) {
            handleMessage(sender_psid, webhook_event.message);        
        } else if (webhook_event.postback) {
            handlePostback(sender_psid, webhook_event.postback);
        }
      });
  
      // Returns a '200 OK' response to all requests
      res.status(200).send('EVENT_RECEIVED');
    } else {
      // Returns a '404 Not Found' if event is not from a page subscription
      res.sendStatus(404);
    }
  });

  // Adds support for GET requests to our webhook
app.get('/webhook', (req, res) => {

    // Your verify token. Should be a random string.
    let VERIFY_TOKEN = "COSC310Bartender"
      
    // Parse the query params
    let mode = req.query['hub.mode'];
    let token = req.query['hub.verify_token'];
    let challenge = req.query['hub.challenge'];
      
    // Checks if a token and mode is in the query string of the request
    if (mode && token) {
    
      // Checks the mode and token sent is correct
      if (mode === 'subscribe' && token === VERIFY_TOKEN) {
        
        // Responds with the challenge token from the request
        console.log('WEBHOOK_VERIFIED');
        res.status(200).send(challenge);
      
      } else {
        // Responds with '403 Forbidden' if verify tokens do not match
        res.sendStatus(403);      
      }
    }
  });


  function handleMessage(sender_psid, received_message) {

    let response;

    received_message.sid = sender_psid;
    request({
      "uri": "http://localhost:8090/givenMessage",
      "method": "POST",
      "json": received_message
    }, (err, res, body) => {
      if (!err) {
        console.log('message sent to python!')
        console.log(typeof body)
        var string = JSON.stringify(body);
        var objectValue = JSON.parse(string);
        response = {"text" : body}; //parse the json body to string
        callSendAPI(sender_psid, response);   // Sends the response message
      } else {
        console.error("Unable to send message to python:" + err);
      }
    });
    
  }

  function callSendAPI(sender_psid, response) {
    // Construct the message body
    let request_body = {
      "recipient": {
        "id": sender_psid
      },
      "message": response
    }

    // Send the HTTP request to the Messenger Platform
  request({
    "uri": "https://graph.facebook.com/v2.6/me/messages",
    "qs": { "access_token": PAGE_ACCESS_TOKEN },
    "method": "POST",
    "json": request_body
  }, (err, res, body) => {
    if (!err) {
      console.log('message sent!')
    } else {
      console.error("Unable to send message:" + err);
    }
  }); 
  }
