from algorithms import *
from cells_and_files import *

def main():
    while True:
        print("Selecciona un algoritmo")
        print("1. Mejor ajuste")
        print("2. Primer ajuste")
        print("3. Peor ajuste")
        print("4. Salir")
        opc = input(">>>")
        memory = [ Cell(n+1) for n in range(12) ]
        files = [ File(n+1) for n in range(32) ]
        if opc == "1":
            best_fit(memory, files)
        elif opc == "2":
            first_fit(memory, files)
        elif opc == "3":
            worst_fit(memory, files)
        elif opc == "4":
            break

if __name__ == "__main__":
    main()