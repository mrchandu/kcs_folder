import asyncio
import websockets

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        #await websocket.send("Hello world!")
        await websocket.recv()

asyncio.get_event_loop().run_until_complete(hello('wss://192.168.1.32/ws/channels/34a44798-40fa-44fb-9323-a516b03dee19/messages?authorization=c04b338d-af2c-4345-8bea-f1a4ead89a64'))