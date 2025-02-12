from concurrent import futures
import grpc
import helloword_pb2
import helloword_pb2_grpc

class Greeter(helloword_pb2_grpc.GreeterServicer):
    def HelloWorld(self, request, context):
        print(f"Mensagem do cliente: {request.mensagem}")
        return helloword_pb2.MsgServidor( mensagem="World")

endereco = "[::]:50051"
servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
helloword_pb2_grpc.add_GreeterServicer_to_server(Greeter(), servidor)

servidor.add_insecure_port(endereco)
servidor.start()
print(f"Servidor escutando em {endereco}")
servidor.wait_for_termination()
