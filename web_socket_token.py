import json
from ringcentral import SDK

SANDBOX_JWT="eyJraWQiOiI4NzYyZjU5OGQwNTk0NGRiODZiZjVjYTk3ODA0NzYwOCIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJhdWQiOiJodHRwczovL3BsYXRmb3JtLmRldnRlc3QucmluZ2NlbnRyYWwuY29tL3Jlc3RhcGkvb2F1dGgvdG9rZW4iLCJzdWIiOiI4MjY4OTcwMDUiLCJpc3MiOiJodHRwczovL3BsYXRmb3JtLmRldnRlc3QucmluZ2NlbnRyYWwuY29tIiwiZXhwIjozODQ2ODYxNTg0LCJpYXQiOjE2OTkzNzc5MzcsImp0aSI6IkQ3UGtndTRjUnp1dlREenBDZWZYTncifQ.OaOidJIDCmDdVuMtMBDTUM2LmIREZriOL2Lj--O3ncq856BxhU8eNJB_d_LTjyokvo-UUVjAmjfmQtB7t0somEcMaF5o8UVzgzzQkO-xQFradU00Va4D9etS38p2cMfM-VXMxoh0q9ZiT0-ImCCbTXua_fMiZeE_aci19I4xFgcgE-MagW9cD_QpvghN5TtKs10j_uDPxLGefrgmOZxqSJ35gDaMP8JRG39GKGugIj4-krQ4kjX0D3E6wKuaKfZOF62GVUpJL5VBUll2s7d5iU6uiHXo4jEVtK44Hfvti0WuO70oO_hqEpJOXoAs0TFK-IFKenKRp1gZQOn5Bb-ZBg"
SANDBOX_APP_CLIENTID="X7XpZoDS6cHdRkx0Y4OpKn"
SANDBOX_APP_CLIENTSECRET="cm87YR88dpZdSQncovNLfa7SXnvIIb2GXbKOpjNGS0xM"


API_SERVER_URL="https://platform.devtest.ringcentral.com"
# API_SERVER_URL="https://platform.ringcentral.com"



def create_websocket_token():
    try:
        
        # endpoint = "/restapi/v1.0/account/~/extension/~/message-store"
        endpoint = "/restapi/oauth/wstoken"
        
        headers = {
            "Authorization": f"Bearer {SANDBOX_JWT}"
        }

        resp = platform.post(endpoint, headers=headers)
        jsonObj = resp.json_dict()
        print("jsonObj: ", jsonObj)

    except Exception as e:
        print (str(e))


# Authenticate a user using a personal JWT token
def login():
    try:
      platform.login( jwt= SANDBOX_JWT )
      create_websocket_token()
    except Exception as e:
      print ("Unable to authenticate to platform. Check credentials." + str(e))

# Instantiate the SDK and get the platform instance
rcsdk = SDK(SANDBOX_APP_CLIENTID, SANDBOX_APP_CLIENTSECRET, API_SERVER_URL)
platform = rcsdk.platform()

login()

