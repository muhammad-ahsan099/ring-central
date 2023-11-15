import json
from ringcentral import SDK

# SANDBOX_JWT="eyJraWQiOiI4NzYyZjU5OGQwNTk0NGRiODZiZjVjYTk3ODA0NzYwOCIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJhdWQiOiJodHRwczovL3BsYXRmb3JtLmRldnRlc3QucmluZ2NlbnRyYWwuY29tL3Jlc3RhcGkvb2F1dGgvdG9rZW4iLCJzdWIiOiI4MjY4OTcwMDUiLCJpc3MiOiJodHRwczovL3BsYXRmb3JtLmRldnRlc3QucmluZ2NlbnRyYWwuY29tIiwiZXhwIjozODQ2ODYxNTg0LCJpYXQiOjE2OTkzNzc5MzcsImp0aSI6IkQ3UGtndTRjUnp1dlREenBDZWZYTncifQ.OaOidJIDCmDdVuMtMBDTUM2LmIREZriOL2Lj--O3ncq856BxhU8eNJB_d_LTjyokvo-UUVjAmjfmQtB7t0somEcMaF5o8UVzgzzQkO-xQFradU00Va4D9etS38p2cMfM-VXMxoh0q9ZiT0-ImCCbTXua_fMiZeE_aci19I4xFgcgE-MagW9cD_QpvghN5TtKs10j_uDPxLGefrgmOZxqSJ35gDaMP8JRG39GKGugIj4-krQ4kjX0D3E6wKuaKfZOF62GVUpJL5VBUll2s7d5iU6uiHXo4jEVtK44Hfvti0WuO70oO_hqEpJOXoAs0TFK-IFKenKRp1gZQOn5Bb-ZBg"
# SANDBOX_APP_CLIENTID="X7XpZoDS6cHdRkx0Y4OpKn"
# SANDBOX_APP_CLIENTSECRET="cm87YR88dpZdSQncovNLfa7SXnvIIb2GXbKOpjNGS0xM"
# SANDBOX_JWT="eyJraWQiOiI4NzYyZjU5OGQwNTk0NGRiODZiZjVjYTk3ODA0NzYwOCIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJhdWQiOiJodHRwczovL3BsYXRmb3JtLnJpbmdjZW50cmFsLmNvbS9yZXN0YXBpL29hdXRoL3Rva2VuIiwic3ViIjoiMjk3NDk0ODAzNiIsImlzcyI6Imh0dHBzOi8vcGxhdGZvcm0ucmluZ2NlbnRyYWwuY29tIiwiZXhwIjozODQzNTE2NDMyLCJpYXQiOjE2OTYwMzI3ODUsImp0aSI6ImJ0bDl1TncwUUVLUDAzVlF4N0tmREEifQ.QWAzaeEksPlRrVq_Jp7EHSKn5Ga80oVj0k765OiqGAzc7VKNQlOcZcSSqX52GmXnQGzCswp2n1aWx-va4L7tAYnOHEJ35pH5JD5swYupcbrBwjCiemd7PvcCWtEPpGqR424ywr4SWGzDz8xw76sJbg303h5N537iN-Ysyke5A6R9IGFaMaRtDMgRtR_h6OKQZuP-GJd5bdwP_1d_QLQPKBBeVHMUM8k9_pEw59mIXYtH7A72PE3YgIYVmW0bViq3FHXx-eUrachl_-wTYQ6pCZS7dD81upNkYYqlydWbIjVFSaHRu6Q-dsE6g1hn66LBEj_J-mvVcdUVTBxU4prpYw"

