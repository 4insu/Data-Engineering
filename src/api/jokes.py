import requests

def get_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        joke = data["data"]["content"]
        return joke
    else:
        raise Exception("Failed to fetch the joke!")