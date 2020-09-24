print("Введите 3 числа")
a,b,c= map(int,input().split())
if a==b==c:
    print('Все числа равны')
else:
    if a==b or a==c or b==c :
        print('Два числа равны')
    else:
        print("Ниче не равно,вводи нормальные числа")
        
