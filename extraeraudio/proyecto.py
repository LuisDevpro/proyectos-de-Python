#importar la libreria 
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

#aqui hacemos que la funcion del proyecto


ruta_video = filedialog.askopenfilename(filetypes=[("Archivos de video", "*.mp4;*.avi;*.mkv")])
if ruta_video:
        try:
            video = VideoFileClip(ruta_video) # type: ignore
            ruta_guardado = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Archivos de audio", "*.mp3"), ("Todos los archivos", "*.*")])
            if ruta_guardado:
                audio = video.audio
                audio.write_audiofile(ruta_guardado)
                audio.close()
                video.close()
                print("Audio extraído y guardado correctamente en:", ruta_guardado)
        except Exception as e:
            print("Error al extraer el audio:", str(e))
