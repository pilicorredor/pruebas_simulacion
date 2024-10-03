import numpy as np

# Función para realizar la prueba de Kolmogorov-Smirnov y devolver los datos de la tabla y los resultados
def kolmogorov_smirnov(numeros_aleatorios, alpha=0.05):
    # Número de datos
    n = len(numeros_aleatorios)

    # Calcular el número menor y mayor de la lista de números
    numero_menor = np.min(numeros_aleatorios)
    numero_mayor = np.max(numeros_aleatorios)

    # Calcular el número de intervalos basado en la raíz cuadrada del número de datos
    k = int(np.sqrt(n))

    # Crear los intervalos
    intervalos = np.linspace(numero_menor, numero_mayor, k + 1)

    # Contar las frecuencias observadas en cada intervalo
    frecuencias_observadas, _ = np.histogram(
        numeros_aleatorios, bins=intervalos)

    # Calcular la frecuencia esperada por intervalo (distribución uniforme)
    frecuencia_esperada = n / k

    # Calcular las frecuencias acumuladas
    frecuencias_observadas_acumuladas = np.cumsum(frecuencias_observadas)
    frecuencias_esperadas_acumuladas = np.arange(
        1, k + 1) * frecuencia_esperada

    # Calcular las probabilidades observadas y esperadas acumuladas
    probabilidades_observadas_acumuladas = frecuencias_observadas_acumuladas / n
    probabilidades_esperadas_acumuladas = frecuencias_esperadas_acumuladas / n

    # Calcular las diferencias entre probabilidades observadas y esperadas
    diferencias = np.abs(probabilidades_observadas_acumuladas -
                         probabilidades_esperadas_acumuladas)

    # Calcular la diferencia máxima
    D_max = np.max(diferencias)

    # Valor crítico para la prueba de Kolmogorov-Smirnov
    D_critico = 1.36 / np.sqrt(n)

    datos = [
        [
            f"{intervalos[i]:.5f}", f"{intervalos[i+1]
                :.5f}", frecuencias_observadas[i],
            frecuencias_observadas_acumuladas[i], f"{
                probabilidades_observadas_acumuladas[i]:.5f}",
            f"{frecuencias_esperadas_acumuladas[i]:.5f}", f"{
                probabilidades_esperadas_acumuladas[i]:.5f}",
            f"{diferencias[i]:.5f}"
        ]
        for i in range(k)
    ]

    # Generar el resultado en forma de texto
    resultado = f"PRUEBA KOLMOGOROV SMIRNOV\n"
    resultado += f"Diferencia máxima (D_max): {D_max}\n"
    resultado += f"Valor crítico de Kolmogorov-Smirnov (D_crítico): {
        D_critico}\n"
    if D_max <= D_critico:
        resultado += "La secuencia de números aleatorios pasa la prueba de Kolmogorov-Smirnov.\n"
    else:
        resultado += "La secuencia de números aleatorios NO pasa la prueba de Kolmogorov-Smirnov.\n"

    return datos, resultado
