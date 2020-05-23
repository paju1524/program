import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름":"정다운", "나이":"19", "취미":["자전거", "코딩", "노래 듣기"]}
print(profile)
pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
profile_file.close()

# import pickle
# profile_file = open("profile.pickle", "rb") as profile_file:
# profile = pickle.load(profile_file) # file 에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


 # print(pickle.load(profile))
