import tkinter as tk
from tkinter import filedialog, messagebox
import os

def configurar_dialogo(root):
    """Intenta configurar el diálogo para ocultar archivos ocultos (especialmente en Linux)"""
    try:
        # Forzamos la carga del código interno de diálogos de Tcl
        root.tk.call('catch', 'tk_getOpenFile -foo')
        # Desactivamos el botón de 'Mostrar Ocultos' y su estado
        root.tk.call('set', '::tk::dialog::file::showHiddenBtn', '0')
        root.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')
    except:
        pass # Si falla en Windows/Mac, simplemente sigue el comportamiento nativo

def seleccionar_archivo():
    configurar_dialogo(ventana)
    # Al definir filetypes, filtramos visualmente solo lo que nos interesa
    ruta = filedialog.askopenfilename(
        title="Seleccionar archivo de texto", 
        filetypes=[("Archivos de texto", "*.txt")]
    )
    if ruta:
        entrada_ruta.delete(0, tk.END)
        entrada_ruta.insert(0, ruta)

# --- El resto de tu lógica se mantiene igual ---

def leer_configuracion():
    archivo_config = "config.txt"
    if os.path.exists(archivo_config):
        with open(archivo_config, "r", encoding="utf-8") as f:
            return f.read().strip()
    return "No hay dirección configurada"

def procesar_y_guardar():
    direccion = entrada_config.get()
    try:
        with open("resultado.txt", "a", encoding="utf-8") as f:
            f.write(f"La direccion es: {direccion}\n")
        messagebox.showinfo("Éxito", "Guardado en resultado.txt")
    except Exception as e:
        messagebox.showerror("Error", f"Fallo al guardar: {e}")

ventana = tk.Tk()
ventana.title("Gestor de Direcciones")
ventana.geometry("400x250")

tk.Label(ventana, text="Dirección desde config.txt:", font=("Arial", 10, "bold")).pack(pady=5)
entrada_config = tk.Entry(ventana, width=40)
entrada_config.insert(0, leer_configuracion())
entrada_config.pack(pady=5)

tk.Label(ventana, text="Seleccionar un archivo extra:").pack(pady=5)
entrada_ruta = tk.Entry(ventana, width=40)
entrada_ruta.pack(pady=5)
btn_buscar = tk.Button(ventana, text="Explorar...", command=seleccionar_archivo)
btn_buscar.pack(pady=2)

btn_guardar = tk.Button(ventana, text="Guardar en resultado.txt", 
                       bg="#4CAF50", fg="white", command=procesar_y_guardar)
btn_guardar.pack(pady=20)

ventana.mainloop()

