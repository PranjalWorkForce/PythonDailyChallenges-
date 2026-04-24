import requests 

s = requests.Session()

def request(url, payload):
  headers = {
    "User-agent" : "Mozilla/5.0",
    "Content-Type" : "Application/x-www-form-urlencoded"
  }

  try:
    respond = s.post(url, headers=headers)
    respond.raise_for_status()
    return respond.text

  except requests.exception.RequestException as e:
    print("error", e)


url = input("Enter the url")
payload = {
  "username" : "puppy",
  "passworr" : "poop"
}
print(request(url, payload))
