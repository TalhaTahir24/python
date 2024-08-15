import datetime

def get_greeting():
    current_time = datetime.datetime.now().time()
    hour = current_time.hour

    if hour < 12:
        return "Good morning!"
    elif hour < 17:
        return "Good afternoon!"
    else:
        return "Good night!"

print(get_greeting())
