import sys
import requests
from libs import main


if __name__ == "__main__":
    print(main.get_greeting())
    print(sys.version)
    print(requests.get("https://example.com").content)
