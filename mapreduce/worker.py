import pystreaming as ps
import zmq
from models import loadmodel
import cv2
import jetson.utils

def main():

    net = loadmodel()
    
    def func(frame):
        """Return a list of detected objects 

        Args:
            frame (np.ndarray): Image frame. Will be resized to 480 width x 320 height
        """
        nonlocal net

        frame = cv2.resize(frame, (480, 320))
        frame = jetson.utils.cudaFromNumpy(frame)
        detections = net.Detect(frame)
        ret = [(d.ClassID, d.Top, d.Left, d.Right, d.Bottom) for d in detections]
        print(ret)
        return ret
        
    
    worker = ps.Worker(zmq.Context(), "tcp://172.16.0.4:5555", "tcp://172.16.0.25:5556")
    worker.run(func)
    
if __name__ == '__main__':
    main()