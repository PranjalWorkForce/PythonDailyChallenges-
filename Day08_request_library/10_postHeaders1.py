import requests

# Create a session (keeps cookies and login state across requests)
s = requests.Session()

# Take target URL from user
url = input("Enter the URL: ")

# Headers tell the server how to interpret your request
# User-Agent → makes request look like it's coming from a real browser
# Content-Type → tells server how the data is formatted
headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded"  
    # Used for traditional HTML form data
    # Format sent: username=ramanuj&password=login
    # Most normal login pages expect this
}

# Data to send in POST request (login credentials)
data = {
    "username": "ramanuj",
    "password": "login"
}

# Send POST request with form-encoded data
# data= → sends data as application/x-www-form-urlencoded
response = s.post(url, headers=headers, data=data)

# Print status code (200 = success, 403 = forbidden, etc.)
print("Status:", response.status_code)

# Print server response (HTML / JSON / message)
print("Response:", response.text)


# ---------------- IMPORTANT NOTES ----------------
# 1. JSON vs Form:
#    - application/x-www-form-urlencoded → used by HTML forms
#    - application/json → used by APIs (modern apps, mobile apps)
#
# 2. Login is NOT fixed to one format:
#    - Some sites use form data
#    - Some APIs use JSON
#    - Server decides what it accepts
#
# 3. If using JSON:
#    response = s.post(url, json=data)
#    → automatically sets Content-Type: application/json
#
# 4. If you mismatch:
#    - Sending JSON when server expects form → FAIL
#    - Sending form when server expects JSON → FAIL
#
# 5. Real-world rule (VERY IMPORTANT):
#    - Never guess request format
#    - Open browser → Inspect → Network tab
#    - Check actual request:
#         • Headers
#         • Payload format (JSON or form)
#    - Then replicate exactly in Python
#
# 6. Session():
#    - Keeps cookies automatically
#    - Helps maintain login state across requests
