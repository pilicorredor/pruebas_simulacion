import numpy as np
from scipy.stats import chi2

# Función para mostrar los resultados en una tabla compatible con Tkinter
def mostrar_tabla(intervalos, frec_obtenida, frec_esperada, chi2_intervalos):
    # Convertir los datos en una lista de listas para que Tkinter pueda mostrarla
    tabla = []

    for i in range(len(frec_obtenida)):
        fila = [
            round(intervalos[i], 4),  # Intervalo (Inicio)
            round(intervalos[i + 1], 4),  # Intervalo (Final)
            frec_obtenida[i],  # Frecuencia Observada
            round(frec_esperada[i], 4),  # Frecuencia Esperada
            round(chi2_intervalos[i], 4)  # Chi2 por Intervalo
        ]
        tabla.append(fila)

    return tabla

# Función para realizar la prueba de Chi-cuadrado de bondad de ajuste
def prueba_chi_cuadrado(numeros_aleatorios, alpha=0.05):
    n = len(numeros_aleatorios)

    # Definir el número de intervalos (k) según la raíz cuadrada del tamaño de la muestra
    k = int(np.sqrt(n))

    # Frecuencia esperada por intervalo
    frecuencia_esperada = n / k

    # Crear los intervalos para los números aleatorios
    intervalos = np.linspace(np.min(numeros_aleatorios),
                             np.max(numeros_aleatorios), k + 1)

    # Calcular las frecuencias observadas
    frecuencias_observadas, _ = np.histogram(
        numeros_aleatorios, bins=intervalos)

    # Calcular el estadístico Chi-cuadrado por intervalo
    chi2_intervalos = (frecuencias_observadas -
                       frecuencia_esperada) ** 2 / frecuencia_esperada

    # Calcular el valor total de Chi-cuadrado
    chi2_total = np.sum(chi2_intervalos)

    # Grados de libertad (k - 1)
    grados_libertad = k - 1
    chi2_critico = chi2.ppf(1 - alpha, df=grados_libertad)

    # Generar la tabla de resultados
    tabla = mostrar_tabla(intervalos, frecuencias_observadas, [
                          frecuencia_esperada] * k, chi2_intervalos)

    # Generar el resultado del test
    resultado = f"PRUEBA CHI CUADRADO\n"
    resultado += f"Estadístico Chi-cuadrado total: {chi2_total}\n"
    resultado += f"Valor crítico de Chi-cuadrado (α = {alpha}, gl = {
        grados_libertad}): {chi2_critico}\n"

    if chi2_total <= chi2_critico:
        resultado += "La secuencia de números aleatorios pasa la prueba de Chi-cuadrado."
    else:
        resultado += "La secuencia de números aleatorios NO pasa la prueba de Chi-cuadrado."

    return tabla, resultado
