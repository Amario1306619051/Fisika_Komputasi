def Amar(x):
    return x*x + 2*x

deltaX = 0.5
point = 3

F = (Amar(point) - Amar(point - deltaX))/deltaX
print(F)