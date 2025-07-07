#Part 1: Sequential Conversation
#Customize method (Python console-flow based sequential conversation)

#Bot memory state
memory = {
    "outlet_PetalingJaya": "SS2, Petaling Jaya",
    "open_time": "9 a.m.",
    "close_time": "11 p.m."
}

#Chatbot interaction (sequential-based)
def memory_chatbot():
    print("Bot: Hi user, Would you like to start the conversation? (Yes/No)") #happy/interrupted path 1
    greeting = input("User: ")

    if greeting.lower() in ["no", "n"]:
        print("Bot: Alright, have a nice day ahead.")

    elif greeting.lower() in ["yes", "y"]:
        while(True):
            print("Bot: Sure, you may ask your question now.") #happy path 2
            user_question = input("User: ").lower()

            if "other outlet" in user_question and "petaling jaya" in user_question:
                print("Bot: Sorry we currently have only one outlet in SS2, would you like to continue? (Yes/No)") #interrupted path 2
                reply = input("User: ")
                if reply.lower() in ["yes", "y"]:
                    print(f"Bot: The outlet in {memory['outlet_PetalingJaya']} outlet opens at {memory['open_time']} and closes at {memory['close_time']}.") #happy path 4
                    print("Bot: Would you like to end this session?(Yes/No)") #happy path 5
                    end = input("User: ")
                    if end.lower() in ["yes", "y"]:
                        print("Bot: Bye, thank you for chatting with me.")
                        break
                    else:
                        True
                else:
                    print("Bot: Bye, thank you for chatting with me.")
                    break

            elif "outlet" in user_question and "petaling jaya" in user_question:
                print("Bot: Yes! Which outlet are you reffering to?") #happy path 3
                outlet = input("User: ").lower()

                if "ss2" in outlet.lower():
                    print(f"Bot: Ah yes, the {memory['outlet_PetalingJaya']} outlet opens at {memory['open_time']} and closes at {memory['close_time']}.") #happy path 4
                    
                    print("Bot: Would you like to end this session?(Yes/No)") #happy path 5
                    end = input("User: ")
                    if end.lower() in ["yes", "y"]:
                        print("Bot: Bye, thank you for chatting with me.")
                        break 
                    else:
                        True
                else:
                    print(f"Bot: Sorry, No outlet" in outlet) #interrupted path 3
            else:
                print("Bot: Sorry, Outlet not available yet") #interrupted path 3
                print("Bot: Would you like to end this session?(Yes/No)") #happy path 5
                end = input("User: ")
                if end.lower() in ["yes", "y"]:
                    print("Bot: Bye, thank you for chatting with me.")
                    break
                else:
                    True
    else:
        print("Bot: Sorry invalid, please retry again.") #interrupted path 4
        

if __name__ == "__main__":
    memory_chatbot()
