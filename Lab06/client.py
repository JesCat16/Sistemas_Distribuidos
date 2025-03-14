# A partir do código de exemplo disponível no repositório, implemente uma calculadora que faz as operações de soma, subtração, multiplicação, 
# divisão de ponto flutuante, divisão de inteiros (resultado e resto) e raiz quadrada de números positivos. 
# O cliente deve pedir para o usuário entrar com os valores e exibir o resultado da operação.
# A mensagem de retorno do servidor deve conter um código do status para o cliente saber se a operação foi realizada ou teve algum erro, além de todos os valores que são resulado da operação.

import zmq
import msgpack

ctx = zmq.Context()
client = ctx.socket(zmq.REQ)
client.connect("tcp://localhost:5555")

while True:
    print("Que deseja fazer:")
    operacao = int(input(" Soma:1\n Subtracao:2\n Multiplicacao:3\n Divisao:4\n Raiz:5\n"))
    if(operacao == 1):
        v1 = int(input("Valor 1:"))
        v2 = int(input("Valor 2:"))
    elif(operacao == 2):
        v1 = int(input("Valor 1:"))
        v2 = int(input("Valor 2:"))
    elif(operacao == 3):
        v1 = int(input("Valor 1:"))
        v2 = int(input("Valor 2:"))
    elif(operacao == 4):
        v1 = int(input("Valor 1:"))
        v2 = int(input("Valor 2:"))
    elif(operacao == 5):
        v1 = int(input("Valor:"))
        v2 = 0
    msg = {"valor1": v1, "valor2": v2, "request": operacao}
    msg_p = msgpack.packb(msg)
    client.send(msg_p)

    reply_p = client.recv()
    reply = msgpack.unpackb(reply_p)
    print(f"Received reply: {reply}")

client.close()
ctx.close()
