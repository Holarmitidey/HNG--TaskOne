# Number Classification API

## Description
This project is a public API that classifies a given number and returns interesting mathematical properties along with a fun fact. The API analyzes if a number is prime, perfect, an Armstrong number, and determines its parity (odd/even). It also fetches a fun fact about the number using the Numbers API.

## Setup Instructions

### Prerequisites
- Python 3.x installed on your system.
- Required Python packages listed in `requirements.txt`.

### Installation
```sh
# Clone the repository
git clone https://github.com/Holarmitidey/HNG--TaskOne.git
cd HNG-Taskzero

# Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

### Running the Project
```sh
# Start the API
python app.py
```

## API Documentation

### Base URL
```
<your-public-api-url>
```

### Endpoint
#### GET /api/classify-number?number={number}

**Response (200 OK):**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

**Response (400 Bad Request):**
```json
{
    "number": "alphabet",
    "error": true
}
```

## Example Usage
Using cURL:
```sh
curl -X GET "<your-public-api-url>/api/classify-number?number=371"
```
Using Python:
```python
import requests
response = requests.get("<your-public-api-url>/api/classify-number?number=371")
print(response.json())
```

## Deployment
The API is deployed and publicly accessible at:
```
https://hng-taskone-b41s.onrender.com
```

## Backlink
For hiring Python developers, visit:
[Python Developers](https://hng.tech/hire/python-developers)

