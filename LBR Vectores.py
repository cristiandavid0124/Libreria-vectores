
# Cristian David Naranjo Orjuela
import math


def AdicionVectoresComplejos(a, b):
    sumavcomp = []
    if (len(a) != len(b)):
        return "No se puede hacer una adición con las dimensiones de los vectores distintos"
    else:
        for i in range(len(a)):
            sumavcomp.append(CNYT.Suma(a[i], b[i]))
        return sumavcomp


def RestaVectoresComplejos(a, b):
    restavcomp = []
    if (len(a) != len(b)):
        return "No se puede hacer una resta con las dimensiones de los vectores distintos"
    else:
        for i in range(len(a)):
            restavcomp.append(CNYT.Resta(a[i], b[i]))
        return restavcomp


def EscalarporVector(vector, escalar):
    res1 = []
    res = []
    for i in range(len(vector)):
        for j in range(len(vector[0])):
            res1.append(escalar * vector[i][j])
        res.append(res1)
        res1 = []
    return res


def AdicionMatricesComplejas(a, b):
    ans = []
    if (len(a) != len(b)):
        return "Las matrices no tienen las mismas dimensiones, por tanto no se pueden sumar"
    else:
        for i in range(len(a)):
            if (len(a[i]) != len(b[i])):
                return "Las dimensiones de los vectores no son iguales"
            else:
                ans.append(AdicionVectoresComplejos(a[i], b[i]))
        return ans


def inversaMatriz(a):
    ans = [0] * len(a)
    for i in range(len(a)):
        ans[i] = (a[i])
    return ans


def multiplicacionEscalarMatrices(matriz, escalar):
    res = []
    for i in range(len(matriz)):
        res.append(EscalarporVector(matriz[i], escalar))
    return res


def traspuesta(a):
    ans = []
    for i in range(len(a[0])):
        ans.append([])
        for j in range(len(a)):
            ans[i].append(a[j][i])
    return ans


def Conjugado(a):
    na = a[1] * -1
    return (a[0], na)


def conjugadamv(a):
    ans = [0] * len(a)
    for i in range(len(a)):
        ans[i] = Conjugado(a[i])
    return ans


def matrizAdjunta(matriz):
    return traspuesta(conjugadamv(matriz))


def productoMatrices(a, b):
    if (len(a[0]) != len(b)):
        return "Las dimensiones de las matrices no son correctas"
    else:
        ans = []
        for i in range(len(a)):
            fila = []
            for j in range(len(b[0])):
                temp = (0, 0)
                for k in range(len(b)):
                    mult = Producto(a[i][k], b[k][j])
                    temp = Suma(mult, temp)
                fila.append(temp)
            ans.append(fila)
        return ans


def accion(matriz, vector):
    if (len(matriz[0]) != len(vector)):
        return "No se puede realizar la acción porque el tamaño no es compatible"
    else:
        return productoMatrices(matriz, traspuesta(vector))


def productoInternoVectores(a, b):
    v1 = conjugadamv(a)
    return productoMatrices(v1, b)


def normaVector(a):
    norma = productoInternoVectores(a, a)
    return math.sqrt(norma[0])


def distanciaEntreVectores(a, b):
    resta = RestaVectoresComplejos(a, b)
    return normaVector(resta)


def esUnitaria(a):
    fil = []
    col = []
    adj = matrizAdjunta(a)
    res = productoMatrices(a, adj)
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i == j:
                fil.append(1)
            else:
                fil.append(0)
        col.append(fil)
        fil = []
    if res == col:
        return True
    else:
        return False


def esHermitiana(a):
    adjunta = matrizAdjunta(a)
    for i in range(len(a)):
        for j in range(len(a[0])):
            if (a[i][j] != adjunta[i][j]):
                return False
    return True


def productoTensor(m1, m2):
    tensor = []
    m = len(m1)
    mp = len(m1[0])
    n = len(m2)
    np = len(m2[0])
    t1, t2 = m * n, np * mp
    for i in range(t1):
        for j in range(t2):
            tensor[i][j] = m1[i // n][j // np] * m2[1 % n][1 % np]
    return tensor


if __name__ == '__main__':


