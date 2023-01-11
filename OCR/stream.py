import requests

def stream(m):

    data = requests.get(m)
    text = data.text
    if "iframe" in text or "play" in text:
        print(1)
    else:
        print(0)


