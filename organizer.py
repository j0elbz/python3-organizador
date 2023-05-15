import os
import shutil
import tkinter
from tkinter import ttk, filedialog,messagebox
from pathlib import Path


class Organizador:
    def __init__(self) -> None:
        root = tkinter.Tk()
        root.title("Organizador")
        
        buscar = tkinter.Button(text="Ordenar",command=lambda:(self.organizador()))
        buscar.pack(side=tkinter.RIGHT)
        salir = tkinter.Button(text="Salir",command=lambda:(root.destroy()))
        salir.pack(side=tkinter.LEFT)

        root.mainloop()


    def buscar_archivos(self):
        try:
            ruta = filedialog.askdirectory()
            lista_archivos = os.listdir(ruta)
            lista_archivos = [archivo for archivo in lista_archivos if os.path.isfile(os.path.join(ruta, archivo))]
            return Path(ruta), lista_archivos
        except TypeError:
            pass


    def mover_archivo(self, archivo, carpeta_destino):
        try:
            archivo_origen = archivo.absolute()
            archivo_destino = carpeta_destino / archivo.name
            shutil.move(archivo_origen, archivo_destino)
        except TypeError:
            pass

    def organizador(self):
        # Define las extensiones y carpetas correspondientes
        extensiones = {'c':'Programacion',
                        'h':'Programacion',
                        'cpp':'Programacion',
                        'h':'Programacion',
                        'hpp':'Programacion',
                        'java':'Programacion',
                        'py':'Programacion',
                        'js':'Programacion',
                        'php':'Programacion',
                        'rb':'Programacion',
                        'swift':'Programacion',
                        'm':'Programacion',
                        'mm':'Programacion',
                        'kt':'Programacion',
                        'ts':'Programacion',
                        'pl':'Programacion',
                        'sh':'Programacion',
                        'bash':'Programacion',
                        'ps1':'Programacion',
                        'psm1':'Programacion',
                        'py':'Programacion',
                            "3gp":"Musica",
                            "aa":"Musica",
                            "aax":"Musica",
                            "act":"Musica",
                            "aiff": "Musica",
                            "amr": "Musica",
                            "ape": "Musica",
                            "au": "Musica",
                            "awb": "Musica",
                            "dct": "Musica",
                            "dss": "Musica",
                            "dvf": "Musica",
                            "flac": "Musica",
                            "gsm": "Musica",
                            "iklax": "Musica",
                            "ivs": "Musica",
                            "m4a": "Musica",
                            "m4b": "Musica",
                            "m4p": "Musica",
                            "mmf": "Musica",
                            "mp3": "Musica",
                            "mpc": "Musica",
                            "msv": "Musica",
                            "ogg": "Musica",
                            "opus": "Musica",
                            "ra": "Musica",
                            "raw": "Musica",
                            "sln": "Musica",
                            "tta": "Musica",
                            "vox": "Musica",
                            "wav": "Musica",
                            "wma": "Musica",
                            "wv": "Musica",
                            "mp4": "Videos",
                            "avi": "Videos",
                            "mkv": "Videos",
                            "mov": "Videos",
                            "flv": "Videos",
                            "wmv": "Videos",
                            "webm": "Videos",
                            "mpg": "Videos",
                            "mpeg": "Videos",
                            "m4v": "Videos",
                            "3gp": "Videos",
                            "swf": "Videos",
                            "vob": "Videos",
                            "rmvb": "Videos",
                            "rm": "Videos",
                            "m2ts": "Videos",
                            "ts": "Videos",
                            "mts": "Videos",
                            "f4v": "Videos",
                            "mxf": "Videos",
                            "mp2": "Videos",
                            "ogv": "Videos",
                            "qt": "Videos",
                            "asf": "Videos",
                            "yuv": "Videos",
                            "dav": "Videos",
                            "mpv": "Videos",
                            "divx": "Videos",
                            "flv": "Videos",
                            "m1v": "Videos",
                            "m2v": "Videos",
                            "mod": "Videos",
                            "tod": "Videos",
                            "mts": "Videos",
                            "m2p": "Videos",
                            "mvc": "Videos",
                            "cine": "Videos",
                            "h264": "Videos",
                            "h265": "Videos",
                            "hevc": "Videos",
                            "av1": "Videos",
                            "vp9": "Videos",
                            "jpg": "Imagenes",
                            "jpeg": "Imagenes",
                            "png": "Imagenes",
                            "gif": "Imagenes",
                            "bmp": "Imagenes",
                            "svg": "Imagenes",
                            "ico": "Imagenes",
                            "tiff": "Imagenes",
                            "webp": "Imagenes",
                            "raw": "Imagenes",
                            "ai": "Imagenes",
                            "eps": "Imagenes",
                            "pdf": "Imagenes",
                            "ps": "Imagenes",
                            "txt": "Documentos",
                            "doc": "Documentos",
                            "docx": "Documentos",
                            "pdf": "Documentos",
                            "odt": "Documentos",
                            "xls": "Documentos",
                            "xlsx": "Documentos",
                            "ppt": "Documentos",
                            "pptx": "Documentos",
                            "csv":"Documentos",
                            "rtf":"Documentos",
                            "md":"Documentos",
                            "html":"Documentos",
                            "json":"Documentos",
                            "yaml":"Documentos",
                            "ini":"Documentos",
                            "cfg":"Documentos",
                            "log":"Documentos",
                            "tex":"Documentos",
                            "odp":"Documentos",
                            "ods":"Documentos",
                            "odg":"Documentos",
                            "odf":"Documentos",
                            "epub":"Documentos",
                            "mobi":"Documentos",
                            "fb2":"Documentos",
                            "pdb":"Documentos",
                            "ps":"Documentos",
                            "dvi":"Documentos",
                            "djvu":"Documentos",
                            "docm":"Documentos",
                            "dotm":"Documentos",
                            "dotx":"Documentos",
                            "potm":"Documentos",
                            "potx":"Documentos",
                            "ppam":"Documentos",
                            "ppsm":"Documentos",
                            "ppsx":"Documentos",
                            "pptm":"Documentos",
                            "sldm":"Documentos",
                            "thmx":"Documentos",
                            "xlam":"Documentos",
                            "xlsb":"Documentos",
                            "xlsm":"Documentos",
                            "xltm":"Documentos",
                            "xltx":"Documentos"}

        # Busca los archivos a organizar
        try:
            carpeta_origen, archivos = self.buscar_archivos()

            # Crea las carpetas correspondientes y mueve los archivos
            archivos_totales = 0
            for archivo in archivos:
                if archivo != "organizer.py":
                    extension_archivo = os.path.splitext(archivo)[1][1:].lower()
                    if extension_archivo in extensiones:
                        carpeta_destino = carpeta_origen / extensiones[extension_archivo]
                        if not carpeta_destino.exists():
                            os.mkdir(carpeta_destino)
                        self.mover_archivo(carpeta_origen / archivo, carpeta_destino)
                        archivos_totales += 1
            
            #Muestra un mensaje indicando la cantidad de archivos movidos
            messagebox.showinfo(message=f"¡Se movieron {archivos_totales} archivos!")

        except FileNotFoundError or TypeError:
            pass


if __name__ == "__main__":
    root = Organizador()