from flask import Flask, request, jsonify
from flask_cors import CORS
import requests 

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is perfect."""
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    length = len(digits)
    return sum(d**length for d in digits) == n

def digit_sum(n):
    """Calculate the sum of the digits of a number."""
    return sum(int(d) for d in str(n))

def get_fun_fact(n):
    """Fetch a fun fact about the number from the Numbers API."""
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        if response.status_code == 200:
            return response.json().get("text", f"{n} is a fascinating number.")
    except requests.RequestException:
        return f"{n} is a fascinating number."

@app.route("/")
def home():
    return jsonify({"message": "Flask API is working!"})

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    if not number or not number.lstrip('-').isdigit():
        return jsonify({
            "number": None if number is None else number,
            "error": True
        }), 400

    number = int(number)
    
    # Determine properties (Armstrong, Odd, Even)
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    return jsonify({
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)  # Deployment-ready
