from django.shortcuts import render
import xmltodict, json
import requests

def index(request):
    data = requests.get("https://www.gulseli.com/library/service/xml.asp?Type=FACEBOOK")
    obj = xmltodict.parse(data.content)
    json_data = json.dumps(obj)
    jsonFile = open("Templates/data.json", "w")
    jsonFile.write(json_data)
    jsonFile.close()
    return render(request,'data.json')

def data(requset):
    return render(requset,'data.json')