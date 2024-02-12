import json
import requests

def readFromAPI(url, params, headers, filename):
    
    response = requests.get(url, params=params, headers=headers).json()
    

    with open(filename, 'a') as file:  
        json_str = json.dumps(response, indent=4)  
        file.write(json_str + '\n')

# API parameters
api_key = "605ea1ba1998c6b3f09eb540e489b013"  
url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "krabi,th",
    "appid": api_key
}
filename = "data.jsonl"  
headers = {}


readFromAPI(url, params, headers, filename)
