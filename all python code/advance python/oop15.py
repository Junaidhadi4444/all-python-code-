#...class method without parameter using class variable
class Mobile:
    f='yes'        # class variable or static variable 
    @classmethod   # decorator
    def show_model(cls):
        print('fingerprint',cls.f)

realmw=Mobile()
Mobile.show_model()