# SANDBOX_JWT="eyJraWQiOiI4NzYyZjU5OGQwNTk0NGRiODZiZjVjYTk3ODA0NzYwOCIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJhdWQiOiJodHRwczovL3BsYXRmb3JtLmRldnRlc3QucmluZ2NlbnRyYWwuY29tL3Jlc3RhcGkvb2F1dGgvdG9rZW4iLCJzdWIiOiI4MjY4OTcwMDUiLCJpc3MiOiJodHRwczovL3BsYXRmb3JtLmRldnRlc3QucmluZ2NlbnRyYWwuY29tIiwiZXhwIjozODQ3MDQxNDYzLCJpYXQiOjE2OTk1NTc4MTYsImp0aSI6Ikc5eFZOYi1TUmJleUZ3MHU0eWNjaXcifQ.LRYJY1EY_UXbrThCkXUf5OyO3aTSTXNk2ZlxcU_0Gj8r2_3OI1QrabfVKzSz0mfFGhWbwqAVwWfD_BuD71VRSqRep87P2VPREKNG8-GHs084pVhmkoy030nVqKTxQUBQVa9DAzJrlJ0BNql7cNRBWhPJQkp_Cm3RgVvDGjDQoF-mAzHgiiIOyJguifCv2NWhbKRz7ADJhEeBtUrrAooWC3uo1Chi4QSipQ-zJWqfsIN_0x19E7vk3qUXRjS3TaocGggoP05cXDvBVpPxKR6oLRWXBSHbHTnc19VuU75ygVq9aji6r0hNLYxN0HZuZBdkTzWF9w0yQVSeIAKuCc1QNg"
# SANDBOX_APP_CLIENTID="dR6tCzmjfcwfcs2shP8HHT"
# SANDBOX_APP_CLIENTSECRET="VtppGt4XmWPelMilZsA2eZABlPoOkG13VedlwXXCqL0K"

# SANDBOX_JWT="eyJraWQiOiI4NzYyZjU5OGQwNTk0NGRisODZ   iZjVjYTk3ODA0NzYwOCIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJhdWQiOiJodHRwczovL3BsYXRmb3JtLnJpbmdjZW50cmFsLmNvbS9yZXN0YXBpL29hdXRoL3Rva2VuIiwic3ViIjoiMjk3MDYyNTAzNiIsImlzcyI6Imh0dHBzOi8vcGxhdGZvcm0ucmluZ2NlbnRyYWwuY29tIiwiZXhwIjozODQzMTU3MzkyLCJpYXQiOjE2OTU2NzM3NDUsImp0aSI6Im0zR1BzampiVEl5Ny1VY0hEcTV3YlEifQ.QbVIb6-Ljkr8tl5iEkXUewWGSifrai5P_Vr6wDOH95yC3BNF1yhNVPyyERDLu_70QGs6-ke7-P8d5_DwAWAF1AxPIJZ-xzV5zLBQwFOG7qBbB8ivdw3uf9pEB26NUAqFMlX_8CxcIV7ICaB5SwDlBkJNCcOyW3KhUiKt-vgQY_MWJlelw8ieY9TPHkBXCmaqRjBDu12Z_ac9_FQhPLkkxwMJIAuAuDwn-bhAKqy9mlGOKy5Ipxvwkly0kz1tkN4-bUbSjKKdtImvvx0Oz386JlCwJD2peQYMhH8xijf9DtDLZjgmE-_49ldFBGaaQhGkYD377-bK2IXbxb4Qrwm_qQ"
SANDBOX_JWT="eyJraWQiOiI4NzYyZjU5OGQwNTk0NGRiODZiZjVjYTk3ODA0NzYwOCIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJhdWQiOiJodHRwczovL3BsYXRmb3JtLnJpbmdjZW50cmFsLmNvbS9yZXN0YXBpL29hdXRoL3Rva2VuIiwic3ViIjoiMjk3MDYyNTAzNiIsImlzcyI6Imh0dHBzOi8vcGxhdGZvcm0ucmluZ2NlbnRyYWwuY29tIiwiZXhwIjozODQ3MTIwOTE0LCJpYXQiOjE2OTk2MzcyNjcsImp0aSI6Ijk0bDMyRmk2UlZ1b1pDNTFqODlId3cifQ.HHLnC604NqHws_Z2MKrkaga1qenteG4YtXzUo2yWMmZdwQJyPtEL4yrMjbdD6ado-zSevLvaj1pJTq-X4MyjllxJYJ6CzriJy_P42fEsQIh8UVnKmKNpZiHOwJc9VbxxnKLt-wRJkd5-ZV-me37YPOxPU4oA8QuPEpUJZREadV39rwqyOCOpILaiI9gxytPrDhnkWX03SSyDmVc_asmUtMk36IVEqQIwGHDGpsh2CglUijfDe3fiPA49h-iSmtMNCxF_H7Bjy_PKFmaoLT-UZOek-UjAX-cwbH_grpHIBj5czP1VNkiKqb5lJBO9T1_-YnD55_H-8cn96ipBWfz__g"
SANDBOX_APP_CLIENTID="dIbZwaDj28geY8HgSjyg19"
SANDBOX_APP_CLIENTSECRET="0OHlMWSlxdZfmVt2oyj1LwXPnsnWDrTUNdSs6vnyTxd2"


