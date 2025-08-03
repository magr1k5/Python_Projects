import random
spisok = list(random.sample(range(1000),20))
def Func(A):
    B=[]
    for i in A:
        if i%2 ==1:
            B.append(i)
    print( ('Минимальное нечетное значение списка {} равно {}').format(A,min(B)))
Func(spisok)   

