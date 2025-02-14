import grpc
import calculadora_pb2
import calculadora_pb2_grpc

print("Cliente conectando com servidor")

porta = "50051"
endereco = "localhost"

with grpc.insecure_channel(f"{endereco}:{porta}") as channel:
    stub = calculadora_pb2_grpc.GreeterStub(channel)
    print("O que quer fazer?\n Somar(1)\n Subtrair(2)\n Multiplicar(3)\n Dividir(4)")
    operacao = int(input())
    print("Insira os valores...")
    valor1 = int(input("Valor 1:"))
    valor2 = int(input("Valor 2:"))
    resultado = None
    stub = calculadora_pb2_grpc.GreeterStub(channel)
    valor = calculadora_pb2.Valores(valor1= valor1, valor2= valor2)
    if(operacao == 1):
        resultado = stub.Soma(valor)
    elif(operacao == 2):
        resultado = stub.Subtracao(valor)
    elif(operacao == 3):
        resultado = stub.Multiplicacao(valor)
    elif(operacao == 4):
        resultado = stub.Divisao(valor)
    else:
        print("Não foi encontrada")
    print(f"Resposta do servidor: {resultado.resultado}")
