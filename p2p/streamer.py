import pystreaming, cv2, zmq, time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

stream = pystreaming.Streamer(zmq.Context(), "tcp://*:5555") 
stream.start()

start = time.time()
n = 0
while True:
    n += 1
    ret, frame = cap.read()
    stream.send(frame)
    print(f"\rFPS: {(n / (time.time() - start)):.3f}", end="")
