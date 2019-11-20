from PyQt5.QtWidgets import QMainwindow, QApplication, QMessageBox
import sys
import numpy as np
import socket
import struct
import config
from threading import Thread, Lock

lock = Lock()
ip = '192.168.1.151'
port = 21210
ipAddress = (ip, port)
threadRunningFlag = False
rangingModeFlag = 2
nodeIdA = 0
nodeIdB = 0
queue = []

class AppWindow(QMainwindow):
    def __init__(self):
        super().__init__()
        self.currentRadarConfig
        self.currentMode = 2 #0 for range mode, 1 for radar mode
        self.benchMarkDistance = 0 #distance between marks
        

    def setCallback(self):
        
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
        

class ProducerThread(Thread):
    
    def run(self):
        global ipAddress
        global threadRunningFlag
        global queue
        global nodeIdA
        global nodeIdB

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(ipAddress)

        while True:
            if not threadRunningFlag:
                continue

            while True: # ranging
                setRandingMode = pack('>HHI', 0xf003, 0, 0) # 0 for ranging, 1 for radar
                s.sendto(setRandingMode, address)
                rangingModeConfirm, add = s.recvfrom(12)
                messageId, opMode, confirmStatus = unpack('>HII', rangingModeConfirm[2:12])
                if confirmStatus != 0:
                    continue
                if messageId != 0:
                    continue
                if opMode != 0:
                    print('ranging ok')
                    break

            while True: # radar
                setRadarMode = pack('>HHI', 0xf003, 1, 1)
                s.sendto(setRadarMode, address)
                radarModeConfirm, add = s.recvfrom(12)
                messageId, opMode, confirmStatus = unpack('>HII', rangingModeConfirm[2:12])
                if confirmStatus != 0:
                    continue
                if messageId != 1:
                    continue
                if opMode == 1:
                    print('radar ok')
                    s.sendto(pack('>HHHHI', 0x1003, 2, 1, 0, 0))
                    while True:
                        scanInfo, add = s.recvfrom(2000)
                        if scanInfo[0:2] = b'\xf2\x01':
                            thisLen, totalLen, thisIndex, totalIndex = unpack('>HIHH', scanInfo[42: 52])
                            print(thisLen, totalLen, thisIndex, totalIndex)
                            newSignal = np.frombuffer(scanInfo[52:thisLen * 4 + 52])
                            lock.acquire()
                            queue.append(newSignal))
                            lock.release()
                            break
                    break
            print('---------------------------------')

