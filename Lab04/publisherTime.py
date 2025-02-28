import time
import zmq

ctx = zmq.Context.instance()
pub = ctx.socket(zmq.PUB)
pub.connect("tcp://localhost:5555")

while True:
    msg = str(time.time())
    topic = str("time")
    print(f"msg: {msg}")
    pub.send_string(f"{topic} {msg}")
    time.sleep(1)

ctx.close()
pub.close()
