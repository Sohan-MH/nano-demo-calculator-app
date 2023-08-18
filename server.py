from flask import Flask, request, jsonify 

app = Flask(__name__)

# PORT = int(os.environ.get("PORT", 8080))
# BASE_URL = '/calculator'

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello world!", 200

@app.route("/calculator/add", methods=['POST'])
def add():
    input_data = request.json
    ans = input_data['first'] + input_data['second']
    return ans, 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    input_data = request.json
    ans = input_data['first'] - input_data['second']
    return ans, 200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
