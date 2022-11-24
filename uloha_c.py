pocet_ludi = int(input())
ludia=[]
are_repeaing = []

if pocet_ludi < 1 or pocet_ludi > 1000: raise ValueError("Can't be more then 1000, and less then 0")

for _ in range(pocet_ludi):
    sutaziaci = input()
    namesa, point = sutaziaci.split(" ")
    are_repeaing.append(point)
    ludia.append(namesa+" "+point)

are_repeaing.sort(reverse=True)
ludia.sort(key=str.lower)
s = sorted(ludia, key=lambda x: int(x.split(" ")[1]), reverse=True)

place = 1
repeating = 0
for x in s:
    name, points = x.split()
    if int(points) == are_repeaing[0]:
        print(f"{place}. {x}")
        are_repeaing.remove(points)
        repeating+=1
    else:
        print(f"{place}. {x}")
        place+=1+repeating