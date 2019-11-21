from PyQt5.QtWidgets import QMainwindow, QApplication, QMessageBox
from PyQt5 import QtCore
import sys
import numpy as np
import socket
import struct
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import config
from threading import Thread, Lock
from scipy.signal import hilbert
from mainWindow import Ui_MainWindow
import signalArray
import math
import datetime

lock = Lock()
ip = '192.168.1.151'
port = 21210
ipAddress = (ip, port)
threadRunningFlag = False
updateFigureFlag = False
nodeIdA = 0, nodeIdB = 0, xCoordinate = 0, yCoordinate = 0
windowLength = 200
queue = []

class AppWindow(QMainwindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setCallback()
        self.currentRadarConfig
        self.benchMarkDistance = 0 #distance between marks
        self.figureBScan = plt.figure()
        self.canvasBScan = FigureCanvas(self.figureBScan)
        self.ui.BScanImage.addWidget(self.canvasBScan)
        self.axBScan = self.figureBScan.add_subplot(111)
        self.canvasBScan.draw()

        self.figureCoordinate = plt.figure()
        self.canvesCoordinate = FigureCanvas(self.figureCoordinate)
        self.ui.RangeNetPlot.addWidget(self.canvesCoordinate)
        self.axCoordinate = self.figureCoordinate.add_subplot(111)
        self.canvesCoordinate.draw()

        plt.tight_layout()

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.updateCanvas)
        timer.start(50)

        self.producer = ProducerThread().start()
        


    def setCallback(self):
        self.ui.btnRadarConfigRead.clicked.connect(self.readConfig)
        self.ui.btnRadarConfigSet.clicked.connect(self.writeConfig)
        

        
    def readConfig(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((ip, port))

        requestConfigMsg = struct.pack('>HH', 0x1002, 0)
        s.sendto(requestConfigMsg, ipAddress)
        configMessage, addr = s.recvfrom(44)
        self.currentRadarConfig = config.RadarConfig(configMessage)

      

        #set ui

    def writeConfig(self):
        
        pass
        #set node id

    
    def updateCanvas(self):
        
        if not updateFigureFlag:
            return
        global queue
        if queue:

            lock.acquire
            for line in queue:
                self.dataOriginal.add(line[2:])
            self.axBScan.clear()
            lastFrame = self.dataOriginal.getLastFrame(windowLength + 1)
            envelop = np.abs(hilbert(lastFrame[0:-1] - lastFrame[1:]))
            envelop = np.clip(np.round(63 * envelop / 10e3) + 1, -1e5, 64)
            self.axBScan.imshow(envelop, aspect = 'auto')
            self.canvasBScan.draw()
            queue = []
            lock.release()

            # draw range plot
            xCoordinate = (rangeA**2 + self.benchMarkDistance**2 - rangeB**2) / (2 * self.benchMarkDistance)
            yCoordinate = math.sqrt(rangeA**2 - self.benchMarkDistance**2)
            x = [0, self.benchMarkDistance, xCoordinate]
            y = [0, 0, yCoordinate]
            self.axCoordinate.scatter(x, y)
            self.canvesCoordinate.draw()

            

    def clearWindow(self):
        self.dataOriginal = signalArray.SignalArray()
        self.updateCanvas()


    def saveData(self):
        fileName = str(datetime.datetime.now())[0:19].replace(' ', '_')\
            .replace('-', '_').replace(':', '_').replace('.', '_')
        np.savetxt(fileName, self.dataOriginal.getAllArrays())
        self.showMessage(fileName + ' is saved !')
        # save data array

    def showMessage(self, text):
        msg = QMessageBox()
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok)
        ret = msg.exec_()


    def runAndStop(self):
        global threadRunningFlag
        global updateFigureFlag
        if threadRunningFlag:
            threadRunningFlag = False
            updateFigureFlag = False
            self.ui.btnStart.setText('Start')
        else:
            self.dataOriginal = signalArray.SignalArray()
            self.dataProcessed = []
            threadRunningFlag = True
            updateFigureFlag = True
            self.ui.btnStart.setText('End')

        

class ProducerThread(Thread):
    
    def run(self):
        global ipAddress
        global threadRunningFlag
        global queue
        global nodeIdA, nodeIdB, xCoordinate, yCoordinate
        
        setRandingMode = pack('>HHI', 0xf003, 0, 0) # 0 for ranging, 1 for radar
        setRadarMode = pack('>HHI', 0xf003, 1, 1) 
        radarInfoRequest = pack('>HHHHI', 0x1003, 2, 1, 0, 0)
        

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(ipAddress)

        while True:
            if not threadRunningFlag:
                continue

            while True: 
                # ranging
                rangeStatus = True
                s.sendto(setRandingMode, address)
                rangingModeConfirm, add = s.recvfrom(12)
                messageId, opMode, confirmStatus = unpack('>HII', rangingModeConfirm[2:12])
                if confirmStatus != 0:
                    continue
                if messageId != 0:
                    continue
                if opMode != 0:
                    # range A
                    whichNodeId = nodeIdA
                    rangeInfoRequest = pack('>HHIBBH', 0x0003, 3, nodeIdA, 2, 0, 0)
                    s.sendto(rangeInfoRequest)
                    while True:
                        rangePacked, add = s.recvfrom(2000)
                        if rangePacked[0:2] == b'\x02\x01':
                            rangeInfo = unpack('>HHIBBHI', range_info[0:16])
                            if rangeInfo[2] != nodeIdA:
                                continue
                            rangeA = rangeInfo[6]
                        break
                    #range B
                    rangeInfoRequest = pack('>HHIBBH', 0x0003, 3, nodeIdB, 2, 0, 0)
                    s.sendto(rangeInfoRequest)
                    while True:
                        rangePacked, add = s.recvfrom(2000)
                        if rangePacked[0:2] == b'\x02\x01':
                            rangeInfo = unpack('>HHIBBHI', range_info[0:16])
                            if rangeInfo[2] != nodeIdB:
                                continue
                            rangeB = rangeInfo[6]
                        break

                    print('ranging ok')
                    break

            while True:
                # radar
                cont = 0
                s.sendto(setRadarMode, address)
                radarModeConfirm, add = s.recvfrom(12)
                messageId, opMode, confirmStatus = unpack('>HII', rangingModeConfirm[2:12])
                if confirmStatus != 0:
                    continue
                if messageId != 1:
                    continue
                if opMode == 1:
                    print('radar ok')
                    s.sendto(radarInfoRequest)
                    while True:
                        scanInfo, add = s.recvfrom(2000)
                        if scanInfo[0:2] = b'\xf2\x01':
                            thisLen, totalLen, thisIndex, totalIndex = unpack('>HIHH', scanInfo[42: 52])
                            print(thisLen, totalLen, thisIndex, totalIndex)
                            newSignal = np.frombuffer(scanInfo[52:thisLen * 4 + 52])
                            xCoordinate = (rangeA**2 + self.benchMarkDistance**2 - rangeB**2) / (2 * self.benchMarkDistance)
                            yCoordinate = math.sqrt(rangeA**2 - self.benchMarkDistance**2)
                            oneFrame = np.append(xCoordinate, yCoordinate)
                            oneFrame = np.append(oneFrame, newSignal)

                            lock.acquire()
                            queue.append(oneFrame)
                            lock.release()
                            break

                    break
            print('---------------------------------')