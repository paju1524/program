# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#    print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("정다운", 19, "python", "js", "css", "html", "c", ".*txt")
profile("김솔이", 20, "Kotlin", "swift")