def folder(x): 
    import os
    a=int(input("Введите работы с каталогом цифру от 1 до 3: "))
    if a == 1:
        os.mkdir("NEW")
        print("Каталог создан")
    elif a ==2:
        print(os.getcwd())
        print("Ниже выдан список файлов в данном каталоге: ")
        print(os.listdir("NEW"))
    elif a == 3:
        print(os.name)
    else:
        print("Такая команда не определена: ")
folder(1)
