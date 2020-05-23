gun = 1000

def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("in function : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("in function : {0}".format(gun))
    return gun

print("total gun : {0}".format(gun))
# checkpoint(100) # 100명이 경계 근무 나감
gun = checkpoint_ret(gun, 100)
print("remaining gun : {0}".format(gun))