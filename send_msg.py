import os, sys, time
from ringcentral import SDK

RECIPIENT    = "+17192912805"
TEXT_MESSAGE = "Text Message as Test Message!"
# SERVER_URL = "https://platform.devtest.ringcentral.com"
# CLIENT_ID = "X7XpZoDS6cHdRkx0Y4OpKn"
# CLIENT_SECRET = "cm87YR88dpZdSQncovNLfa7SXnvIIb2GXbKOpjNGS0xM"
# JWT_TOKEN = "eyJraWQiOiI4NzYyZjU5OGQwNTk0NGRiODZiZjVjYTk3ODA0NzYwOCIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJhdWQiOiJodHRwczovL3BsYXRmb3JtLmRldnRlc3QucmluZ2NlbnRyYWwuY29tL3Jlc3RhcGkvb2F1dGgvdG9rZW4iLCJzdWIiOiI4MjY4OTcwMDUiLCJpc3MiOiJodHRwczovL3BsYXRmb3JtLmRldnRlc3QucmluZ2NlbnRyYWwuY29tIiwiZXhwIjozODQ2ODYxNTg0LCJpYXQiOjE2OTkzNzc5MzcsImp0aSI6IkQ3UGtndTRjUnp1dlREenBDZWZYTncifQ.OaOidJIDCmDdVuMtMBDTUM2LmIREZriOL2Lj--O3ncq856BxhU8eNJB_d_LTjyokvo-UUVjAmjfmQtB7t0somEcMaF5o8UVzgzzQkO-xQFradU00Va4D9etS38p2cMfM-VXMxoh0q9ZiT0-ImCCbTXua_fMiZeE_aci19I4xFgcgE-MagW9cD_QpvghN5TtKs10j_uDPxLGefrgmOZxqSJ35gDaMP8JRG39GKGugIj4-krQ4kjX0D3E6wKuaKfZOF62GVUpJL5VBUll2s7d5iU6uiHXo4jEVtK44Hfvti0WuO70oO_hqEpJOXoAs0TFK-IFKenKRp1gZQOn5Bb-ZBg"

# Read phone number(s) that belongs to the authenticated user and detect if a phone number
# has the SMS capability
def read_extension_phone_number_detect_sms_feature():
    try:
        resp = platform.get("/restapi/v1.0/account/~/extension/~/phone-number")
        jsonObj = resp.json()
        for record in jsonObj.records:
            for feature in record.features:
                if feature == "SmsSender":
                    # If user has multiple phone numbers, check and decide which number
                    # to be used for sending SMS message.
                    return send_sms(record.phoneNumber)
        if len(jsonObj.records) == 0:
            print("This user does not own a phone number!")
        else:
            print("None of this user's phone number(s) has the SMS capability!")
    except Exception as e:
        print(e)

# Send a text message from a user own phone number to a recipient number
def send_sms(fromNumber):
    try:
        bodyParams = {
            'from' : { 'phoneNumber': fromNumber },
            'to'   : [ {'phoneNumber': RECIPIENT } ],
            'text' : TEXT_MESSAGE
        }
        endpoint = "/restapi/v1.0/account/~/extension/~/sms"
        resp = platform.post(endpoint, bodyParams)
        jsonObj = resp.json()
        print("SMS sent. Message id: " + str(jsonObj.id))
        check_message_status(jsonObj.id)
    except Exception as e:
        print(e)

# Check the sending message status until it's out of the queued status
def check_message_status(messageId):
    try:
        endpoint = "/restapi/v1.0/account/~/extension/~/message-store/" + str(messageId)
        resp = platform.get(endpoint)
        jsonObj = resp.json()
        print("Message status: " + jsonObj.messageStatus)
        if jsonObj.messageStatus == "Queued":
            time.sleep(2)
            check_message_status(jsonObj.id)
    except Exception as e:
        print(e)

# Instantiate the SDK and get the platform instance
# rcsdk = SDK(CLIENT_ID, CLIENT_SECRET, SERVER_URL)
rcsdk = SDK(
        os.environ['RINGCENTRAL_CLIENT_ID'],
        os.environ["RINGCENTRAL_CLIENT_SECRET"],
        os.environ["RINGCENTRAL_SERVER_URL"],
    )
platform = rcsdk.platform()

# Authenticate a user using a personal JWT token
def login():
    try:
        # platform.login(jwt= JWT_TOKEN )
        platform.login(jwt=os.environ["RINGCENTRAL_JWT_TOKEN"])

        
        # for _ in range(5):
        read_extension_phone_number_detect_sms_feature()

    except Exception as e:
        sys.exit("Unable to authenticate to platform. Check credentials." + str(e))

login()
