import sys
import requests

if __name__ == "__main__":
    print("hello")
    print(sys.version)
    print(requests.get("https://example.com").content)
