import sys
import requests
from libs import greeter, name_getter


if __name__ == "__main__":
    print(f'{greeter.get_greeting()}, {name_getter.get_name()}')
    print(sys.version)
    print(requests.get("https://example.com").content)
