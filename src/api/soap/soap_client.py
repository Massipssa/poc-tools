
from zeep import Client

# pip install zeep
wsdl = "http://127.0.0.1:8000/?wsdl"
c = Client(wsdl)
print(c.service.say_hello("Massipssa"))
