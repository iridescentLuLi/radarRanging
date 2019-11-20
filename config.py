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


