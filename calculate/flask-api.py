#Part 3: Tool Calling 
#Flask API method (Python based calculator tool)

#Import libraries 
from flask import Flask, request, jsonify

app = Flask(__name__)

#With arithmetric intent (Plus, Minus, Divide, Multiply)
#Calculator endpoint
@app.route('/calculate', methods=['POST'])
def calculator():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    arith_operation = data.get('arith_operation')

    if num1 == None or num2 == None or arith_operation == None:
        return jsonify({'error': 'Missing number parameter'}), 400

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({'error': 'Number format invalid'}), 400
    
    #Custom calculator operations (arithmetic intent)
    calc_result = None 
    if arith_operation in ['add', '+']:
        calc_result = num1 + num2
    elif arith_operation in ['subtract', '-']:
        calc_result = num1 - num2
    elif arith_operation in ['multiply', '*', 'x']:
        calc_result = num1 * num2
    elif arith_operation in ['divide', '/']:
        if num2 == 0:
            return jsonify({'error': 'Number unable to divide'}), 400
        calc_result = num1 / num2
    else:      
        return jsonify({'error': 'Invalid arithmetric operation'}), 400
    
    return jsonify({'result': calc_result}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)