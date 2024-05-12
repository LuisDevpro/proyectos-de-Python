import zipfile
from tkinter import filedialog

def convertir_a_zip(ruta_archivo_word, ruta_zip):
    with zipfile.ZipFile(ruta_zip, 'w') as archivo_zip:
        archivo_zip.write(ruta_archivo_word, arcname='documento_word.docx')

#archivo que se convertira en zip y ruta donde se aguarda utilizando la librerias FILEDIALOG
ruta_archivo_word = filedialog.askopenfilename(filetypes=[("Archivos ", "*.docx")])  # Ruta del archivo de Word
ruta_zip = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("Archivos de documento", "*.zip"), ("Todos los archivos", "*.*")])  # Ruta donde se guardará el archivo ZIP

convertir_a_zip(ruta_archivo_word, ruta_zip)
