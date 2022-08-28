
def getParityBits(lengthData):
    pos = []

    for i in range(lengthData):
        if(2**i>=lengthData + 1 + i):
            return pos
        pos.append(2**i)

def insertZeroToRedudantBits(data, redundatPositionsList):
    currentDataPosition = 0
    lengthData = len(data)
    positionsAdded = len(redundatPositionsList)
    hammingEncoded = ''

    for i in range(1, lengthData + positionsAdded + 1):
        if i in parityPositionsList:
            hammingEncoded += '0'
        else:
            hammingEncoded += data[currentDataPosition]
            currentDataPosition+=1

    return hammingEncoded

def defineParityBits(hammingCodeWithZeros, parityPositionsList, parity):
    hammingCodeLength = len(hammingCodeWithZeros)
    hammingCodeResult = hammingCodeWithZeros

    for parityPosition in parityPositionsList:
        val = 0 if parity == "par" else 1

        for hammingCodePosition in range(1, hammingCodeLength + 1):
            if(hammingCodePosition & parityPosition == parityPosition):
                val = val ^ int(hammingCodeWithZeros[hammingCodePosition - 1])

        hammingCodeResult = hammingCodeResult[:parityPosition-1] + str(val) + hammingCodeResult[parityPosition:]

    return hammingCodeResult


def detectError(hammingCodeToCheck, parityPositionsList, parity):
    hammingCodeLenght = len(hammingCodeToCheck)
    result = 0

    for parityPosition in range(len(parityPositionsList)):
        val = 0 if parity == "par" else 1
        for hammingCodePosition in range(1, hammingCodeLenght + 1):
            if(hammingCodePosition & (2**parityPosition) == (2**parityPosition)):
                val = val ^ int(hammingCodeToCheck[ hammingCodePosition - 1])

        result = result + val*(10**parityPosition)

        print(result)

    return int(str(result), 2)


data = '1011001'

lengthData = len(data)

parityPositionsList = getParityBits(lengthData)

hammingCodeWithZeros = insertZeroToRedudantBits(data, parityPositionsList)

parity = "impar"

encoded = defineParityBits(hammingCodeWithZeros, parityPositionsList, parity)

print(encoded)

correct = '01110110001'
error = '01110110001'

detectError = detectError(error, parityPositionsList,"impar")

if(detectError==0):
    print("There is no error in the received message.")
else:
    print("The position of error is ", detectError,"from the left")