import requests

s = requests.Session()

def make_request(url, cookie, data):
    try:
        response = s.post(url, cookies=cookie, data=data)
        response.raise_for_status()

        print("Status Code:", response.status_code)
        print("Response:", response.text)

    except requests.exceptions.RequestException as e:
        print("Error:", e)


# cookie passed from outside (GOOD practice)
cookie = {
    "name": "init",
    "pass": "Current"
}

data = {
    "full_name": "kites pup",
    "email": "puppyparty@catie.com"
}

url = input("Enter URL: ")

make_request(url, cookie, data)
