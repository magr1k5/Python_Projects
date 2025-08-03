import random as r

def function(n, m):

   matrix = [[r.randint(0, 100) for x in range(n)] for y in range(m)]

   max_sum = []

   for q in matrix:

       max_sum.append(sum(q))

       print("{} -- {}".format(q, sum(q)))

   id_max_el = max_sum.index(max(max_sum))

   print(

       "\nСтрока матрицы сумма элементов в которой максимальна: {}".format(

           matrix[id_max_el]))

z = int(input("Сколька столбцов?: "))

c = int(input("Сколька строк?: "))

function(z, c)
