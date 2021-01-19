from pystreaming import Collector, collate, display
from collections import deque
import zmq, cv2, time

cdict = {
    1: "person",
    2: "bicycle",
    3: "car",
    4: "motorcycle",
    5: "airplane",
    6: "bus",
    7: "train",
    8: "truck",
    9: "boat",
    10: "traffic light",
    11: "fire hydrant",
    13: "stop sign",
    14: "parking meter",
    15: "bench",
    16: "bird",
    17: "cat",
    18: "dog",
    19: "horse",
    20: "sheep",
    21: "cow",
    22: "elephant",
    23: "bear",
    24: "zebra",
    25: "giraffe",
    27: "backpack",
    28: "umbrella",
    31: "handbag",
    32: "tie",
    33: "suitcase",
    34: "frisbee",
    35: "skis",
    36: "snowboard",
    37: "sports ball",
    38: "kite",
    39: "baseball bat",
    40: "baseball glove",
    41: "skateboard",
    42: "surfboard",
    43: "tennis racket",
    44: "bottle",
    46: "wine glass",
    47: "cup",
    48: "fork",
    49: "knife",
    50: "spoon",
    51: "bowl",
    52: "banana",
    53: "apple",
    54: "sandwich",
    55: "orange",
    56: "broccoli",
    57: "carrot",
    58: "hot dog",
    59: "pizza",
    60: "donut",
    61: "cake",
    62: "chair",
    63: "couch",
    64: "potted plant",
    65: "bed",
    67: "dining table",
    70: "toilet",
    72: "tv",
    73: "laptop",
    74: "mouse",
    75: "remote",
    76: "keyboard",
    77: "cell phone",
    78: "microwave",
    79: "oven",
    80: "toaster",
    81: "sink",
    82: "refrigerator",
    84: "book",
    85: "clock",
    86: "vase",
    87: "scissors",
    88: "teddy bear",
    89: "hair drier",
    90: "toothbrus",
}

font = cv2.FONT_HERSHEY_SIMPLEX
fontcolor = (255, 0, 0)

def drawboxes(handler):
    for frame, predictions, idx in handler:
        for predictclass, t, l, r, b in predictions:
            classname = cdict[predictclass]
            TL = (int(l), int(t))
            BR = (int(r), int(b))
            cv2.rectangle(frame, TL, BR, fontcolor, 2)
            cv2.putText(frame, classname, (int(l) + 5, int(t) + 25), font, 1, fontcolor, 2)
        yield frame 
        
def dispfps(handler, n=100):
    """Average iterations per second over last {n} iterations.
    """
    times = deque()
    for data in handler:
        end = time.time()
        times.append(end)
        if len(times) > n:
            diff = end - times.popleft()
            print(f"\rFPS: {(n / diff):.3f}", end="")
        yield data
    
def main():
    stream = Collector(zmq.Context(), "tcp://*:5556", mapreduce=True)
    display(
    	dispfps(
            drawboxes(
                collate(
                    stream.handler()
                )
            )
        )
	)
    
    
if __name__ == '__main__':
    main()
