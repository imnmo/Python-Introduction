a = [4, 1, 3, 2, 1, 2, 2, 3, 3, 3]


n = a.count(1)
m = a.count(2)
o = a.count(3)
p = a.count(4)


points = {}
points[1] = n
points[2]=m
points[3] = o
points[4]=p
SORTED_TUPLE = tuple(sorted(points.items(), key=lambda item: item[1],reverse=True))
print(points)

print (points.items())
print (SORTED_TUPLE)



