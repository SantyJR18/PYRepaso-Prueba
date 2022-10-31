import Estructura 
listaEst = []
notas = []

def agregarEstudiante(id, nom, ape, car, notas):
    est = Estructura.Estudiante(id, nom, ape, car, notas)
    listaEst.append(est)

def agregarAsig(mat, calif):
    nota = Estructura.Nota(mat, calif)
    notas.append(nota)

def calcPromedio(notas):
    suma = 0
    for nota in notas:
        suma += nota.calificacion
    promedio = suma / len(notas)
    return promedio

def calcPrimerosLugares():
    i = 0
    while i < len(listaEst):
        j = i+1
        while j < len(listaEst):
            est1 = listaEst[i]
            est2 = listaEst[j]
            prom1 = calcPromedio(est1.Notas)
            prom2 = calcPromedio(est2.Notas)
            if(prom2 > prom1):
                aux = listaEst[i]
                listaEst[i] = listaEst[j]
                listaEst[j] = aux
            j+=1
        i+=1
    return listaEst[0], listaEst[1], listaEst[2]

 
