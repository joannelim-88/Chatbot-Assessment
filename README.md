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


# Architecture overview 
This project follows a simple architecture for backend and data flows. 

Components:
Python language as main backend language for API handling and chatbot logic workflow. 
Database using SQL queries inside Python functions
API used: GEMINI / OPENAI 
RAG integration: FAISS for information retrieval KB, SQlite3 for Text2SQL in Python

Data flow:
1. Interacts with chatbot via terminal
2. API calls from one terminal and applications run separately
3. Both API and system responses are returned according to the given actions by user

# Key trade-offs 
1. Database (SQL query in Python)
SQL queries easy to handle in database, however it is run inside Python by connecting directly using queries and specific SQL functions.

2. Host on Vercel
Able to easily deploy. However this application does not have proper interface, therefore it is best to use it locally to run that has terminals. 


# Important Note 
To run the rag integration, you need to get your own API key from OPENAI or GEMINI to continue and save the API KEY inside a .env file before continue running Part 4.

Visit OPENAI: https://platform.openai.com/api-keys

Visit GEMINI: https://aistudio.google.com/apikey
