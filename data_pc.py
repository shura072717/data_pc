"""
PROGRAMA PARA GUARDAR DATOS DE MI PC
"""
import platform,socket
from pathlib import Path
import shutil
import subprocess

FILE_PATH = Path(r"C:\Users\Gonzalo\Documents\pc.txt")

def guardar_pc_info():

    pc_data = "======== INFO DE PC ========\n"
    # esto simplemente captura el sistema operativo que tengo en mi pc
    pc_data +=" SISTEMA OPERATIVO: " + platform.system()+"\n"
    # llamamos ahora la version
    pc_data += " VERSION: "+ platform.version()+"\n"
    # vemos el tipo de arquitectura
    pc_data +=" ARQUITECTURA: " + platform.machine()+"\n"
    # vemos que procesador tiene
    pc_data +=" PROCESADOR: " + platform.processor()+"\n"
    # hostname
    pc_data +=" HOSTNAME: " + socket.gethostname()+"\n"
    # direccion ip
    pc_data +=" DIRECCION IP: " + socket.gethostbyname(socket.gethostname())+"\n"
    # creamos 3 variables de cda informarcion del disco
    total, used,free = shutil.disk_usage("c:/")
    # total del disco
    pc_data += f" TOTAL DEL DISCO : {total // (1024**3)} GB\n"
    # espacio usado del disco
    pc_data += f" ESPACIO USADO: {used // (1024**3)} GB\n"
    # espacio disponible del disco
    pc_data += f" ESPACIO LIBRE : {free // (1024**3)} GB\n"
    # Miramos el tipo de interface de red en la cual el equipo esta  
    tipo_red = subprocess.check_output("netsh interface show interface", shell=True,text=True)
    pc_data +=f" TIPO DE INTERFAZ DE RED: {tipo_red}"
    tipo_red = subprocess.check_output("ipconfig", shell=True,text=True)
    pc_data +=f" INFROMACION DE LA INTERFACE DE RED: {tipo_red}"
   
    # el segundo argumento es para los permisos "w" la w es de escritura
    with open(FILE_PATH,"w") as pc_file:
       pc_file.write(pc_data)

    print("El archivo se guardado con EXITO!!")


def leer_pc_info():
   try: 
    # "r" es solo lectura
    with open(FILE_PATH,"r") as pc_file:
       pc_data = pc_file.read()
       print(pc_data)
   
   except:
      print("No se encontro el archivo")


 
   
   


# esto simepre debe ser la ultima linea del codigo 
if __name__ == "__main__":
    guardar_pc_info()
    leer_pc_info()