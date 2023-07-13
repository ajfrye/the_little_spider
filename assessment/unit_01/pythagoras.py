class Triangle:
    def __init__(self, leg1, leg2):
        self.leg1 = leg1
        self.leg2 = leg2
    
    def get_hypotenuse(self):
        c = ( self.leg1**2 + self.leg2**2 )**0.5
        return c
    
    def get_leg1(self): 
       return self.leg1 
    
    def get_leg2(self):
        return self.leg2

