
import grpc, hello_pb2, hello_pb2_grpc

def main():
    with grpc.insecure_channel("127.0.0.1:50051") as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        resp = stub.SayHello(hello_pb2.HelloRequest(name="gRPC"))
        print(resp.message)

if __name__ == "__main__":
    main()
