import jetson.utils

def loadmodel():
    # load model
    net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)