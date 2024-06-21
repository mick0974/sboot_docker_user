import requests
import json

login_url = "http://localhost:8080/api/auth/login"

body = {
    "username": "admin",
    "password": "password"
}

response = requests.post(login_url, json=body)
response_data = response.json()
#print(response_data)

if response.status_code == 200:
    response_data = response.json()
    token = response_data.get("token")

    if token is not None:
        rtg_info = {
            "name": "Authorization",
            "value": "Bearer " + token,
            "in": "header",
            "duration": 600
        }
        print(json.dumps(rtg_info))
else:
    body = {
        "username": "admin2",
        "password": "password"
    }

    response = requests.post(login_url, json=body)
    response_data = response.json()
    #print(response_data)

    if response.status_code == 200:
        response_data = response.json()
        token = response_data.get("token")

        if token is not None:
            rtg_info = {
                "name": "Authorization",
                "value": "Bearer " + token,
                "in": "header",
                "duration": 600
            }
            print(json.dumps(rtg_info))
    else:
        body = {
            "username": "admin3",
            "password": "password"
        }

        response = requests.post(login_url, json=body)
        response_data = response.json()
        #print(response_data)

        if response.status_code == 200:
            response_data = response.json()
            token = response_data.get("token")

            if token is not None:
                rtg_info = {
                    "name": "Authorization",
                    "value": "Bearer " + token,
                    "in": "header",
                    "duration": 600
                }
                print(json.dumps(rtg_info))