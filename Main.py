import sys
import fnmatch
from Modelo.Organizar import Organizar

def main(argv):

    org = Organizar()

    org.listar_archivos('/home/Akira_Genocyber/Documentos')

    org.cargar_extensiones()

    org.categorizar_archivos()

    

    
    

    # for archivo in listado_archivos:
    # # org.cargar_extensiones()
    

if  __name__ == '__main__':
    
    main(sys.argv)