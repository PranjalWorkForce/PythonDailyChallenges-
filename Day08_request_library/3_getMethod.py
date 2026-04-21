import requests

params = {
    "q": "python",
    "page": 1
}

res = requests.get("https://www.google.com/search", params=params)
print(res.url)

# https://www.google.com/search?q=python&page=1 l

# Get method is a method the data is transfered by the url 
