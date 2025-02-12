import grpc
import helloword_pb2
import helloword_pb2_grpc

print("Cliente conectando com servidor")

porta = "50051"
endereco = "localhost"

with grpc.insecure_channel(f"{endereco}:{porta}") as channel:
    stub = helloword_pb2_grpc.GreeterStub(channel)
    resposta = stub.HelloWorld(helloword_pb2.MsgCliente(mensagem="hello"))
    print(f"Resposta do servidor: {resposta.mensagem}")
