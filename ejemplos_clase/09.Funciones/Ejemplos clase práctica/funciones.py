def pedir_notas(num:int)-> list:
    notas = []
    for i in range(num):
        nota = pedir_validar_nota()
        notas.append(nota)
    return notas


def mostrar_menu() -> None:
    menu  = """
    1. Llenar la lista de las notas
    2. Calcular la nota maxima
    3. Calcular la media de la clase
    4. Salir"""
    print(menu)
    
##### Programar una funcion que pida y valide, para evitar DRY. 
            
def pedir_validar_nota()-> float:
    nota = float(input("Introduce una nota: "))
    while nota < 0 or nota > 10:
        nota = float(input("Introduce una nota: "))
    return nota

def calcula_maximo(lista:list) -> float:
    maximo = 0
    for nota in lista:
        if nota > maximo:
            maximo = nota
    return maximo

def pedir_validar_op():
    op = int(input("Introduce una op: "))
    while op < 1 or op > 4:
        op = int(input("Introduce una op: "))
    return op

def calcula_media(notas:list)-> float:
    suma = 0
    for nota in notas:
        suma += nota
    media = suma / len(notas)
    return media    