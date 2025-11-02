
from aiohttp import web
from aiortc import RTCPeerConnection, RTCSessionDescription

pcs = set()

async def offer(request):
    params = await request.json()
    pc = RTCPeerConnection()
    pcs.add(pc)

    @pc.on("datachannel")
    def on_dc(channel):
        @channel.on("message")
        def on_message(message):
            channel.send(f"echo: {message}")

    await pc.setRemoteDescription(RTCSessionDescription(**params))
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)
    return web.json_response({"sdp": pc.localDescription.sdp,
                              "type": pc.localDescription.type})

app = web.Application()
app.router.add_post("/offer", offer)

if __name__ == "__main__":
    print("WebRTC signaling on http://127.0.0.1:8080/offer")
    web.run_app(app, port=8080)
