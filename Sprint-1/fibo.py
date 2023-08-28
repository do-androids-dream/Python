def fibo(n):
    if n < 0: return -1
    if n == 0: return 0
    if n== 1: return 1
    
    return (fibo(n-1) + fibo(n-2))
        
#print(fibo(7))

def fibo_seq(n):
    a, b = 1, 1
    count = 0
    while count < n:
        count += 1
        print(b, end=" ")
        a, b = b, a + b

fibo_seq(7)