from concurrent import futures
import grpc
import calculadora_pb2
import calculadora_pb2_grpc

# class Greeter(calculadora_pb2_grpc.GreeterServicer):
#     def HelloWorld(self, request, context):
#         print(f"Mensagem do cliente: {request.mensagem}")
#         return calculadora_pb2.MsgServidor( mensagem="World")
class Calculadora(calculadora_pb2_grpc.GreeterServicer):
    def Soma(self, request, context):
        return calculadora_pb2.Resultado(resultado= request.valor1 + request.valor2)
    def Subtracao(self, request, context):
       return calculadora_pb2.Resultado(resultado= request.valor1 - request.valor2)
    def Multiplicacao(self, request, context):
        return calculadora_pb2.Resultado(resultado= request.valor1 * request.valor2)
    def Divisao(self, request, context):
        return calculadora_pb2.Resultado(resultado= request.valor1 / request.valor2)

endereco = "[::]:50051"
servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
calculadora_pb2_grpc.add_GreeterServicer_to_server(Calculadora(), servidor)

servidor.add_insecure_port(endereco)
servidor.start()
print(f"Servidor escutando em {endereco}")
servidor.wait_for_termination()
