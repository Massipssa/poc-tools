
import asyncio, websockets

async def echo(ws):
    async for msg in ws:
        await ws.send(f"echo: {msg}")

async def main():
    async with websockets.serve(echo, "127.0.0.1", 8765):
        print("WebSocket server on ws://127.0.0.1:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
