def line():
    A = float(input('Ingrese el coeficiente A: '))
    B = float(input('Ingrese el coeficiente B: '))
    X1 = float(input('Ingrese el coeficiente X1:'))
    X2 = float(input('Ingrese el coeficiente X2: '))
    print('El coeficiente A de su ecuación de la recta es: ',float(A))
    print('El coeficiente B de su ecuación de la recta es: ',float(B))
    print('El coeficiente X1 de su ecuación de la recta es: ',float(X1))
    print('El coeficiente X2 de su ecuación de la recta es: ',float(X2))
    print(f'''Para la siguiente ecuación
       Y = {A}x+{float(B)}
     ''')
    print(f'''Dados los siguientes puntos:
        P1 ({float(X1)},{float(A*X1+B)}) 
        P2 ({float(X2)},{float(A*X2+B)})
        ''')
    
    p = [float(X1),float(A*X1+B)]
    q = [float(X2),float(A*X2+B)]
    print(math.dist(p, q))
