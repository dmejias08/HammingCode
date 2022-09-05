
def octalToDecimal(number):
    decimalValue = 0
    base = 0
    temporalNumber = number

    while (temporalNumber):
        lastDigit = temporalNumber % 10
        temporalNumber = int(temporalNumber / 10)
        decimalValue += lastDigit * (8**base)
        base += 1
 
    return decimalValue

def octolToBinaryOrHexa(number, binaryOrHexa):
    resultValue = ""
    temporalNumber = octalToDecimal(number)
    dicForHexa = {
        10 : "A",
        11 : "B",
        12 : "C",
        13 : "D",
        14 : "E",
        15 : "F"
    }
    while (temporalNumber > 0):
        coeficient = temporalNumber // binaryOrHexa
        remainder = temporalNumber % binaryOrHexa
        if remainder >= 10:
            resultValue = dicForHexa.get(remainder) + resultValue
        else:
            resultValue = str(remainder) + resultValue
        temporalNumber = coeficient
    return resultValue

def decimalToBinary(ip_val, string=""):
    if ip_val >= 1:
        string = str(ip_val % 2)+string
        return decimalToBinary(ip_val // 2, string)
    return string


        
