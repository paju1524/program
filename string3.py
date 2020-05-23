#print("a" + "b")
#print("a", "b")

# 방법 1 (%를 사용하여서 할때)
print("나는 %d 살입니다." % 19) # %d 는 숫자일때 사용
print("나는 %s 을 좋아해요" % "python") # %s 는 문자열일때 사용
print("Apple 은 %c 로 시작해요." % "A")

print("나는 %s 살입니다." % 19) # %s 는 숫자도 출력이 가능하다
print("나는 %s색과 %s색을 좋아해요." % ("gold", "gray")) 

# 방법 2 (중괄호를 사용하여서 할때)
print("나는 {}살입니다." .format(19))
print("나는 {}색과 {}색을 좋아해요." .format ("gold", "gray"))
print("나는 {0}색과 {1}색을 좋아해요." .format ("gold", "gray"))
print("나는 {1}색과 {0}색을 좋아해요." .format ("gold", "gray"))

# 방법 3
print("나는 {age}살이고, {color}색을 좋아해요." .format(age = 19, color = "gold" ))
# 앞뒤를 변경해서 할수도 있다

# 방법 4 (v3.6 이상)
age = 19
color = "gray"
print(f"나는 {age}살이고, {color}색을 좋아해요.") 
# f로 문장을 시작한다 그러면 뒤에 .format 을 쓰지 않아도 된다.