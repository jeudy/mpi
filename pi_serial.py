# -*- coding: UTF-8 -*-

# Funcion para calcular PI por medio del producto de Wallis
def calcular_pi(N):
    i = 1

    acum = 1.0

    while i < N:
        # Producto de Wallis
        acum *= ((2.*i / (2.*i - 1)) * (2.*i / (2.*i + 1)))
        i += 1

    return acum * 2

print calcular_pi(100000)