from PyQt5.QtWidgets import QMainwindow, QApplication, QMessageBox
import sys
import numpy as np
import socket
import struct
import config
from threading import Thread, Lock
from main_window import Ui_MainWindow

lock = Lock()
ip = '192.168.1.151'
port = 21210
ipAddress = (ip, port)
threadRunningFlag = False
updateFigureFlag = False
nodeIdA = 0
nodeIdB = 0
rangeA = 0
rangeB = 0
queue = []

class AppWindow(QMainwindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setCallback()
        self.currentRadarConfig
        self.benchMarkDistance = 0 #distance between marks
        

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

        requestModeConfig = struct.pack('>HH', 0xf004, 0)
        s.sendto(requestModeConfig, ipAddress)
        modeConfig, addr = s.recvfrom(8)
        self.currentMode = struct.unpack('>I', modeConfig[4:8])

        #set ui

    def writeConfig(self):

        #set node id

        

    def runAndStop(self):
        global threadRunningFlag
        global updateFigureFlag
        if threadRunningFlag:
            threadRunningFlag = False
            updateFigureFlag = False
            self.ui.btnStart.setText('start')
        else:


        

class ProducerThread(Thread):
    
    def run(self):
        global ipAddress
        global threadRunningFlag
        global queue
        global nodeIdA, nodeIdB, rangeA, rangeB
        
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
                            lock.acquire()
                            queue.append(newSignal))
                            cont += 1
                            lock.release()
                            break
                    if cont == 5:
                        break
            print('---------------------------------')