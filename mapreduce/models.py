import jetson.inference

def loadmodel():
    # load model
    net = jetson.inference.detectNet("ssd-mobilenet-v2", None, 0.5)
    return net