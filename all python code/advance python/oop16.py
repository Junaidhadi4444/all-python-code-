#...class method with parameter using class variable
class Mobile:
    f='yes'        # class variable or static variable 
    @classmethod   # decorator
    def show_model(cls, a):
        cls.ram=a
        print('fingerprint',cls.f)
        print('RAM',cls.ram)

realmw=Mobile()
Mobile.show_model('4GB')