import math
def line():
    A = float(input('Ingrese el coeficiente A: '))
    B = float(input('Ingrese el coeficiente B: '))
    X1 = float(input('Ingrese el coeficiente X1:'))
    X2 = float(input('Ingrese el coeficiente X2: '))
    print('El coeficiente A de su ecuación de la recta es:',float(A))
    print('El coeficiente B de su ecuación de la recta es:',float(B))
    print('El coeficiente X1 de su ecuación de la recta es:',float(X1))
    print('El coeficiente X2 de su ecuación de la recta es:',float(X2))
    print('')
    print( f'''Para la siguiente ecuación:\n\tY = {A}X + {float(B)}''')
    print(f'''\nDados los siguientes puntos:\n\tP1 ({float(X1)}, {float(A*X1+B)})\n\tP2 ({float(X2)}, {float(A*X2+B)})''')
    
    p = [float(X1),float(A*X1+B)]
    q = [float(X2),float(A*X2+B)]
    print(f'\nLa distancia entre ellos es: {math.dist(p,q)}')
