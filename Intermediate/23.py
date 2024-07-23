# create the fibonacci series

def suma_fibo(num):
    a,b = 0,1
    serie = [0]
    for i in range(num): # defined characters
        if b > num: return serie
        else:
            serie.append(b)
            a,b = b,b+a
    return serie

res = suma_fibo(34)
print(res)
