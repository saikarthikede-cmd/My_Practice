def even_nos(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
def odd_nos(n):
    for j in range(n):
        if j%2!=0:
            yield j
print(list(even_nos(10)))
print(list(odd_nos(10)))
    
