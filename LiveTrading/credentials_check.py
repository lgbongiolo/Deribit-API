import asyncio
import websockets
import json


client_id = "" #replace this with your key
client_secret = "" # replace with your secret


msg = \
{
  "jsonrpc" : "2.0",
  "id" : 9929,
  "method" : "public/auth",
  "params" : {
    "grant_type" : "client_credentials",
    "client_id" : client_id,
    "client_secret" : client_secret
  }
}

async def call_api(msg):
   async with websockets.connect('wss://test.deribit.com/ws/api/v2') as websocket:
       await websocket.send(msg)
       while websocket.open:
           response = await websocket.recv()
           # do something with the response...
           return json.loads(response)


def async_loop(api, message):
    return asyncio.get_event_loop().run_until_complete(api(message))


def test_creds(api, msg):
    response = async_loop(api, json.dumps(msg))
    if 'error' in response.keys():
        print(f"Auth failed with error {response['error']}")
    else:
        print("Auth creds are good, it worked")


if __name__ =='__main__':
    test_creds(call_api, msg)