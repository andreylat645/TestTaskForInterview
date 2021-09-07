import json
import requests

def updateInfo():

    fileName = "COMPANY.json"
    url = "api/web/searchAbonents"

    infoCompany = {
   "companyContact": {
        "displayName": "Company name",
        "address": {
            "streetAddress": "Company address"
        },
        "phoneNumbers": [
            "company phone"
        ]
    },
    "supportContact": {
        "phoneNumber": "support phone",
        "displayName": "Support",
        "email": "support@email.com"
    }
}

    requests.post(url, data=json.dumps(infoCompany))

    infoList = [infoCompany]

    with open(fileName, mode='w') as fObj:
        json.dump(infoList, fObj)
        fObj.close()

"ИЗМЕНЕНИЯ"
updateInfo()