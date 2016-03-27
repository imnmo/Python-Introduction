def per(v):
    t = sum(v)
    def av(v):
        return v/t
    
    return map(p,v)

x=per([1,2,3])
print(x)
