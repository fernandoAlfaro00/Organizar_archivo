import os
import sys
import json
import glob
import fnmatch
from argparse import ArgumentParser

# Extraer extensiones de los archivos del entorno de ejecucion  y guardarlo en un json o otro formato
# Ver la forma de ordenar los archivos segun la extension de forma automatica
# Rutas


class Organizar:

    def __init__(self):

        self.destination = ""
        self.source_path = ""
        self.file_extension = os.path.join(os.getcwd(),'Modelo/extension.json')
        self.folder = []
        self.included_extensions = []
        self.extensiones = ''
        self.listado_archivos = []


    def cargar_extensiones(self):

        try:
            self.extensiones = json.load(open(self.file_extension))

            print(self.extensiones)

        except FileNotFoundError as fne:

            print(fne)

    
    def listar_archivos(self, source_path=os.getcwd(), extension = '*'):

        self.source_path = source_path

        self.listado_archivos =  glob.glob(os.path.join(self.source_path ,('*.' + extension)))

        print(self.listado_archivos)

        return self.listado_archivos


   

    def categorizar_archivos(self):

        wea = []
        for categoria in  self.extensiones:

            print('Archivo tipo',categoria['category_file'])
            for extension in categoria['file_format']:

                wea.append(extension)
                #devolvemos el listado según la extension
                archvi = fnmatch.filter(self.listado_archivos, ('*.'+extension))

                print(extension , archvi)
                
        #ver esta parte
        print("parte de ")
        sin_categoria = set()
        con_categoria = set()
        for e in self.listado_archivos:

            if e.split('.')[-1] in tuple(wea):

               con_categoria.add(e)
               continue
            
            sin_categoria.add(e)

        
        

        
    def get_nombreArchivos(self):

        file_names = [fn for fn in self.listar_archivos()
                      if any(fn.endswith(ext) for ext in self.included_extensions)]

        return file_names

    def seleccionar_archivos(self):
        pass

    def mover_archivos(self, files, folder):
        for file in files:
            try:
                os.renames(os.path.join(self.source_path, file), os.path.join(
                    self.destination, self.folder, file))
                print("Se a movido correctamente")
            except FileExistsError as fee:
                print(fee)

            except:
                print("Pero que a pasao ?!!!!!!", sys.exc_info()[0])

    def renombrar_archivo(self, file):
        option = input("Desea conservar los dos archivos [y/n] ")
        if option == "y":
            filename, extension = os.path.splitext(file)
            filename = filename + "1"

            os.renames(os.path.join(self.source_path, file), os.path.join(
                self.destination, self.folder, (filename+extension)))
