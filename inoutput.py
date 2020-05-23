# import sys
# print("python", "Java", file=sys.stdout)
# print("python", "Java", file=sys.stderr)
# print("python", "Java", sep=" vs ", end="? ")
# print("무엇이 더 쉬울까요?")

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(4), str(score).rjust(4), sep=":")

# 은행 대기순변표
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(2))

answer = input(" 아무말 대찬치 : ")
print(type(answer))
print("입력한 값은 " + answer + "입니다.")