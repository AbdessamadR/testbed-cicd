
import requests

def check_api():
    response = requests.get("https://httpbin.org/get", timeout=10)
    print(f"API Status: {response.status_code}")

if __name__ == "__main__":
    print("Starting application...")
    check_api()
