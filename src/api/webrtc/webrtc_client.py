
import asyncio, requests
from aiortc import RTCPeerConnection, RTCSessionDescription

async def main():
    pc = RTCPeerConnection()
    channel = pc.createDataChannel("chat")

    recv_done = asyncio.get_event_loop().create_future()

    @channel.on("message")
    def on_message(msg):
        print("received:", msg)
        if not recv_done.done():
            recv_done.set_result(True)

    offer = await pc.createOffer()
    await pc.setLocalDescription(offer)

    r = requests.post("http://127.0.0.1:8080/offer",
                      json={"sdp": pc.localDescription.sdp,
                            "type": pc.localDescription.type})
    answer = r.json()
    await pc.setRemoteDescription(RTCSessionDescription(**answer))

    channel.send("hello webrtc")
    await recv_done
    await pc.close()

if __name__ == "__main__":
    asyncio.run(main())
