import pystreaming as ps
import zmq
from models import loadmodel

def main():

    model = loadmodel()
    
    def func(frame):
        """Return a list of detected objects 

        Args:
            frame (): Image frame of size ()
        """
        nonlocal model
        assert 
        if frame.shape != (, 3):
            frame = frame[?,?,:]
        
        return model(frame)
        
    
    worker = ps.Worker(zmq.Context(), "tcp://172.16.0.4:5555", "tcp://172.16.0.25:5555")
    worker.run(func)
    
if __name__ == '__main__':
    main()