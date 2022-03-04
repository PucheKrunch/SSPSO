from algorithms import *
from cells_and_files import *

def main():
    while True:
        print("Select an algorithm:")
        print("1. Best fit")
        print("2. First fit")
        print("3. Worst fit")
        print("4. Exit")
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