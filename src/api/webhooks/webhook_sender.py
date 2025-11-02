
import requests
r = requests.post("http://127.0.0.1:5000/hook",
                  json={"type":"user.created","id":123,"email":"a@b.com"})
print("Status:", r.status_code)
