import requests

query = '''
query SayHello($name: String){
  hello(name: $name)
}
'''
r = requests.post("http://127.0.0.1:8000", json={"query": query, "variables": {"name": "GraphQL"}})
print(r.json())
