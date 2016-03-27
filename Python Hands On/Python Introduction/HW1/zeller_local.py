def zeller(day, month, year):
  
    m = month
    q = day
    if (q == 1 ):
         q = 13
    else:
          if (q == 2):
              q = 14
    year = year -1
    i = str(year)
    j = i[0]+i[1]
    k = i[2]+i[3]
    J = int(j)
    K = int(k)
    a = int((m+1)*26 /10)
    b = int((K/4) + (J/4))
    
    
    h = (q + a + K + b - 2*J)%7
    
    return h 
