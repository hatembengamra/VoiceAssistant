import requests

API = "e8b8ca39c6914fbd8a8bf0543ab89f63"
api_address = "http://newsapi.org/v2/top-headlines?country=us&apikey="+ API
json_data = requests.get(api_address).json()


ar = []

def news():
    for i in range(3):
        ar.append("Number "+ str(i+1) + ", " + json_data["articles"][i]["title"]+".")
    return ar

arr = news()


