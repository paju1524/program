import time
import random

entries = []

with open("excel.xls") as f:
    for line in f:
        년도, 회차, 추첨일, 당첨번호 = line.split("\t")
        entries.append({
            "년도":년도,
            "회차":회차,
            "추첨일":추첨일,
            "당첨번호":당첨번호
        })

uniq_entries = []
used_names = set()    

for e in entries:
    if e["당첨번호"] not in used_names:
        used_names.add(e["당첨번호"])
        uniq_entries.append(e)

print(len(uniq_entries))

winners = random.new(uniq_entries, 5)
with open("winners.txt", "w+") as f2:
    for winner in winners:
        f2.write("%d\t%d\t%d\t%d" % (winner["년도"], winner["회차"], winner["추첨일"], winner["당첨번호"]))

for i, w in enumerate(winners):
    time.sleep(1)
    print("%d. %d, 추첨 번호 입니다!" % (i, w["년도"], w["회차"], w["추첨일"], w["당첨번호"],))
