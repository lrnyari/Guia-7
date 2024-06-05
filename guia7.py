def es_vocal(letra: str) -> bool:
    return letra == 'a' or letra == 'A' or letra == 'e' or letra == 'E' or letra == 'i' or letra == 'I' or letra == 'o' or letra == 'O' or letra == 'u' or letra == 'U' 
#EJ1.1
#def pertenece(valor: int,lista: list[int]) -> bool:
#    res: bool = False
#    for i in lista:
 #       if i == valor:
  #          res = True
   # return res

def pertenece(valor: int, lista: list[int]) -> bool:
    for i in lista:
        if i == valor:
            return True
    return False


#def pertenece(valor: int,lista: list[int]) -> bool:
#    res: bool = False
#    indice: int = 0
#    longitud: int = len(lista)
#    while not res and indice < longitud:
#        if lista[indice] == valor:
#            res = True
#        else:
#            indice+=1
#    return res

#EJ1.2
def divide_a_todos(valor: int, lista: list[int]) -> bool:
    res = True
    for i in lista:
        if i % valor != 0:
            res = False
    return res

#EJ1.3
def suma_total(lista: list[int]) -> int:
    total: int = 0
    indice: int = 0
    longitud: int = len(lista)
    while indice<longitud:
        total = total + lista[indice]
        indice+=1
    return total

#EJ1.4
def ordenados(lista: list[int]) -> bool:
    res: bool = True
    indice: int = 0
    longitud: int = len(lista)
    while indice < longitud - 1 and res:
        if lista[indice] > lista[indice + 1]:
            res = False
        indice+=1
    return res

#EJ1.5
def long_mayor_7(lista: list[str]) -> bool:
    res = False
    palabra: str
    indice: int = 0
    longitud: int = len(lista)
    while indice < longitud and not res:
        palabra = lista[indice]
        if len(palabra) > 7:
            res = True
        indice+=1
    return res

#EJ 1.7
def es_num(letra: chr) -> bool:
    return letra >= '0' and letra <= '9'

def es_minus(letra: chr) -> bool:
    return letra >= 'a' and letra <= 'z'

def es_mayus(letra: chr):
    return letra >= 'A' and letra <= 'Z'

def condicion_verde(palabra: str) -> bool:
    cond_mayus: bool = False
    cond_minus: bool = False
    cond_num: bool = False
    longitud: int = len(palabra)
    indice: int = 0
    if longitud > 8:
        while indice < longitud and (not cond_mayus or not cond_minus or not cond_num):
            if es_num(palabra[indice]):
                cond_num = True
            if es_minus(palabra[indice]):
                cond_minus = True
            if es_mayus(palabra[indice]):
                cond_mayus = True
            indice+=1
    return cond_mayus and cond_minus and cond_num

def condicion_roja(palabra: str) -> bool:
    longitud: int = len(palabra)
    return longitud < 5

def fortaleza_contraseña(palabra: str) -> str:
    res: list[str] = ["VERDE","AMARILLO","ROJO"]
    if condicion_verde(palabra):
        return res[0]
    elif condicion_roja(palabra):
        return res[2]
    else:
        return res[1]    

#EJ 1.8
tuple
def saldo_actual(movimientos: list[(str, int)]) -> int:
    saldo: int = 0
    for i in range(len(movimientos)):
        operacion = movimientos[i]
        if(operacion[0] == 'I'):
            saldo = saldo + operacion[1]
        else:
            saldo = saldo - operacion[1]
    return saldo

movimientos_prueba = [("I", 2000), ("R", 20),("R", 1000),("I", 300)]
print(saldo_actual(movimientos_prueba))

#EJ 1.9

#

#EJ 2.1
def borrar_pares(lista: list[int]) -> list[int]:
    for i in range(len(lista)):
        if(lista[i] % 2 == 0):
            lista[i] = 0
    return lista
print(borrar_pares([1,2,3,4,5]))

#EJ 2.2

