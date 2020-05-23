# score_file = open("score.txt", "w", encoding="utf8")
# print("코딩 : 100", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n수학 : 10")
score_file.close()