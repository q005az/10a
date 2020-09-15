from math import*
print("Введите координаты точек A и B:")
x1y1,x2y2= map(float,input().split())
print(x1y1,x2y2)
print("Введите начала и концы(x1,x2,y1,y2) координат точек A  и B")
x1,x2,y1,y2= map(int,input().split())
AB= sqrt((x2-x1)**2-(y2-y2)**2)
print(AB)
