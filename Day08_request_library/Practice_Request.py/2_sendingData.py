import requests

url = "https://httpbin.org/post"

data = {
    "user": "puppy",
    "pass": "123"
}

response = requests.post(url, json=data)
print(response.json())
