python = "Python is Amazing"
print(python.lower()) # 소문자로 변경
print(python.upper()) # 대문자로 변경
print(python[0].isupper()) #대괄호 안의 값만 대문자로 변결할때
print(len(python)) # 길이를 나타낼때
print(python.replace("Python", "Java")) 
# python 에서 Java 로 바꿀때 replace 를 사용

index = python.index("n") # 5위치에 있는것을 반환
print(index)
index = python.index("n", index + 1) # 5위치를 지나 6부터 뒤에있는 n 을 찾을때
print(index)

print(python.find("n")) # 소괄호 안의 값을 찾을때

print(python.find("Java")) # 위의 변수 python 에 Java 라는 함수가 없어서 -1으로 반환
# print(python.index("Java")) 이것은 오류가 난다. 변수에 이값이 없기 때문에
print('hi')

print(python.count("n")) # 변수 python 에서 n 이 몇번이나 쓰였는지 보여 줄때