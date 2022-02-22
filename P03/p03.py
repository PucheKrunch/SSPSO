import json, os, shutil
from collections import OrderedDict

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

def combine(file1, file2):
    file1_data =  open(f"json_files/{file1}", 'r')
    file1_data_json = json.load(file1_data)
    file1_data.close()
    file2_data =  open(f"json_files/{file2}", 'r')
    file2_data_json = json.load(file2_data)
    file2_data.close()
    merged_data = OrderedDict()
    file1_keys = list(file1_data_json.keys())
    file2_keys = list(file2_data_json.keys())
    minor = file1_keys if len(file1_data_json) < len(file2_data_json) else file2_keys
    for i in range(len(minor)):
        merged_data[file1_keys[i]] = file1_data_json[file1_keys[i]]
        merged_data[file2_keys[i]] = file2_data_json[file2_keys[i]]
        last_index = i + 1
    if len(file1_data_json) > len(file2_data_json):
        for i in range(last_index, len(file1_data_json)):
            merged_data[file1_keys[i]] = file1_data_json[file1_keys[i]]
    else:
        for i in range(last_index, len(file2_data_json)):
            merged_data[file2_keys[i]] = file2_data_json[file2_keys[i]]

    file1_name = file1.split('.')[0]
    file2_name = file2.split('.')[0]
    merged_data_file = open(f"json_files/{file1_name}_{file2_name}.json", 'w')
    merged_data_file.write(json.dumps(merged_data, indent=4))
    merged_data_file.close()

def group(files):
    i = 1
    while(True):
        if os.path.exists(f"json_files/Agrupación{i}"):
            i += 1
        else:
            break
    os.makedirs(f"json_files/Agrupación{i}")
    for file in files:
        shutil.copyfile(f"json_files/{file}", f"json_files/Agrupación{i}/{file}")
    return f"Agrupación{i}"

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

        elif command.split()[0] == 'combinar':
            combine(command.split()[1], command.split()[2])
            print("Combinado")

        elif command.split()[0] == 'agrupar':
            print(f"Archivos agrupados en la carpeta '{group(command.split()[1::])}'")

        elif command.split()[0] == 'salir':
            break

        else:
            print("Comando no reconocido")

if __name__ == "__main__":
    main()