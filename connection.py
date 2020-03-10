import serial

class Connection:

    def __init__(self, port, baudrate, timeout):
        self.serial = serial.Serial(port, baudrate, timeout=timeout)
        #print ('asd')

    def sendData(self, data):
        #print (data)
        self.serial.write(str.encode(data))

    def readData (self):
        string = self.serial.read()
        string = string.decode()
        return string
