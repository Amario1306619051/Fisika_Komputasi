def f(x):
    return x*x + 2*x

deltaX = 0.001
point = 3

F = (f(point + deltaX) - f(point))/deltaX
print('Hasil turunan pada titik {point} adalah', F)

print('{0:^20} | {1:^20}'.format('aku', 'muhlis'))