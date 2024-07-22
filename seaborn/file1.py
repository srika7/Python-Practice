import requests

def fetch_webpage_example():
    response = requests.get('https://www.example.com')
    print(response.status_code)
    print(response.text[:100])  # Print the first 100 characters of the response

if __name__ == "__main__":
    fetch_webpage_example()
