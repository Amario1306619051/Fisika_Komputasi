from distutils.log import debug


def fungsiBray(x):
    return 5*x*x

deltaX = 0.00000001
point = 3

F = (fungsiBray(point + deltaX) - fungsiBray(3))/deltaX
print('Hasil turunan pada titik {point} adalah', F)



#print('{0:^20} | {1:^20}'.format('aku', 'muhlis'))