# __del__ method

class ABC:
    def __init__(self,mahi):
        self.mahi=mahi
    def __del__(self):
        print('object with value%d deleted'%(self.mahi))
s1=ABC(70)
s2=ABC(80)
del s1
del s2
