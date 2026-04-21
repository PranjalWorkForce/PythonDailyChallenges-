import requests

res = requests.get("https://api.github.com")

print(res.status_code)
print(res.headers)
print(res.text[:200])


#response.status_code   # 200, 404, 500
#response.text          # HTML content
#response.json()        # JSON response
#response.headers       # Server response headers
#response.cookies       # Cookies from server
