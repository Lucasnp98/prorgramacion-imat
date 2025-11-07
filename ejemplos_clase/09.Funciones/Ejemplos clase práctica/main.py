import funciones as f
if __name__ == "__main__":
    
    num_alu = 3
    
    op = 0
    while op != 4:
        f.mostrar_menu()
        op = f.pedir_validar_op()
        if op == 1:
            lista_notas = f.pedir_notas(num_alu)
        elif op == 2:
            nota_max = f.calcula_maximo(lista_notas)
            print("La nota maxima es: ", nota_max)
        elif op == 3:
            nota_media = f.calcula_media(lista_notas)
            print("La nota media es: ", nota_media)
            
            
    print("Programa terminado!")
            
            
        
            
    
        
    
    