import grpc
from concurrent import futures
import hello_pb2, hello_pb2_grpc


class Greeter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloReply(message=f"Hello, {request.name}")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:50051")
    print("gRPC server on 127.0.0.1:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("Starting gRPC server...")
    serve()
