import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

def boxprint(*args, **kwargs):
    print("*" * 100)
    print(*args, **kwargs)
    print("*" * 100)

boxprint(response.json())

