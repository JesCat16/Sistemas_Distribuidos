import zmq
import msgpack
import time

ctx = zmq.Context()

server = ctx.socket(zmq.REP)
server.bind("tcp://*:5555")
client = ctx.socket(zmq.REQ)
client.connect("tcp://localhost:5556")
atual = 0


for i in range(11):
    if i == 2:
        msg_p = server.recv()
        msg = msgpack.unpackb(msg_p)
    elif i == 3:
        msg = {"timestamp": atual, "mensagem": "horas"}
        msg_p = msgpack.packb(msg)
        client.send(msg_p)
    elif i == 7:
        reply_p = client.recv()
        reply = msgpack.unpackb(reply_p)
        print(f"Mensagem{reply}")
        hora = int(reply["timestamp"])
        atual = hora + 1
    elif i == 8:
        ans = {"timestamp": atual, "mensagem": "horas"}
        ans_p = msgpack.packb(ans)
        server.send(ans_p)
    print(atual)
    atual = atual + time.time()
    time.sleep(1)