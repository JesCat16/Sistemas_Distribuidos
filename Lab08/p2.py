import zmq
import msgpack

ctx = zmq.Context()

pub = ctx.socket(zmq.PUB)
pub.connect("tcp://localhost:5555")

sub = ctx.socket(zmq.SUB)
sub.connect("tcp://localhost:5556")

atual = 0


for i in range(11):
    if i == 2:
        topic = str("p1Top2")
        sub.setsockopt_string(zmq.SUBSCRIBE, topic)
        msg_p = sub.recv()
        msg = msgpack.unpackb(msg_p)
    elif i == 3:
        topic = str("p2Top3")
        msg = {"timestamp": atual, "mensagem": "horas"}
        msg_p = msgpack.packb(msg)
        pub.send_string(f"{topic} {msg_p}")
    elif i == 7:
        topic = str("p3Top2")
        sub.setsockopt_string(zmq.SUBSCRIBE, topic)
        reply_p = sub.recv()
        reply = msgpack.unpackb(reply_p)
        print(f"Mensagem{reply}")
        # hora = int(reply["timestamp"])
        # atual = hora + 1
    elif i == 8:
        topic = str("p2Top1")
        ans = {"timestamp": atual, "mensagem": "horas"}
        ans_p = msgpack.packb(ans)
        pub.send_string(f"{topic} {ans_p}")
    print(atual)
    atual = atual + 8