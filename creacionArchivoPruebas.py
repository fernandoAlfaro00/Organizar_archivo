import os
import json 
directory = r'./CPruebas'
with open('./Modelo/extension.json') as json_file:

    data = json.load(json_file)

    for category in data:
        for ext in category['file_format']:

            for i in range(1,30):

                open(os.path.join(directory,  "nombre{}.{}".format(i,ext) ), "w").close()
               