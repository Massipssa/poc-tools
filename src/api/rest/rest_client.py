
import requests
base = "http://127.0.0.1:8000"
print("CREATE:", requests.post(f"{base}/todos", json={"title": "Learn REST"}).json())
print("GET:", requests.get(f"{base}/todos/todo:1").json())
