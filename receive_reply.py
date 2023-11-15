from ringcentral import SDK
from dotenv import load_dotenv
import asyncio
import os
from ringcentral.websocket.events import WebSocketEvents
import websockets


async def ping_pong_handler(websocket, path):
    try:
        while True:
            await asyncio.sleep(30)  # Adjust the interval as needed
            print("Send Ping Message----")
            await websocket.ping()
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed: {e}")

def on_notification(message):
    print("on_notification Message", message)

def on_sub_created(sub):
    print("on_sub_created: ",sub.get_subscription_info())

def on_ws_created(web_socket_client):
    print("on_ws_created", web_socket_client.get_connection_info())

async def subscribe():
    load_dotenv(override=True)
    sdk = SDK(
        os.environ['RINGCENTRAL_CLIENT_ID'],
        os.environ["RINGCENTRAL_CLIENT_SECRET"],
        os.environ["RINGCENTRAL_SERVER_URL"],
    )
    platform = sdk.platform()
    platform.login(jwt=os.environ["RINGCENTRAL_JWT_TOKEN"])

    try:
        print("Try to Create Connection with ClientId: ", os.environ['RINGCENTRAL_CLIENT_ID'])
        web_socket_client = sdk.create_web_socket_client()
        print("web_socket_client: ", web_socket_client)
        
        web_socket_client.on(WebSocketEvents.connectionCreated, on_ws_created)
        web_socket_client.on(WebSocketEvents.subscriptionCreated, on_sub_created)
        web_socket_client.on(WebSocketEvents.receiveSubscriptionNotification, on_notification)

        asyncio.create_task(ping_pong_handler(web_socket_client._web_socket, None))


        await asyncio.gather(
            web_socket_client.create_new_connection(), 
            web_socket_client.create_subscription(["/restapi/v1.0/account/~/extension/~/message-store"])
        )
    except KeyboardInterrupt:
        print("Stopped by User")

if __name__ == "__main__":
    # asyncio.run(subscribe())
    asyncio.get_event_loop().run_until_complete(subscribe())

