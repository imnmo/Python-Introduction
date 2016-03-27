q=[3,3,3,3,9,7,7,0]
count=0
for i in q:
    for j in q[1:]:
        if i == j:
            count=1
        print (count)
