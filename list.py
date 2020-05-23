# list []

# 지하철 칸별로 10, 20, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["정다운", "정유로", "정유진"]
print(subway)

# 정유로가 몇번째 칸에 타고 있는가?
print(subway.index("정유로"))

# 엄마빠가 다음정류장에서 다음 칸에 탐
subway.append("엄마빠")
print(subway)

# 할머니를 정유진 / 엄마빠 사이에 태워드림
subway.insert(3, "할머니")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("정다운")
print(subway)
print(subway.count("정다운"))

# 정렬도 가능
num_list = [1,5,2,4,3,0]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [3,4,2,0,1,5]
mix_list = ["정다운", 20, True]
print(mix_list, num_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)