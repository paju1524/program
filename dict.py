cabinet = {3:"정다운", 100:"정로진"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))

# print(cabinet[5]) 아래의 "hi 갑을 출력하지 않고 종료"
print(cabinet.get(5)) # 반대로 none 라는 값을 추력하고 "hi"도 출력한다
print(cabinet.get(5, "사용 가능"))
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-1":"정다운", "B-2":"정유로"}
print(cabinet["A-1"])
print(cabinet["B-2"])

# 새 손님
print(cabinet)
cabinet["C-3"] = "정유진"
cabinet["D-4"] = "엄마빠"
print(cabinet)

# 간 손님 
del cabinet["C-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 마카롱 폐점
cabinet.clear()
print(cabinet)