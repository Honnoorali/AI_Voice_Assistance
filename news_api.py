import requests


key="https://newsapi.org/account"
api_address="http://newsapi.org/y2/top-headlines?country=us&apiKey"+key
json_data = requests.get(api_address).json()

arr=[]


def news():
    for i in range(3):
        arr.append("Number"+str(i+1) + json.data["articles"][i]["title"]+".")
    return arr

arr=news()

print(arr)