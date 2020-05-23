# 집합 (set)
# 중복 x, 순서 x
my_set = {1,2,3,1,1}
print(my_set)

java = {"쟈스민", "장미", "민들레"}
python = set(["쟈스민", "라벤더"])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집함 (java 할 수 있거나 python 을 할수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python 을 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 을 할 줄 아는 사람이 늘어남
python.add("해바라기")
print(python)

# java 를 잊어버림
java.remove("장미")