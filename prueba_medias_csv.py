import numpy as np
from scipy.stats import norm


def truncar(numeros, decimales):
    factor = 10.0 ** decimales
    return np.trunc(numeros * factor) / factor


def prueba_medias(numeros_aleatorios, alpha=0.05):
    numeros_aleatorios = truncar(numeros_aleatorios, 5)
    n = len(numeros_aleatorios)
    media_esperada = 0.5
    R = np.mean(numeros_aleatorios)
    valor_critico = 1 - (alpha / 2)
    Z = norm.ppf(valor_critico)
    error_estandar = 1 / (np.sqrt(12 * n))
    limite_inferior = media_esperada - Z * error_estandar
    limite_superior = media_esperada + Z * error_estandar

    resultado = f"PRUEBA DE MEDIAS\nMedia muestral (R): {R}\nIntervalo de confianza: [{
        limite_inferior}, {limite_superior}]\n"

    if limite_inferior <= R <= limite_superior:
        resultado += "La secuencia de números aleatorios pasa la prueba de medias."
    else:
        resultado += "La secuencia de números aleatorios NO pasa la prueba de medias."

    return resultado
