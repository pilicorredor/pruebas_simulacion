import tkinter as tk
from tkinter import ttk


def mostrar_tabla_en_nueva_ventana(columnas, datos, titulo="Tabla de Resultados"):
    ventana_tabla = tk.Toplevel()
    ventana_tabla.title(titulo)
    ventana_tabla.geometry("900x500")

    # Estilo para los encabezados de la tabla
    style = ttk.Style()
    style.configure("Treeview.Heading", font=(
        'Helvetica', 10, 'bold'), foreground="blue")
    style.configure("Treeview", rowheight=30)

    # Crear un Treeview para la tabla con las columnas dinámicas
    tree = ttk.Treeview(ventana_tabla, columns=columnas, show='headings')

    # Definir los encabezados dinámicos
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center")

    # Agregar los datos a la tabla
    for row in datos:
        tree.insert("", "end", values=row)

    # Estilo de las líneas divisorias
    style.configure("Treeview", highlightthickness=2, bd=2, relief="solid")

    # Empaquetar la tabla en la ventana
    tree.pack(padx=10, pady=10, fill="both", expand=True)

    # Añadir un scrollbar
    scrollbar = ttk.Scrollbar(
        ventana_tabla, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Botón para cerrar la ventana
    btn_cerrar = tk.Button(ventana_tabla, text="Cerrar",
                           command=ventana_tabla.destroy, font=('Helvetica', 10, 'bold'))
    btn_cerrar.pack(pady=10)
