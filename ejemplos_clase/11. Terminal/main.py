import sys


if __name__ == "__main__":
    
    # Desde la terminal mandaré la clave del alumno
    # y una opción. Si es 1 sacaré la nota media
    # Y si es 2, sacaré la nota máxima
    # Si la clave no es válida, lo diré en un print
    
    # Esto guarda en una lista todo lo que haya a la derecha
    # de python cuando ejecuto desde la terminal
    argumentos = sys.argv 
    print("La lista de argumentos es: ", argumentos)
    op = int(argumentos[1])
    clave = argumentos[2]
    
    
    alumnos = {"2016":[5,4,5], "2018":[4,3,5], "2019":[4,3,4]}
    if clave not in alumnos: 
        print("La clave no es válida")
    else:
        notas = alumnos[clave]
        if op == 1:
            print(sum(notas) / len(notas))
        elif op == 2:
            print(max(notas))
        
    
   
    
    