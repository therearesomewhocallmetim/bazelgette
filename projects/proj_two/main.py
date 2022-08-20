from libs import greeter


def get_str_to_print():
    return f"{greeter.get_greeting()}, everyone"

if __name__ == "__main__": 
    print(get_str_to_print())