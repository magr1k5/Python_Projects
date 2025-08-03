import random
num = []
a = int(input("Введите количетсво цифр: "))
for i in range (a):
   num.append(random.randint(-150,150))
print(*num)
c = 0
for i in range (a):
   if ((num[i] % 2 == 0) and (num[i] > 0)):
       if (len(str(num[i])) == 2):
           c += 1
print ("Количество нужных цифр:  ", c)
