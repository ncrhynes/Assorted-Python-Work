def intDiv(m, n):
    if m < n:
        return 0
    else:
        return intDiv(m - n, n) + 1
       
def intDivL(m, n):
    c = 0
    while m >= n:
        m -= n
        c += 1
    return c
        
for i in range(1, 102):
    print(i, ":", intDivL(100, i))
      
