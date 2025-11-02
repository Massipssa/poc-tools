
from flask import Flask, request
app = Flask(__name__)

@app.post("/hook")
def hook():
    event = request.json
    print("Got event:", event)
    return ("", 204)

if __name__ == "__main__":
    print("Webhook receiver on http://127.0.0.1:5000/hook")
    app.run(port=5000)
