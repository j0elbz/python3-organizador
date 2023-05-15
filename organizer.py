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
        extensiones = {'c':'Programación',
                        'h':'Programación',
                        'cpp':'Programación',
                        'h':'Programación',
                        'hpp':'Programación',
                        'java':'Programación',
                        'py':'Programación',
                        'js':'Programación',
                        'php':'Programación',
                        'rb':'Programación',
                        'swift':'Programación',
                        'm':'Programación',
                        'mm':'Programación',
                        'kt':'Programación',
                        'ts':'Programación',
                        'pl':'Programación',
                        'sh':'Programación',
                        'bash':'Programación',
                        'ps1':'Programación',
                        'psm1':'Programación',
                        'py':'Programación',
                            "3gp":"Música",
                            "aa":"Música",
                            "aax":"Música",
                            "act":"Música",
                            "aiff": "Música",
                            "amr": "Música",
                            "ape": "Música",
                            "au": "Música",
                            "awb": "Música",
                            "dct": "Música",
                            "dss": "Música",
                            "dvf": "Música",
                            "flac": "Música",
                            "gsm": "Música",
                            "iklax": "Música",
                            "ivs": "Música",
                            "m4a": "Música",
                            "m4b": "Música",
                            "m4p": "Música",
                            "mmf": "Música",
                            "mp3": "Música",
                            "mpc": "Música",
                            "msv": "Música",
                            "ogg": "Música",
                            "opus": "Música",
                            "ra": "Música",
                            "raw": "Música",
                            "sln": "Música",
                            "tta": "Música",
                            "vox": "Música",
                            "wav": "Música",
                            "wma": "Música",
                            "wv": "Música",
                            "mp4": "Vídeos",
                            "avi": "Vídeos",
                            "mkv": "Vídeos",
                            "mov": "Vídeos",
                            "flv": "Vídeos",
                            "wmv": "Vídeos",
                            "webm": "Vídeos",
                            "mpg": "Vídeos",
                            "mpeg": "Vídeos",
                            "m4v": "Vídeos",
                            "3gp": "Vídeos",
                            "swf": "Vídeos",
                            "vob": "Vídeos",
                            "rmvb": "Vídeos",
                            "rm": "Vídeos",
                            "m2ts": "Vídeos",
                            "ts": "Vídeos",
                            "mts": "Vídeos",
                            "f4v": "Vídeos",
                            "mxf": "Vídeos",
                            "mp2": "Vídeos",
                            "ogv": "Vídeos",
                            "qt": "Vídeos",
                            "asf": "Vídeos",
                            "yuv": "Vídeos",
                            "dav": "Vídeos",
                            "mpv": "Vídeos",
                            "divx": "Vídeos",
                            "flv": "Vídeos",
                            "m1v": "Vídeos",
                            "m2v": "Vídeos",
                            "mod": "Vídeos",
                            "tod": "Vídeos",
                            "mts": "Vídeos",
                            "m2p": "Vídeos",
                            "mvc": "Vídeos",
                            "cine": "Vídeos",
                            "h264": "Vídeos",
                            "h265": "Vídeos",
                            "hevc": "Vídeos",
                            "av1": "Vídeos",
                            "vp9": "Vídeos",
                            "jpg": "Imágenes",
                            "jpeg": "Imágenes",
                            "png": "Imágenes",
                            "gif": "Imágenes",
                            "bmp": "Imágenes",
                            "svg": "Imágenes",
                            "ico": "Imágenes",
                            "tiff": "Imágenes",
                            "webp": "Imágenes",
                            "raw": "Imágenes",
                            "ai": "Imágenes",
                            "eps": "Imágenes",
                            "pdf": "Imágenes",
                            "ps": "Imágenes",
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
