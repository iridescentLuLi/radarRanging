import numpy as np 

class SignalArray:

    def __init__(self, windowSize = 100):

        self.initSize = windowSize
        self.dataArray = []
        self.ArraySize = windowSize
        self.currentDataSize = 0
        self.signalLen = 0


    def add(self, signal):

        if len(self.dataArray) == 0:
            self.signalLen = len(signal)
            self.dataArray = np.zeros((self.ArraySize, self.signalLen))

        if self.currentDataSize >= self.ArraySize:
            self.ArraySize = self.ArraySize * 2
            temp = self.dataArray.copy()
            self.dataArray = np.zeros((self.ArraySize, self.signalLen))
            self.dataArray[0:self.currentDataSize] = temp
        
        self.dataArray[self.currentDataSize] = signal
        self.currentDataSize += 1


    def getAllArrays(self):

        return self.dataArray[:self.currentDataSize]


    def getLastFrame(self, windowLength):

        if windowLength > self.currentDataSize:
            temp = np.zeros((windowLength, self.signalLen))
            temp[0: self.currentDataSize] = self.dataArray[0: self.currentDataSize]
            return temp
        else:
            return self.dataArray[self.currentDataSize - windowLength: self.currentDataSize]

