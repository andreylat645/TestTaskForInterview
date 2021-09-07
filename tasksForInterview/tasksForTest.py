import json
import requests

def getResponse():

    url = "/api/web/searchAbonents"
    url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

    r = requests.get(url)
    print("Status code: ", r.status_code)

    #Сохранение ответа API
    response_dict = r.json()

    return response_dict

def saveDict(dict):
    fileName = "COMPANY.json"
    with open(fileName, mode = 'w') as f_obj:
        json.dump(dict, f_obj)
    f_obj.close()



dict = getResponse()
saveDict(dict)