import requests

def generate_random_name():
    name = requests.get("https://api.namefake.com/american/male")
    return name.json()['name']

def generate_random_content():
    content = requests.get("https://asdfast.beobit.net/api/")
    return content.json()['text']

def generate_random_email(name):
    return '_'.join(name.lower().split()) + "@gmail.com"