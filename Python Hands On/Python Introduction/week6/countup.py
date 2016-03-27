src = [ 'one', 'two', 'three', 'two', 'three', 'three' ]
result_dict = dict( [ (i, src.count(i)) for i in set(src) ] )
print(result_dict)

