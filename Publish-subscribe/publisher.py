import time
import zmq

ctx = zmq.Context.instance()
pub = ctx.socket(zmq.PUB)
pub.connect("tcp://localhost:5555")

while True:
    msg = str(time.time())
    print(f"msg: {msg}")
    pub.send_string(msg)
    time.sleep(1)

ctx.close()
pub.close()
