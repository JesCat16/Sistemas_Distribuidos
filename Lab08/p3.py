import zmq
import msgpack

ctx = zmq.Context()
pub = ctx.socket(zmq.PUB)
pub.connect("tcp://localhost:5555")

sub = ctx.socket(zmq.SUB)
sub.connect("tcp://localhost:5556")


atual = 0
for i in range(11):
    if i == 4:
        topic = str("p2Top3")
        sub.setsockopt_string(zmq.SUBSCRIBE, topic)
        msg_p = sub.recv()
        msg = msgpack.unpackb(msg_p)
    elif i == 6:
        topic = str("p3Top2")
        ans = {"timestamp": atual, "mensagem": "horas"}
        ans_p = msgpack.packb(ans)
        pub.send_string(f"{topic} {ans_p}")
    atual = atual + 10
