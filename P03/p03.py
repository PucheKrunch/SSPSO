import json, os

data = open('json_files/Jalisco.json', 'r')

data_json = json.load(data)
data.close()

def copy(file, state):
    try:
        file_data = open(f"json_files/{file}", 'r+')
        file_data_json = json.load(file_data)
        file_data.seek(0)
        file_data.truncate()
        state_data = open(f"json_files/{state}", 'r')
        state_data_json = json.load(state_data)
        state_name = state.split('.')[0]
        file_data_json[state_name] = state_data_json
        file_data.write(json.dumps(file_data_json, indent=4))

    except:
        file_data = open(f"json_files/{file}", 'w')
        state_data = open(f"json_files/{state}", 'r')
        state_data_json = json.load(state_data)
        state_name = state.split('.')[0]
        file_data.write(json.dumps({state_name:state_data_json}, indent=4))

    file_data.close()
    state_data.close()

def delete(file, zipcode):
    try:
        file_data = open(f"json_files/{file}", 'r+')
        file_data_json = json.load(file_data)
        file_data.seek(0)
        file_data.truncate()
        del file_data_json[zipcode]
        file_data.write(json.dumps(file_data_json, indent=4))
        file_data.close()

    except:
        print("No se pudo eliminar, escribe el comando correctamente")

def rename(file, name):
    os.rename(f"json_files/{file}", f"json_files/{name}")

def main():
    while(True):
        command = input(">>> ")
        if command.split()[0] == 'copiar':
            copy(command.split()[1], command.split()[2])
            print("Copiado")

        elif command.split()[0] == 'eliminar':
            delete(command.split()[1], command.split()[2])
            print("Eliminado")

        elif command.split()[0] == 'renombrar':
            rename(command.split()[1], command.split()[2])
            print(f"Se cambió el nombre del archvio de '{command.split()[1]}' a '{command.split()[2]}'")

        elif command.split()[0] == 'salir':
            break

        else:
            print("Comando no reconocido")

if __name__ == "__main__":
    main()