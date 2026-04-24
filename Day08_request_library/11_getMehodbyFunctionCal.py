import requests

def fetch_data(url):
    try:
        response = requests.get(url, timeout=5)

        # Check if request was successful
        response.raise_for_status()

        # Convert response to JSON
        data = response.json()
        return data

    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError:
        print("Connection Error")
    except requests.exceptions.Timeout:
        print("Timeout Error")
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)

# Example usage
url = "https://jsonplaceholder.typicode.com/posts"
result = fetch_data(url)

if result:
    print(result[:2])  # print first 2 items
