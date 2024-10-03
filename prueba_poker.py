import numpy as np
from collections import Counter
from scipy.stats import chi2

# Función para categorizar los números según las combinaciones de dígitos
def categorizar_numero(numero):
    # Extraer solo los primeros 5 dígitos después del punto
    digitos = list(str(numero).split('.')[1][:5])
    conteo = Counter(digitos)
    ocurrencias = sorted(conteo.values(), reverse=True)

    # Clasificación
    if ocurrencias == [5]:
        return 'Q'  # Quintilla
    elif ocurrencias == [4, 1]:
        return 'P'  # Poker
    elif ocurrencias == [3, 2]:
        return 'F'  # Full House
    elif ocurrencias == [3, 1, 1]:
        return 'K'  # Tercia
    elif ocurrencias == [2, 2, 1]:
        return 'T'  # Dos pares
    elif ocurrencias == [2, 1, 1, 1]:
        return 'O'  # Un par
    else:
        return 'D'  # Todos diferentes

# Función para realizar la prueba de Póker
def prueba_poker(numeros_aleatorios):
    categorias = [categorizar_numero(num) for num in numeros_aleatorios]

    n = len(numeros_aleatorios)
    probabilidades = {'D': 0.3024, 'O': 0.504, 'T': 0.108,
                      'K': 0.072, 'F': 0.009, 'P': 0.0045, 'Q': 0.0001}

    tipos = ['D', 'O', 'T', 'K', 'F', 'P', 'Q']
    frec_observadas = []
    esperados = []
    probabilidades_teoricas = []
    chi2_values = []

    for tipo in tipos:
        frec = categorias.count(tipo)
        prob = probabilidades[tipo]  # Obtener la probabilidad teórica
        Ei = prob * n
        chi2_val = ((Ei - frec) ** 2) / Ei if Ei != 0 else 0

        frec_observadas.append(frec)  # Frecuencia observada (números)
        esperados.append(Ei)  # Frecuencia esperada (números)
        probabilidades_teoricas.append(prob)  # Probabilidad teórica
        chi2_values.append(chi2_val)  # Valores de Chi-cuadrado por categoría

    # Generar los datos para la tabla en formato similar a KS
    datos = [
        [
            tipos[i], frec_observadas[i], f"{probabilidades_teoricas[i]:.5f}",
            f"{esperados[i]:.5f}", f"{chi2_values[i]:.5f}"
        ]
        for i in range(len(tipos))
    ]

    chi2_total = np.sum(chi2_values)
    grados_de_libertad = len(tipos) - 1
    valor_critico = chi2.ppf(0.95, grados_de_libertad)

    resultado = f"PRUEBA PÓKER\n"
    resultado += f"Estadístico Chi-cuadrado total: {chi2_total}\n"
    resultado += f"Valor crítico de Chi-cuadrado: {valor_critico}\n"

    if chi2_total < valor_critico:
        resultado += "La secuencia pasa la prueba de Póker.\n"
    else:
        resultado += "La secuencia NO pasa la prueba de Póker.\n"

    return datos, resultado
