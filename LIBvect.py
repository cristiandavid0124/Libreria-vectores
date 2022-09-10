import math
#Cristian Naranjo
#Funciones de respaldo
#.Suma complejos representados como una tupla (real, imaginaria)
def sumacplx(a, b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    if img >= 0:
        return str(real) + "+" + str(img) + "i"
    else:
       return str(real) + str(img) + "i"

#producto
def multicplx(a, b):
    real = (a[0] * b[0])-(a[1] * b[1])
    img = (a[0] * b[1])+(a[1] * b[0])
    if img >= 0:
        return str(real) + "+" + str(img) + "i"
    else:
        return str(real) + str(img) + "i"

# resta complejos representados como una tupla
def restcplx(a, b):
    real = a[0] - b[0]
    img = a[1] - b[1]
    if img >= 0:
        return str(real) + "+" + str(img) + "i"
    else:
        return str(real) + str(img) + "i"




#calcula el conjugado de complejos representados como una tupla
def conjugado(a):
    real = a.real
    imag = -1 * a.imag
    if imag == 0:
        imag = 0
    if imag < 0:
        num = str(real) + str(imag) + 'j'
    else:
        num = str(real) + '+' + str(imag) + 'j'
    return complex(num)


# Libreria de matrizes

#1 Adición de vectores complejos.
def sumVect(a,b):
    result =[]
    for i in range (len(a)):
        sum1 = sumacplx(a[i], b[i])
        result += [sum1]
    return result

#2 Inverso  de un vector complejo.
def inverVect(a,b):
    list =[]
    for i in range (len(a)):
        inver = restcplx(a[i],b[i])
        list += [inver]
    return list

#3 Multiplicación de un escalar por un vector complejo.
def ScalarVectormulti (a, b):
    list = [[b*a[i][j]for j in range(len(a))]for i in range(len(a))]
    return list

#4 Adición de matrices complejas.
def sumMatrixCplx(m1,m2):
    if len(m1) == len(m2) and len(m1[0])== len(m2[0]):
        m3 =[]
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[i][j]+m2[i][j])
        return m3
    else:
        return "no se puede hacer la opercacion"

#5 Inversa (aditiva) de una matriz compleja.
def inverMatrixCplx(m1,m2):
    if len(m1) == len(m2) and len(m1[0])== len(m2[0]):
        m3 =[]
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[i][j]-m2[i][j])
        return m3
    else:
        return "no se puede hacer la operacion"

#6 Multiplicación de un escalar por una matriz compleja.
def multiScalarMatrixCplx(a,v):
    v = [[a * v[i][j] for j in range(len(v[0]))] for i in range(len(v))]
    return v[:]

#7 Transpuesta de una matriz/vector
def transpose(v):
    if len(v[0]):
        list = []
        for i in range(len(v[0])):
            list.append([])
            for j in range(len(v)):
                list[i].append(v[j][i])
        return list
    else:
        list = [[v[j] for i in range(len(v[0]))] for j in range(len(v))]
    return list

#8 Conjugada de una matriz/vector
def conjMatrixVector(m):
    fila = [(0,0)] * len(m[0])
    conjugate = [fila] * len(m)
    for i in range(len(m)):
        conjugate[i] = fila
        for j in range(len(m[0])):
            conjugate[i][j] = conjugado(m[j][i])
    return conjugate

#9 Adjunta (daga) de una matriz/vector
def Adjunt(m1):
    return transpose(conjMatrixVector(m1))

#10 Producto de dos matrices
def matrixProduct(v,w):
    if len(v[0]) == len(w):
        list = [[0 for i in range(len(v))] for j in range(len(w[0]))]
        for i in range(len(v)):
            for j in range(len(w[0])):
                for k in range(len(v[0])):
                    list[i][j] += v[i][k] * w[k][j]
        return list
    else:
        return None

#11 Función para calcular la "acción" de una matriz sobre un vector.
def action(m,v):
    list = [0 for i in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            list[i] += m[i][j]*v[j]
    return list

#12 Producto interno de dos vectores
def innerProduct(v,w):
    productEscalar = 0
    for i in range(len(v)):
        productEscalar += v[i]*w[i]
    return productEscalar

#13. Norma de un vector
def normVector (v):
    j = []
    for i in range(len(v)):
        j.append(v[i]**2)
        norm = math.sqrt(sum(j))
    return norm

#14 Distancia entre dos vectores
def distanceVectors(v1,v2):
    distance = math.sqrt((v1[0]-v2[0])**2+(v1[1]-v2[1])**2)
    return distance

#15 Revisar si una matriz es unitaria
def unitMatrix(m):
    list = [[(1 if j == k else 0) for k in range(len(m))]for j in range(len(m))]
    m = matrixProduct(m,conjMatrixVector(transpose(m[:])))
    if m == list:
        return True
    else:
        return False

#16 Revisar si una matriz es Hermitiana
def matrixHermitian(m):
    m1 = conjMatrixVector(transpose(m[:]))
    if m1 == m:
        return True
    else:
        return False

#17 Producto tensor de dos matrices/vectores
def tensorProduct(v,w):
    tensor = []
    for i in range(len(v)*len(w)):
        tensor.append([])
        for j in range(len(v[0])*len(w[0])):
            tensor[i].append(0)

    for i in range(len(tensor)):
        for j in range(len(tensor[i])):
            tensor[i][j]= multicplx(v[i//len(w)][j//len(w[0])], w[i%len(w)][j%len(w[0])])


if __name__ == '__main__':

    v = [2, 3], [4, 7]
    w = [1, 3], [2, 7]
    h = [4, 7]
    c1 = [(4,2),(3,4)]
    c2 = [(1,2),(3,4)]
    h1= [[(1,2), (1,2)],[(3,4), (3,7)]]
    #pruebas
    print(sumVect(v,w))
    print(inverVect(v,w))
    print(ScalarVectormulti (v,2))
    print(sumMatrixCplx(c1,c2))
    print(inverMatrixCplx(c1, c2))
    print(multiScalarMatrixCplx(2, h1))
    print(transpose(c1))
    print(conjMatrixVector(c1))
    print(Adjunt(c1))
    print(matrixProduct(c1,c2))
    print(action(c2, h))
    print(innerProduct(h, h))
    print(normVector(h))
    print(distanceVectors(h,h))
    print(unitMatrix(c1))
    print(matrixHermitian(c1))
    #print(tensorProduct(c1,c2))