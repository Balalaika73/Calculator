numb = int(input("Введите количество чисел для операции: "))
op=0
for i in range(numb):
    num = int(input("Введите число: "))
    while (num == 0) and (op == 3):
        num = int(input("Введите число: "))
    if op !=0:
        if op == 1:
            res = prev + num
        elif op == 2:
            res = prev - num
        elif op == 3:
            res = prev / num
        elif op == 4:
            res = prev * num
    else: 
        res=num
    prev=res
    print("Результат: ", res)
    if i!=numb-1:
        op = int(input("Выберите операцию: \n1. +\n2. -\n3. /\n4. *\n"))
        while op not in range(1,4):
            op = int(input("Выберите операцию: \n1. +\n2. -\n3. /\n4. *\n"))
print("Результат: ", res)