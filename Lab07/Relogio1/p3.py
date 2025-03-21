import zmq
import msgpack

ctx = zmq.Context()

server = ctx.socket(zmq.REP)
server.bind("tcp://*:5556")
atual = 0
for i in range(11):
    if i == 4:
        msg_p = server.recv()
        msg = msgpack.unpackb(msg_p)
    elif i == 6:
        ans = {"timestamp": atual, "mensagem": "horas"}
        ans_p = msgpack.packb(ans)
        server.send(ans_p)
    atual = atual + 10
