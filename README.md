# Introduction - Chatbot-Assessment
This chatbot application is an console-based Python application that is assessible to run on any Python IDE and connect to website port for running API at website. It consists of few parts which includes:

Part 1: chatbot_memory.py 
- Run chatbot with memory 

Part 2: agent_planner.py 
- Run chatbot agent for different intents and actions

Part 3: flask_api.py & calculatortool.py 
- Run FLASK API with calculator tool for running different arithmetric operations 

Part 4/5: fast_api.py, rag_outlet.py & rag_drinkware.py 
- Run FAST API with specific endpoints and OPENAI / GEMINI API KEYS

Part 5: chatbot_unhappy.py 
- Run testing file for testing unhappy flows using pytest


# Setup 
- Simply download this file to run the python chatbot application to test the outcome.
  
- Ensure to download all relevant libraries to successfully run the application parts.


# Run Instructions
- Run each parts separately in a console at Python terminal.
  
- Simply run Part 1 and Part 2 at terminal by entering user query to view outcome.
  
- Connect with FLASK API first, then run Part 3 at terminal by entering user query accordingly to view outcome.
  
- Connect with FAST API first, then run Part 4 files accordingly by typing user query and enter the link URL to website for testing API calls and return expected outcome.
  
- Connect with FAST API first, then run Part 5 separately with typing pytest and modifying the testing prompt before testing runs.


# Important Note 
To run the rag integration, you need to get your own API key from OPENAI or GEMINI to continue and save the API KEY inside a .env file before continue running Part 4.

Visit OPENAI: https://platform.openai.com/api-keys

Visit GEMINI: https://aistudio.google.com/apikey 