# API_SERVER_URL="https://platform.devtest.ringcentral.com"
API_SERVER_URL="https://platform.ringcentral.com"

# Read the current authenticated user's message store.
def read_extension_message_store():
    try:
        queryParams = {
            'dateFrom': "2023-09-01T00:00:00.000Z",
            'dateTo': "2023-11-14T23:59:59.999Z",
            'messageType': ["SMS"],
            'perPage': 1000
          }
        endpoint = "/restapi/v1.0/account/~/extension/~/message-store"
        resp = platform.get(endpoint, queryParams)
        jsonObj = resp.json_dict()
        print("jsonObj: ", jsonObj)
        for index, record in enumerate(jsonObj['records']):
          # Print the index and total length of the records list
          print(f"Record {index+1} of {len(jsonObj['records'])}:")
          # Print the individual record with indentation and sorted keys
          print(json.dumps(record, indent=2, sort_keys=True))

    except Exception as e:
        print (str(e))


# Authenticate a user using a personal JWT token
def login():
    try:
      platform.login( jwt= SANDBOX_JWT )
      read_extension_message_store()
    except Exception as e:
      print ("Unable to authenticate to platform. Check credentials." + str(e))

# Instantiate the SDK and get the platform instance
rcsdk = SDK(SANDBOX_APP_CLIENTID, SANDBOX_APP_CLIENTSECRET, API_SERVER_URL)
platform = rcsdk.platform()

login()




# import os
# import sys

# from ringcentral import SDK

# SERVER_URL = "https://platform.devtest.ringcentral.com"
# CLIENT_ID = "X7XpZoDS6cHdRkx0Y4OpKn"
# CLIENT_SECRET = "cm87YR88dpZdSQncovNLfa7SXnvIIb2GXbKOpjNGS0xM"
# JWT_TOKEN = "eyJraWQiOiI4NzYyZjU5OGQwNTk0NGRiODZiZjVjYTk3ODA0NzYwOCIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJhdWQiOiJodHRwczovL3BsYXRmb3JtLmRldnRlc3QucmluZ2NlbnRyYWwuY29tL3Jlc3RhcGkvb2F1dGgvdG9rZW4iLCJzdWIiOiI4MjY4OTcwMDUiLCJpc3MiOiJodHRwczovL3BsYXRmb3JtLmRldnRlc3QucmluZ2NlbnRyYWwuY29tIiwiZXhwIjozODQ2ODYxNTg0LCJpYXQiOjE2OTkzNzc5MzcsImp0aSI6IkQ3UGtndTRjUnp1dlREenBDZWZYTncifQ.OaOidJIDCmDdVuMtMBDTUM2LmIREZriOL2Lj--O3ncq856BxhU8eNJB_d_LTjyokvo-UUVjAmjfmQtB7t0somEcMaF5o8UVzgzzQkO-xQFradU00Va4D9etS38p2cMfM-VXMxoh0q9ZiT0-ImCCbTXua_fMiZeE_aci19I4xFgcgE-MagW9cD_QpvghN5TtKs10j_uDPxLGefrgmOZxqSJ35gDaMP8JRG39GKGugIj4-krQ4kjX0D3E6wKuaKfZOF62GVUpJL5VBUll2s7d5iU6uiHXo4jEVtK44Hfvti0WuO70oO_hqEpJOXoAs0TFK-IFKenKRp1gZQOn5Bb-ZBg"

# rcsdk = SDK(CLIENT_ID, CLIENT_SECRET, SERVER_URL)
# platform = rcsdk.platform()
# try:
#     platform.login(jwt=JWT_TOKEN)
# except Exception as e:
#     sys.exit("Unable to authenticate to platform: " + str(e))

# resp = platform.get('/restapi/v1.0/account/~/extension')
# jsonObj = resp.json()
# for record in jsonObj.records:
#     print(f'| Extension: {record.extensionNumber}', end="")
#     print(f'| Name: {record.name}', end="")
#     print(f'| Type: {record.type}')
