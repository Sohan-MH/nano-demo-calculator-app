# from flask import Flask, request, jsonify 

# app = Flask(__name__)

# # PORT = int(os.environ.get("PORT", 8080))
# # BASE_URL = '/calculator'

# @app.route("/calculator/greeting", methods=['GET'])
# def greeting():
#     return "Hello world!", 200

# @app.route("/calculator/add", methods=['POST'])
# def add():
#     input_data = request.json
#     ans = input_data['first'] + input_data['second']
#     return ans, 200

# @app.route("/calculator/subtract", methods=['POST'])
# def subtract():
#     input_data = request.json
#     ans = input_data['first'] - input_data['second']
#     return ans, 200

# if __name__ == '__main__':
#     app.run(port=8080,host='0.0.0.0')

from flask import Flask, request, jsonify

app = Flask(__name__)

class Numbers:
    def __init__(self, first, second):
        self.first = first
        self.second = second

@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return "Hello world!", 200

@app.route('/calculator/add', methods=['POST'])
def add():
    numbers = request.json
    if 'first' in numbers and 'second' in numbers:
        result = numbers['first'] + numbers['second']
        return jsonify({"result": result}), 200
    else:
        return "Invalid input", 400

@app.route('/calculator/subtract', methods=['POST'])
def subtract():
    numbers = request.json
    if 'first' in numbers and 'second' in numbers:
        result = numbers['first'] - numbers['second']
        return jsonify({"result": result}), 200
    else:
        return "Invalid input", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
