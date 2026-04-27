import tkinter as tk
from tkinter import messagebox

class AplicacionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi Reproductor de Playlist")
        self.root.geometry("400x300")

        # --- Crear la barra de menú ---
        barra_menu = tk.Menu(self.root)
        self.root.config(menu=barra_menu)

        # --- Menú Archivo ---
        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Abrir Playlist", command=lambda: self.abrir_ventana_secundaria("Abrir Playlist"))
        menu_archivo.add_command(label="Convertir", command=lambda: self.abrir_ventana_secundaria("Convertir"))
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Cerrar", command=self.root.quit)

        # --- Menú Editar ---
        menu_editar = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Editar", menu=menu_editar)
        menu_editar.add_command(label="Preferencias", command=lambda: self.abrir_ventana_secundaria("Preferencias"))

        # --- Menú Ayuda ---
        menu_ayuda = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Ayuda", "Versión 1.0"))

        # Etiqueta principal
        self.label = tk.Label(root, text="Ventana Principal", font=("Arial", 14))
        self.label.pack(pady=50)

    def abrir_ventana_secundaria(self, titulo):
        """Crea una nueva ventana y oculta la principal."""
        self.root.withdraw() # Oculta la ventana principal
        
        nueva_ventana = tk.Toplevel(self.root)
        nueva_ventana.title(titulo)
        nueva_ventana.geometry("300x200")

        tk.Label(nueva_ventana, text=f"Estas en: {titulo}", pady=20).pack()

        # Botón para volver
        btn_volver = tk.Button(
            nueva_ventana, 
            text="Volver a la Principal", 
            command=lambda: self.volver_principal(nueva_ventana)
        )
        btn_volver.pack(pady=10)

    def volver_principal(self, ventana_actual):
        """Cierra la ventana actual y muestra la principal."""
        ventana_actual.destroy()
        self.root.deiconify() # Vuelve a mostrar la principal

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionApp(root)
    root.mainloop()

