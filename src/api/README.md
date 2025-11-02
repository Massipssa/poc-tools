
# Python API Styles — Minimal Examples

This repo contains small, runnable examples for seven API styles:
REST, SOAP, gRPC, GraphQL, Webhooks, WebSocket, and WebRTC.

Each folder has:

- `server.py` (or appropriately named server)
- `client.py` (or sender for webhooks)
- `requirements.txt`
- (gRPC only) a `.proto` file and generation command in README section below

## Quick Start

1) Create a fresh virtualenv (optional but recommended).
2) `cd` into a folder, `pip install -r requirements.txt`.
3) Start the server (see commands below).
4) Run the client in a separate terminal.

---

## REST (FastAPI)

```bash
cd rest
pip install -r requirements.txt
uvicorn rest_server:app --reload --port 8000
# in another terminal
python rest_client.py
```

## SOAP (Spyne)

```bash
cd soap
pip install -r requirements.txt
python soap_server.py
# in another terminal
python soap_client.py
# WSDL: http://127.0.0.1:8000/?wsdl
```

## gRPC

Generate Python code from the proto (first time only):

```bash
cd grpc
pip install -r requirements.txt
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hello.proto
python grpc_server.py
# in another terminal
python grpc_client.py
```

## GraphQL (Strawberry)

```bash
cd graphql
pip install -r requirements.txt
uvicorn graphql_server:app --reload --port 8000
python graphql_client.py
```

## Webhooks (Flask)

```bash
cd webhooks
pip install -r requirements.txt
python webhook_server.py  # receiver
# in another terminal (sender)
python webhook_sender.py
```

## WebSocket (websockets)

```bash
cd websocket
pip install -r requirements.txt
python ws_server.py
# in another terminal
python ws_client.py
```

## WebRTC (aiortc + aiohttp)
>
> Minimal data-channel echo demo using simple HTTP signaling.

```bash
cd webrtc
pip install -r requirements.txt
python webrtc_server.py
# in another terminal
python webrtc_client.py
```
