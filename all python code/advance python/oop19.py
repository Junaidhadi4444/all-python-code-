#....passing member of one class to anther class...
#...real using of static method
class Student:
    # constructor
    def __init__(self, n, r):
        self.name=n
        self.roll=r

    #instance method
    def disp(self):
        print('student name:',self.name)
        print('student roll:',self.roll)

class User:
    # static method
    @staticmethod
    def show(s):
        print('user name:',s.name)
        print('user roll:',s.roll)
        s.disp()
# creating object of the student class
stu = Student('fawad', 10)
User.show(stu)