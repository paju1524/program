def profile(name, age, main_sub):
    print("이름 : {0}\t나이 : {1}\t주 과목 :{2}"\
        .format(name, age, main_sub))

profile("정다운", 20, "물리")
profile("김솔이", 20, "생명")

# 같은 학교 같은 반 같은 학년 같은 수업.#

def profile(name, age=19, main_lang="화학"):
    print("이름 : {0}\t나이 : {1}\t주 과목 :{2}"\
        .format(name, age, main_lang))

profile("정다운")
profile("김솔이")