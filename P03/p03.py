import json

data = open('json_files/Jalisco.json', 'r')

data_json = json.load(data)
data.close()

def copy(file, state):
    try:
        file_data = open(f"out_files/{file}", 'r+')
        file_data_json = json.load(file_data)
        file_data.seek(0)
        file_data.truncate()
        state_data = open(f"json_files/{state}", 'r')
        state_data_json = json.load(state_data)
        state_name = state.split('.')[0]
        file_data_json[state_name] = state_data_json
        file_data.write(json.dumps(file_data_json, indent=4))
    except:
        file_data = open(f"out_files/{file}", 'w')
        state_data = open(f"json_files/{state}", 'r')
        state_data_json = json.load(state_data)
        state_name = state.split('.')[0]
        file_data.write(json.dumps({state_name:state_data_json}, indent=4))
    file_data.close()
    state_data.close()


def main():
    while(True):
        command = input(">>> ")
        if command.split()[0] == 'copiar':
            copy(command.split()[1], command.split()[2])
            print("Copiado")
        elif command.split()[0] == 'salir':
            break
        else:
            print("Comando no reconocido")

if __name__ == "__main__":
    main()