import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter import ttk
import pandas as pd
from prueba_medias_csv import prueba_medias
from prueba_varianzas import prueba_varianza
from chi_cuadrado import prueba_chi_cuadrado
from prueba_ks import kolmogorov_smirnov
from prueba_poker import prueba_poker
from tabla_resultados import mostrar_tabla_en_nueva_ventana

# Función para cargar el archivo CSV
def cargar_csv():
    global numeros
    archivo = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if archivo:
        try:
            df = pd.read_csv(archivo)
            if 'numeros' in df.columns:
                numeros = df['numeros'].values
                messagebox.showinfo("Archivo cargado",
                                    "Archivo CSV cargado correctamente.")
                habilitar_botones()
            else:
                messagebox.showerror(
                    "Error", "El archivo debe tener una columna 'numeros'.")
                numeros = None
        except Exception as e:
            messagebox.showerror("Error", str(e))
            numeros = None

# Habilitar botones una vez se haya cargado el archivo
def habilitar_botones():
    btn_medias.config(state=tk.NORMAL)
    btn_varianza.config(state=tk.NORMAL)
    btn_chi_cuadrado.config(state=tk.NORMAL)
    btn_ks.config(state=tk.NORMAL)
    btn_poker.config(state=tk.NORMAL)

# Funciones para los botones de pruebas
def ejecutar_prueba_medias():
    if numeros is not None:
        resultado = prueba_medias(numeros)
        mostrar_resultado(resultado)


def ejecutar_prueba_varianza():
    if numeros is not None:
        resultado = prueba_varianza(numeros)
        mostrar_resultado(resultado)


def ejecutar_prueba_chi_cuadrado():
    if numeros is not None:
        tabla, resultado = prueba_chi_cuadrado(numeros)
        mostrar_resultado(resultado)
        columnas = ["Intervalo (Inicio)", "Intervalo (Final)",
                    "Frec Observada", "Frec Esperada", "Chi2 por Intervalo"]
        mostrar_tabla_en_nueva_ventana(
            columnas, tabla, "Tabla de Resultados - Prueba Chi Cuadrado")


def ejecutar_prueba_ks():
    if numeros is not None:
        tabla, resultado = kolmogorov_smirnov(numeros)
        columnas = ['Intervalo (Inicio)', 'Intervalo (Final)', 'Frec obt', 'Frec obt A.',
                    'P Obt A.', 'Fre Esp A.', 'Prob Esp A.', 'Dif']
        mostrar_tabla_en_nueva_ventana(
            columnas, tabla, "Tabla de Resultados - Prueba Kolmogorov-Smirnov")
        mostrar_resultado(resultado)


def ejecutar_prueba_poker():
    if numeros is not None:
        tabla, resultado = prueba_poker(numeros)
        columnas = ['Categoría', 'Frecuencia Observada',
                    'Probabilidad Teórica', 'Frecuencia Esperada', 'Chi2 por Categoría']
        mostrar_tabla_en_nueva_ventana(
            columnas, tabla, "Tabla de Resultados - Prueba Poker")
        mostrar_resultado(resultado)

# Función para mostrar los resultados en un cuadro de texto
def mostrar_resultado(resultado):
    result_text.config(state=tk.NORMAL)
    result_text.insert(tk.END, resultado + "\n\n")
    result_text.config(state=tk.DISABLED)


# Configuración de la ventana principal
root = tk.Tk()
root.title("Pruebas de Números Pseudoaleatorios")
root.geometry("700x500")

# Botón para importar el archivo CSV
btn_cargar_csv = tk.Button(root, text="Importar archivo CSV", command=cargar_csv, font=(
    'Helvetica', 12), bg="#4CAF50", fg="white")
btn_cargar_csv.pack(pady=10)

# Botones del menú (inicialmente deshabilitados)
btn_medias = tk.Button(root, text="Prueba de Medias", command=ejecutar_prueba_medias,
                       state=tk.DISABLED, font=('Helvetica', 12), bg="#DBE7F3",)
btn_varianza = tk.Button(root, text="Prueba de Varianza", command=ejecutar_prueba_varianza,
                         state=tk.DISABLED, font=('Helvetica', 12), bg="#DBE7F3",)
btn_chi_cuadrado = tk.Button(root, text="Prueba de Chi Cuadrado", command=ejecutar_prueba_chi_cuadrado,
                             state=tk.DISABLED, font=('Helvetica', 12), bg="#DBE7F3",)
btn_ks = tk.Button(root, text="Prueba de Kolmogorov-Smirnov", command=ejecutar_prueba_ks,
                   state=tk.DISABLED, font=('Helvetica', 12), bg="#DBE7F3",)
btn_poker = tk.Button(root, text="Prueba de Poker", command=ejecutar_prueba_poker,
                      state=tk.DISABLED, font=('Helvetica', 12), bg="#DBE7F3",)
btn_medias.pack(pady=10)
btn_varianza.pack(pady=10)
btn_chi_cuadrado.pack(pady=10)
btn_ks.pack(pady=10)
btn_poker.pack(pady=10)

# Cuadro de texto para mostrar los resultados de las pruebas
result_text = scrolledtext.ScrolledText(
    root, height=10, width=90, font=('Helvetica', 10))
result_text.pack(pady=10)
result_text.config(state=tk.DISABLED)

# Iniciar el bucle principal de Tkinter
root.mainloop()
