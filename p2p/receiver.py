from pystreaming import Collector, collate, display
import zmq, cv2

def main():
    stream = Collector(zmq.Context(), "tcp://172.16.0.4:5555")
    display(
    	collate(stream.handler(), getter=lambda x : (x[0], None, x[1])),
    	getter=lambda x : x[0]
	)
    
    
if __name__ == '__main__':
    main()
