import requests

# Target URL
url = "https://httpbin.org/get"

# Send GET request
response = requests.get(url)

# Print response details
print("Status Code:", response.status_code)
print("Headers:", response.headers)
print("Response Body:\n", response.text)

// Status code 200 → Request was successful (server understood and processed it)

// Headers → Metadata sent by the server to the client (not the main content)
// Examples: content-type, cookies, server info

// Response text → The actual content returned by the server
// (HTML, JSON, etc.)
