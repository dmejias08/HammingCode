class Hamming():
    def __init__(self, data, parity):
        self.lengthData = len(data)
        self.parityPositionsList = self.getParityBits(self.lengthData)
        self.hammingCodeWithZeros = self.insertZeroToRedudantBits(data, self.parityPositionsList)
        self.encoded = self.defineParityBits(self.hammingCodeWithZeros, self.parityPositionsList, parity)


    def getParityBits(self, lengthData):
        pos = []

        for i in range(lengthData):
            if(2**i>=lengthData + 1 + i):
                return pos
            pos.append(2**i)

    def insertZeroToRedudantBits(self, data, redundatPositionsList):
        currentDataPosition = 0
        lengthData = len(data)
        positionsAdded = len(redundatPositionsList)
        hammingEncoded = ''

        for i in range(1, lengthData + positionsAdded + 1):
            if i in self.parityPositionsList:
                hammingEncoded += '0'
            else:
                hammingEncoded += data[currentDataPosition]
                currentDataPosition+=1

        return hammingEncoded

    def defineParityBits(self, hammingCodeWithZeros, parityPositionsList, parity):
        hammingCodeLength = len(hammingCodeWithZeros)
        hammingCodeResult = hammingCodeWithZeros

        for parityPosition in parityPositionsList:
            val = 0 if parity == "par" else 1

            for hammingCodePosition in range(1, hammingCodeLength + 1):
                if(hammingCodePosition & parityPosition == parityPosition):
                    val = val ^ int(hammingCodeWithZeros[hammingCodePosition - 1])

            hammingCodeResult = hammingCodeResult[:parityPosition-1] + str(val) + hammingCodeResult[parityPosition:]

        return hammingCodeResult


    def detectError(self, hammingCodeToCheck, parityPositionsList, parity):
        hammingCodeLenght = len(hammingCodeToCheck)
        result = 0

        for parityPosition in range(len(parityPositionsList)):
            val = 0 if parity == "par" else 1
            for hammingCodePosition in range(1, hammingCodeLenght + 1):
                if(hammingCodePosition & (2**parityPosition) == (2**parityPosition)):
                    val = val ^ int(hammingCodeToCheck[ hammingCodePosition - 1])

            result = result + val*(10**parityPosition)

        return int(str(result), 2)
