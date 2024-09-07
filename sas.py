n = 9
scores = [10 ,5 ,20 ,20, 4, 5, 2, 25, 1]

count_min =0
count_max = 0
minn = scores[0]
maxx = scores[0]
print(minn,maxx)
for i in range(1, len(scores)):
    print(scores[i])# correct
    if scores[i]>minn:
        maxx = scores[i]
        count_max+=1
    elif scores[i]<minn:
        minn = scores[i]
        count_min+=1
    elif scores[i]==minn:
        count_min=count_min
    elif scores[i] == maxx:
        count_max =count_max
print([count_max, count_min])

# 2,4

# 10
# 3 4 21 36 10 28 35 5 24 42
# 4 0