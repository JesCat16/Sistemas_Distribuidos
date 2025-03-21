import zmq
import msgpack
import time

ctx = zmq.Context()
client = ctx.socket(zmq.REQ)
client.connect("tcp://localhost:5555")
atual = 0

for i in range(11):
    if i == 1:
        msg = {"timestamp": atual, "mensagem": "horas"}
        msg_p = msgpack.packb(msg)
        client.send(msg_p)
    elif i == 9:
        reply_p = client.recv()
        reply = msgpack.unpackb(reply_p)
        hora = int(reply["timestamp"])
        print(f"Hora Recebida: {reply}")
        atual = hora + 1
    print(atual)
    atual = atual + time.time()
    time.sleep(2)
        



