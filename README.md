## 310 Assignment 3: CHAT BOT
Mishal Hasan

## Introduction
For this assignment, we built a chat bot to mimic basic bartending needs. Built with basic functionality that can accept a text entry and respond with a logical statement. Our bot uses pattern matching and recognizes “aggressive” words instead of adapting a more complex contextual recognition approach. The app was initially accessible through Facebook and can be easily interacted with through the messenger. As of now, it is using a simple input form as messenger regulations on number of people has caused a change in interface.

## Infrastructure
The bartender chatbot uses python as the backend with a combination of other libraries. 

## Libraries

NLTK - Python framework used for natural language 

## Improvements

Although the system’s functionality is efficient as a basic bot, it can be improved by adding data outside the context of a bar and by populating the existing categories (eg. drinks). More elaborate methods can be added to detect false positives after an advanced contextual recognition algorithm is implemented. The chatbot is still very restrictive but adding more responses has resulted in more flexibility. Beforehand, the bot was barely able to answer responses and much was hardcoded in. The bot is now able to answer a little more complex responses but is still restrictive. 

## New Features 
Initially, the bot was using NLTK but was not fully utilizing the parts of speech. Utilizing this library, the bot is able to actually analyze and label parts of speech. Furthermore, initially, the NLTK was only using basic pos but now have started to specify specialized portion of the speech such as modal,"MD", allowing to answer based off of questioning input. Since, the program was developed using Python, incorporated synonym recognition allowing more flexibility. Now users have more of a range as to what they can an ask. Initially, we had a string list of words that could be used but now the system accepts synonyms of for the categories listed. The program is also more flexible because of spelling. It now accepts slight variation to the original words. 

## DFD Level 0 

![DFD LEVEL 0](https://github.com/mishalhasan/Software-Eng-Chatbot-G7/blob/master/Screen%20Shot%202019-04-05%20at%2010.07.24%20PM.png)

  1. POS tagging: tags part of speech 
  2. user input: console text input 
  3. screen: displays result of chat 
  4. flexibility/adaptibility: infuses synonym and spellinng that is less restrictive 

## DFD Level 1 

![DFD LEVEL 1](https://github.com/mishalhasan/Software-Eng-Chatbot-G7/blob/master/Screen%20Shot%202019-04-05%20at%2010.00.46%20PM.png)

  1. Output: places generated output in the console, or GUI
  2. Chatbot: main thread of execution
  3. POS: checks for and if applicable creates a response based on specific points of speech 
  4. Dictionary: if inout matches an entry in the wordnet library, utilize that 
  5. Response: the main worker/ logic unit for generating output based on input from DrunkBot 
  6. User Input: data inputed as text 

## Github Repository 

## Combined features 

  1. POS tagging 
  2. NLTK library usage 
  3. 
