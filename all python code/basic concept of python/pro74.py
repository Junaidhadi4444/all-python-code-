#....function return another funaction.....
def disp():
    def show():
        return "dhow function"
    print('disp function')
    return show
r_sh=disp()
print(r_sh())
