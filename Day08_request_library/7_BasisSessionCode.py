import requests 

session = requests.Session()
url = input("Enter the url")

print(session.get(url).status_code)
