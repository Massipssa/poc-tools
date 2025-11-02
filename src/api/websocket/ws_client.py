
import asyncio, websockets

async def run():
    async with websockets.connect("ws://127.0.0.1:8765") as ws:
        await ws.send("hello websocket")
        print(await ws.recv())

if __name__ == "__main__":
    asyncio.run(run())
