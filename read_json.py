import json 

with open('extension.json') as json_file:

    data = json.load(json_file)

    for category in data:
        print("Formatos Archivos: ",category['file_format'])
        print("Carpeta----------: ", category['folder'])