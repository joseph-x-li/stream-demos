from pystreaming import Collector, collate, display
import zmq, cv2

def drawboxes(handler):
    for frame, predictions, idx in handler():
        yield 
    


def main():
    stream = Collector(zmq.Context(), "tcp://*:5555", mapreduce=True)
    display(
    	drawboxes(
            collate(
                stream.handler(), 
                getter=lambda x : (x[0], None, x[1]))
        )
	)
    
    
if __name__ == '__main__':
    main()
