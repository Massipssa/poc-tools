
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class HelloService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def say_hello(ctx, name):
        return f"Hello, {name}"

app = Application([HelloService], 'example.soap',
                  in_protocol=Soap11(validator='lxml'),
                  out_protocol=Soap11())
wsgi_app = WsgiApplication(app)

if __name__ == "__main__":
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("SOAP server on http://127.0.0.1:8000/?wsdl")
    server.serve_forever()
