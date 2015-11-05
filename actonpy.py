import serial
class actonpy():
    def __init__(self, port='COM3'):
        self.ser = serial.Serial(port, 9600, timeout=1)
        if self.ser.isOpen(self):
            ret = query('MODEL')
            print('Spectrometer {} connected'.format(ret))
        else:
            print('Could not connect to serial port')

    def query(self, cmd):
        self.ser.write(cmd+'\r')
        ret = self.ser.readall()
        return ret[1:-6]

    def write(self, cmd):
        self.ser.write(cmd+'\r')

    def closeConnection(self):
        self.ser.close()
        print('connection closed')

    def get_wavelength(self):
        # return wavelength as float in nm
        ret = self.query('?NM')
        return float(ret[:-3])

    def get_scanrate(self):
        # return scan rate  as float in nm/min
        ret = self.query('?NM/MIN')
        return float(ret[:-7])

    def set_scanrate(self, rate):
        # set scan rate in nm/min
        # return new rate
        self.write('{:.2f} NM/MIN'.format(rate))
        if self.ser.readline().find('ok') != -1:
            ret = self.get_scanrate()
        else:
            ret = 'failed'
        return ret

    def goto(wavelength):
        self.write('{:.3f} GOTO'.format(wavelength))
        if self.ser.readline().find('ok') != -1:
            ret = self.get_wavelength()
        else:
            ret = 'failed'
        return ret

    def get_info():
        self.ser.write('MONO-EESTATUS\r')
        ret = self.ser.readall()
        print(ret)
