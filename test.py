import requests

URL = "http://127.0.0.1:8000"

# Test API GET /
print("Test GET / \n")

res_home = requests.get(f"{URL}/")
print(f"Status code: {res_home.status_code}")
print(f"JSON result: {res_home.json()}")
assert res_home.status_code == 200, "Error: GET / doesn't return 200."

print("\n", "-" * 80, "\n")


# Test API GET /health
print("Test GET /health \n")

res_health = requests.get(f"{URL}/health")
print(f"Status code: {res_health.status_code}")
print(f"JSON result: {res_health.json()}")
assert res_health.status_code == 200, "Error: GET /health doesn't return 200."

print("\n", "-" * 80, "\n")


# Test API POST /predict, positive message
print("Test POST /predict positive message \n")

data_positive = {
    "text": "When you are seriously trying to accomplish something, you'll always be alone. You can't do it if you are not alone."
}

res_predict_positive = requests.post(f"{URL}/predict", json = data_positive)
print(f"Status code: {res_predict_positive.status_code}")
print(f"JSON result: {res_predict_positive.json()}")
assert res_predict_positive.status_code == 200, "Error: POST /predict positive normal message doesn't return 200."

print("\n", "-" * 80, "\n")


# Test API POST /predict, negative message
print("Test POST /predict negative message \n")

data_negative = {
    "text": "You are terrible."
}

res_predict_negative = requests.post(f"{URL}/predict", json = data_negative)
print(f"Status code: {res_predict_negative.status_code}")
print(f"JSON result: {res_predict_negative.json()}")
assert res_predict_negative.status_code == 200, "Error: POST /predict negative message doesn't return 200."

print("\n", "-" * 80, "\n")


# Test API POST /predict, empty message
print("Test POST /predict empty message \n")

data_empty = {
    "text": ""
}

res_predict_empty = requests.post(f"{URL}/predict", json = data_empty)
print(f"Status code: {res_predict_empty.status_code}")
print(f"JSON result: {res_predict_empty.json()}")
assert res_predict_empty.status_code == 400, "Error: The server could not catch empty/whitespaces only message."


print("\n", "-" * 80, "\n")


# Test API POST /predict, whitespaces only message
print("Test POST /predict whitespaces only message \n")

data_ws = {
    "text": "    "
}

res_predict_ws = requests.post(f"{URL}/predict", json = data_ws)
print(f"Status code: {res_predict_ws.status_code}")
print(f"JSON result: {res_predict_ws.json()}")
assert res_predict_ws.status_code == 400, "Error: The server could not catch empty/whitespaces only message."