#....class variable or static varibale
class Mobile:
    fp='yes'      #class variable
    @classmethod
    def is_fp(cls):
        cls.fp
        print(cls.fp)    #access class variable
realme=Mobile()
Mobile.is_fp()            

