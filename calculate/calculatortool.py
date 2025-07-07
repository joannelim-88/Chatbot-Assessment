
#Part 3: Tool Calling 
#Run main app (Calls Calculator API)
#Import libraries 
import requests
import json

#Calculator Bot 
def mainapp():
    print("Bot: Welcome to Calculator Bot tool.")
    print("Bot: Please input your numbers to start.")
    #Error handling (Input must be number)
    try: 
        number1 = float(input("User: Enter Num1 - "))
        number2 = float(input("User: Enter Num2 - "))
    except ValueError:
        print("Bot: Retry, Please enter numbers only")
        return 
    
    print("Bot: Choose arithmetric option:\n add(+) | subtract(-) | multiply(*/x) | divide(/)")
    arithmetric = input("User: ").lower()

    #Request for API 
    calc = {
        "num1": number1, 
        "num2": number2,
        "arith_operation": arithmetric
    }

    try:
        response = requests.post("http://localhost:5000/calculate", json=calc)
        result = response.json()

        if response.status_code == 200 and 'result' in result:
            print(f"Bot: The calculated result is {result['result']}")
        elif 'error' in result:
            print(f"Bot: Error: {result['error']}")
        else:
            print("Bot: Error, please retry again")
            

    except requests.exceptions.ConnectionError:
        print("Bot: System unable to run. Please retry")

if __name__ == "__main__":
    mainapp()