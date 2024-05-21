def imprimir_hola_mundo() -> None:
    hola_mundo: str = "Hola mundo!"
    print(hola_mundo)


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







#prueba: list[int] = [1,2,3,4]
#prueba_str: list[str] = ["cinco","cincose","tres"]
prueba_pass: str = 'contrasenia'

#print(suma_total(prueba))
#print(pertenece(0, prueba))
#print(divide_a_todos(1, prueba))
#print(ordenados(prueba))
#print(long_mayor_7(prueba_str))
print(fortaleza_contraseña(prueba_pass))