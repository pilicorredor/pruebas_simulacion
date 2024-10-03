import numpy as np
from scipy.stats import chi2


def prueba_varianza(numeros_aleatorios, alpha=0.05):
    n = len(numeros_aleatorios)
    varianza_muestral = np.var(numeros_aleatorios, ddof=1)
    chi2_inf = chi2.ppf(alpha / 2, n - 1)
    chi2_sup = chi2.ppf(1 - alpha / 2, n - 1)
    limite_inferior = chi2_inf / (12 * (n - 1))
    limite_superior = chi2_sup / (12 * (n - 1))

    resultado = f"PRUEBA DE VARIANZAS\nVarianza muestral: {
        varianza_muestral}\nIntervalo de confianza de la varianza: [{limite_inferior}, {limite_superior}]\n"

    if limite_inferior <= varianza_muestral <= limite_superior:
        resultado += "La secuencia de números aleatorios pasa la prueba de varianza."
    else:
        resultado += "La secuencia de números aleatorios NO pasa la prueba de varianza."

    return resultado
