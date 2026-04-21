import requests 

data = {
  username = "pranjal",
  password = "anythings"
}

res = requests.post("https://example.com/login", data=data)
print(res.status_code)


# post method is a method where the data is send through the form
