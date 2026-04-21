import requests

json_data = {
    "name": "Pranjal",
    "skill": "cybersecurity"
}

res = requests.post("https://api.example.com/users", json=json_data)
print(res.json())


#JSON is an small data's which goes to the server by POST method and communicate with APIs. 
