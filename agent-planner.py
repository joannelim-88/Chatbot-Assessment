#Part 2: Agentic Planning 
#Customize method (Python based agent planner)

#Flow: Planner --> Tool (Action) --> Response (Result)
#Scenario: Agent to search and ask about ZUS products (product agent for ZUS store)

#Import library
import re

#Menu list 
ZUS_menu = {
    "Classic series": "Americano, Flat white",
    "Latte series": "Rosie latte, Cham latte, Matcha latte",
    "Frappe series": "Mango Spanish frappe, Rosie frappe"
}

#Outlet list 
ZUS_outlet = {
    "outlets": "SS2, Damansara, Taipan USJ, Shah Alam",
    "open_time": "9 a.m.",
    "close_time": "11 p.m."
}

#ZUS menu/outlet tool (Action 1)
def menu_tool():
    print("Bot: This is our store menu: ")
    for series, drink in ZUS_menu.items():
        print(f" {series}: {drink}")

def outlet():
    for category, detail in ZUS_outlet.items():
        print(f" {category}: {detail}")

#ZUS search tool (Action 2)
def search_tool():
    print("Bot: What drink item will you like to search for: ")
    search_drink = input("User: ").lower()
    found_drink = False
    for series, drink in ZUS_menu.items():
        if search_drink in drink.lower():
            print(f"Bot: Yes, this drink {search_drink} is available under our {series}")
            found_drink = True
            break
        elif search_drink in series.lower():
            print(f"Bot: Under {series}, we have {drink}")
            found_drink = True
            break 
    if not found_drink:
        print("Sorry, this drink item is not available.")

#ZUS ask tool (Action 3)
def ask_tool():
    print("Bot: What would you like to ask?\n Enter keywords:\n Outlets | Working hour")
    ask_prompt = input("User: ")
    if ask_prompt.lower() in ["outlet", "outlets"]:
        print(f"Bot: We have {ask_prompt} which are {ZUS_outlet['outlets']}")
    elif ask_prompt.lower() in ["working hour", "time"]:
        print(f"Bot: The store opens at {ZUS_outlet['open_time']} and ends at {ZUS_outlet['close_time']} ")
    elif ask_prompt.lower() in ["open time", "open"]:
        print(f"Bot: The store opens at {ZUS_outlet['open_time']}")
    elif ask_prompt.lower() in ["close time", "close"]:
        print(f"Bot: The store closes at {ZUS_outlet['close_time']}")
    else: 
        print(f"Bot: The {ask_prompt} is not available. Please re-enter based on keywords provided.")


#Exit system (Action 4)
def exit_system():
    print("Bot: Thank you from ZUS, see you again.")

#Intent parsing function 
def parse_intent(user_prompt):
    user_prompt = user_prompt.lower()

    #Menu 
    if re.search(r"\b(menu|show drinks|drinks|have|drink list)\b", user_prompt):
        return "menu"
    #Search 
    if re.search(r"\b(search|find|looking for|look|latte|frappe|classic|have any drink)\b", user_prompt):
        return "search"
    #Ask 
    if re.search(r"\b(ask|outlet|time|working hour|open|close|hours)\b", user_prompt):
        return "ask"
    #Exit
    if re.search(r"\b(exit|end|bye|stop|quit)\b", user_prompt):
        return "exit"

#Main controller loop (Agent)
def agent_planner():
    print("Bot: Hi user, Welcome to ZUS online service.")
    print("Bot: Would you like to start the conversation? (Yes/No)")
    reply = input("User: ")
    if reply.lower() in ["yes", "y"]:
        while(True):
            print("Bot: What would you like to do first?\nEnter keywords:\n Menu | Search | Ask | Exit")
            user_prompt = input("User: ")

            #Intent parsing 
            intent = parse_intent(user_prompt)

            #Call specific actions 
            if intent == "menu":
                menu_tool()
                print("Bot: Continue?(Yes/No)")
                cont = input("User: ")
                if cont.lower() in ["yes", "y"]:
                    True 
                else:
                    print("Bot: Thank you from ZUS, see you again.")
                    break
                
            elif intent == "search":
                search_tool()
                print("Bot: Continue?(Yes/No)")
                cont = input("User: ")
                if cont.lower() in ["yes", "y"]:
                    True 
                else:
                    print("Bot: Thank you from ZUS, see you again.")
                    break
                
            elif intent == "ask":
                ask_tool()
                print("Bot: Continue?(Yes/No)")
                cont = input("User: ")
                if cont.lower() in ["yes", "y"]:
                    True 
                else:
                    print("Bot: Thank you from ZUS, see you again.")
                    break
                
            elif intent == "exit":
                exit_system()
                break
            
            else:
                print("Bot: Invalid request. Please enter keywords as shown above.")
                True
    else:
        print("Bot: Thank you from ZUS, see you again.")


if __name__ == "__main__":
    agent_planner()