import zmq
import msgpack

ctx = zmq.Context.instance()
pub = ctx.socket(zmq.PUB)
pub.connect("tcp://localhost:5555")

sub = ctx.socket(zmq.SUB)
sub.setsockopt_string(zmq.SUBSCRIBE, "p2")
sub.connect("tcp://localhost:5556")

atual = 0
for i in range(11):
    if i == 1:
        topic = str("p1Top2")
        msg = {"timestamp": atual, "mensagem": "horas"}
        msg_p = msgpack.packb(msg)
        pub.send_string(f"{topic} {msg_p}")
    elif i == 9:
        topic = str("p2Top1") 
        reply_p = sub.recv()
        reply = msgpack.unpackb(reply_p)
        hora = int(reply["timestamp"])
        print(f"Hora Recebida: {reply}")
        atual = hora + 1
    print(atual)
    atual = atual + 6


