import requests 

url = input("Enter the url")

cookie = {
  "name" : "ramanuj",
  "password" : "login"
}

s = requests.Session()

respond = s.get(url, cookies=cookie)

print(respond.status_code)
print(respond.text)
