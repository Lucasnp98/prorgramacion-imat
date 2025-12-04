import sys

palabra_ganadora = "LUCAS"
if __name__ == "__main__":

    argumentos = sys.argv
    if len(argumentos) == 2 and argumentos[1] == "1":
        print("La palabra a adivinar es: ", palabra_ganadora)
    else:
        print("No vas a saber la palabra a adivinar...")
