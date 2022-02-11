import json

data = open('data.txt', 'r', encoding="utf-8").readlines()

states = {
    "Ciudad de México" : {},
    "Aguascalientes" : {},
    "Baja California" : {},
    "Baja California Sur" : {},
    "Campeche" : {},
    "Coahuila de Zaragoza" : {},
    "Colima" : {},
    "Chiapas" : {},
    "Chihuahua" : {},
    "Durango" : {},
    "Guanajuato" : {},
    "Guerrero" : {},
    "Hidalgo" : {},
    "Jalisco" : {},
    "México" : {},
    "Michoacán de Ocampo" : {},
    "Morelos" : {},
    "Nayarit" : {},
    "Nuevo León" : {},
    "Oaxaca" : {},
    "Puebla" : {},
    "Querétaro" : {},
    "Quintana Roo" : {},
    "San Luis Potosí" : {},
    "Sinaloa" : {},
    "Sonora" : {},
    "Tabasco" : {},
    "Tamaulipas" : {},
    "Tlaxcala" : {},
    "Veracruz de Ignacio de la Llave" : {},
    "Yucatán" : {},
    "Zacatecas" : {},
}

for line in data:
    line = line.strip("\n")
    line = line.split("|")
    line.remove("")
    try:
        states[line[4]][line[0]].append({
            "Colonia" : line[1],
            "Municipio" : line[4] + " " + line[3],
        })
    except:
        states[line[4]][line[0]] = []
        states[line[4]][line[0]].append({
            "Colonia" : line[1],
            "Municipio" : line[4] + " " + line[3],
        })


for n in states:
    out_file = open(f'json_files/{n}.json', 'w')
    json_object = json.dumps(states[n], indent=4)
    out_file.write(json_object)
    out_file.close()