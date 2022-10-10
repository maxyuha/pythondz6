from itertools import count


song = input().split()
set1 = set()
for i in song:
    count = 0
    list1 = [1 for j in i if j.lower() in 'ауиоыэяюёие']
    set1.add(len(list1))

    for j in i:
        if j.lower() in 'ауиоыэяюёие':
            count += 1
    set1.add(count)
if len(set1) == 1:
    print('парам пам-пам')
else:
    print('пам парам')
