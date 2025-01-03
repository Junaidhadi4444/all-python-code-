#.....nested function.......
def disp():
    def show():
        print("show fuction")
    print('disp function')
    show()
disp()