import Funciones as fun

fun.agregarAsig("Español", 20)
fun.agregarAsig("Mat", 90)

fun.agregarEstudiante(1, "Santiago", "manzanares", "ISI", fun.notas)

for est in fun.listaEst:
    print(est.Nombres)
    print(est.Apellidos)
    print(est.Carrera)
for nota in est.Notas:
    print(nota.Materia)
    print(nota.Calificacion)