import requests

s = requests.Session()

url = input("Enter the URL: ")

headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json"
}

data = {
    "username": "ramanuj",
    "password": "login"
}

response = s.post(url, headers=headers, json=data)

print("Status:", response.status_code)
print("Response:", response.text)
