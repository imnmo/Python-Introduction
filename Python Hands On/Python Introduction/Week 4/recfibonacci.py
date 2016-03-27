def fibonacci(m):
    if m < 1:
        return m
    else:
        return abs(fibonacci(m-2)+fibonacci(m-1))