def borrar_pares_in(lista: list[int]) -> list[int]:
    lista_resultado: list[int] = []
    for i in range(len(lista)):
        if(lista[i] % 2 == 0):
            lista_resultado.append(0)
        else: 
            lista_resultado.append(lista[i])
    return lista_resultado

print(borrar_pares_in([1,2,3,4,5]))

#EJ 2.3

def sacar_vocales(texto: list[str]) -> list[str]:
    texto_resultado: list[str] = []
    for i in range(len(texto)):
        if(not es_vocal(texto[i])):
            texto_resultado.append(texto[i])
    return texto_resultado

print(sacar_vocales("siento por ciento"))

#EJ 2.4

def reemplaza_vocales(texto: list[str]) -> list[str]:
    texto_resultado: list[str] = []
    for i in range(len(texto)):
        if(es_vocal(texto[i])):
            texto_resultado.append(" ")
        else:
            texto_resultado.append(texto[i])
    return texto_resultado
            
print(reemplaza_vocales("ciento por ciento"))

#EJ 2.5

def dar_vuelta_str(texto: list[str]) -> list[str]:
    texto_resultado: list[str] = []
    for i in range(len(texto)):
        texto_resultado.append(texto[len(texto) - i - 1])
    return texto_resultado

#EJ 2.6

def sacar_repetidos(texto: list[str]) -> list[str]:
    texto_resultado: list[str] = []
    for i in range(len(texto)):
        if(not texto[i] in texto_resultado):
            texto_resultado.append(texto[i])
    return texto_resultado

print(sacar_repetidos("ciento por ciento"))

#EJ 3
def promedio_alumno(notas: list[int]) -> int:
    resultado: int = 0
    promedio: float
    total: int = 0
    for i in notas:
        total = total + i
    promedio = total / (len(notas) + 1)
    for i in notas:
        if(i<4 or promedio < 4):
            resultado = 3
    if(resultado != 3):
        if(promedio > 7):
            resultado = 1
        else:
            resultado = 2
    return resultado

print(promedio_alumno([5,6, 4, 3 ,6]))
print(promedio_alumno([10,10,10 , 10]))

#EJ 4.1

def construir_estudiantes() -> list[str]:
    resultado: list[str] = []
    nombre: str = input('Ingrese nombre del estudiante. Para terminar, ingrese listo:\n')
    while(nombre != "listo"):
        resultado.append(nombre)
        nombre = input('Ingrese nombre del estudiante. Para terminar, ingrese listo:\n')
    return resultado

#estudiantes_prueba = construir_estudiantes()
#print(estudiantes_prueba)

#EJ 4.2
def historial_monedero() -> list[(str, int)]:
    operacion: str = input('Qué operación desea realizar? Para terminar ingrese X:\n')
    monto: int
    historial: list[(str, int)] = []
    while(operacion != 'X'):
        monto = input('Ingrese el monto:\n')
        historial.append((operacion, monto))
        operacion: str = input('Qué operación desea realizar? Para terminar ingrese X:\n')
    return historial


# EJ 5.1

def pertenece_a_cada_uno_v1(lista: list[list[int]], valor: int) -> list[bool]:
    resultado: list[bool] = []
    
    for i in range(len(lista)):
        if(valor in lista[i]):
            resultado.append(True)
        else:
            resultado.append(False)
    
    return resultado

prueba_ej5: list[list[int]] = [[1,2,3],[6,3,4],[2,4]]
print(pertenece_a_cada_uno_v1(prueba_ej5,2))
    
#prueba: list[int] = [1,2,3,4]
#prueba_str: list[str] = ["cinco","cincose","tres"]
prueba_pass: str = 'contrasenia'

#print(suma_total(prueba))
#print(pertenece(0, prueba))
#print(divide_a_todos(1, prueba))
#print(ordenados(prueba))
#print(long_mayor_7(prueba_str))
print(fortaleza_contraseña(prueba_pass))

range(1,10,2)