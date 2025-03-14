import zmq
import msgpack
import math

ctx = zmq.Context()

server = ctx.socket(zmq.REP)
server.bind("tcp://*:5555")

while True:
    msg_p = server.recv()
    msg = msgpack.unpackb(msg_p)
    request = msg.get("request")
    if(request == 1):
        v1 = int(msg.get("valor1"))
        v2 = int(msg.get("valor2"))
        result = v1 + v2
        ans = {"status": "ok", "reply": "World", "result": result}
        ans_p = msgpack.packb(ans)
        server.send(ans_p)
    elif(request == 2):
        v1 = int(msg.get("valor1"))
        v2 = int(msg.get("valor2"))
        result = v1 - v2
        ans = {"status": "ok", "result": result}
        ans_p = msgpack.packb(ans)
        server.send(ans_p)
    elif(request == 3):
        v1 = int(msg.get("valor1"))
        v2 = int(msg.get("valor2"))
        result = v1 * v2
        ans = {"status": "ok", "result": result}
        ans_p = msgpack.packb(ans)
        server.send(ans_p)
    elif(request == 4):
        v1 = int(msg.get("valor1"))
        v2 = int(msg.get("valor2"))
        if(v2 == 0):
            ans = {"status": "ERROR", "Reply": "Divisao por zero"}
            ans_p = msgpack.packb(ans)
            server.send(ans_p)
        else:
            result = v1/v2
            sobra = v1%v2
            ans = {"status": "ok", "result": result, "sobra": sobra}
            ans_p = msgpack.packb(ans)
            server.send(ans_p)
    elif(request == 5):
        v1 = int(msg.get("valor1"))
        if(v1 < 0):
            ans = {"status": "ERROR", "Reply": "Raiz de numero negativo"}
            ans_p = msgpack.packb(ans)
            server.send(ans_p)
        else:
            result = math.sqrt(v1)
            ans = {"status": "ok", "result": result}
            ans_p = msgpack.packb(ans)
            server.send(ans_p)

server.close()
ctx.close()
