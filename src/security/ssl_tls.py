import requests
import http.server
import ssl

if __name__ == '__main__':

    # connect to secured ssl server
    response = requests.get('https://google.com/')
    print(response)

    # create http server with ssl certificate
    httpd = http.server.HTTPServer(('localhost', 443), http.server.SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   certfile='./cert/certificate.pem',
                                   keyfile='./cert/key.pem',
                                   server_side=True,
                                   ssl_version=ssl.PROTOCOL_TLS)
    httpd.serve_forever()
