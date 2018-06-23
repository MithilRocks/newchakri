class Camrilla:
    
    def __init__(self, high, low, close):
        self.high = high 
        self.low = low
        self.close = close 

    def r5(self):
        return ( self.high  /  self.low * self.close )
    
    def r4(self):
        return ( ( self.high / self.low + 0.83) / 1.83 * self.close )

    def r3(self):
        return ( ( self.high / self.low + 2.66 ) / 3.66 * self.close )

    def r2(self):
        return ( ( self.high / self.low + 4.5 ) / 5.5 * self.close )

    def r1(self):
        return ( ( self.high / self.low + 10 ) / 11 * self.close )

    def s1(self):
        return -(((self.high / self.low + 10) / 11) - 2) * self.close

    def s2(self):
        return -(((self.high / self.low + 4.5) / 5.5) - 2) * self.close

    def s3(self):
        return -(((self.high / self.low + 2.66) / 3.66) - 2) * self.close

    def s4(self):
        return -(((self.high / self.low + 0.83) / 1.83) - 2) * self.close

    def s5(self):
        return -(self.high / self.low - 2) * self.close
