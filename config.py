import numpy as np
import struct
import math

class RadarConfig:
    def __init__(self, mrmConfigMsg):

        mrmConfigMsg = struct.pack('>HH', 0x1002, 0)
        s.sendto(mrmConfigMsg, )
        structPattern = '>HHIIIHHHHHHBBBBBBBBII'
        (self.messageType, self.messageID, self.nodeID, self.scanStart, self.scanEnd,
        self.scanResolution, self.baseIntegrationIndex, self.seg1, self.seg2,
        self.seg3, self.seg4, self.seg5, self.seg6, self.seg7, self.seg8,
        self.antennaMode, self.transmitGain, self.codeChannel, self.persistFlag,
        self.timeStamp, self.status) = unpack(structPattern, configMsg)

    def configToByte(self):

        self.persistFlag = 1
        self.messageType = 0x1001
        self.nodeID = 100
        self.scanResolution = 32
        structPattern = '>HHIIIHHHHHHBBBBBBBB'
        return pack(
            structPattern,
            self.messageType, self.messageID, self.nodeID, self.scanStart, self.scanEnd,
            self.scanResolution, self.baseIntegrationIndex, self.seg1, self.seg2,self.seg3,
            self.se4, self.seg5, self.seg6, self.seg7, self.seg8, self.antennaMode,
            self.transmitGain, self.codeChannel, self.persistFlag)


def ps2m(ps):

    c = 0.29979
    dT0 = 10
    return round(c * (ps / 1000 - dT0) / 2, 2)

def m2ps(m1, m2):

    c = 0.29979
    dTmin = 1 / (512 * 1.024)
    Tbin = 32 * dTmin
    dNBin = 96
    dT0 = 10
    T1 = 2 * m1 / c + dT0
    T2 = 2 * m2 / c + dT0

    Nbin = (T2 - T1) / Tbin
    Nseg = math.ceil(Nbin / dNBin)
    Nbin = dNBin * Nseg

    T1 = math.floor(1000 * dTmin * math.floor(T1 / dTmin))
    T2 = math.floor(1000 * dTmin * math.floor(T2 / dTmin))
    return T1, T2

