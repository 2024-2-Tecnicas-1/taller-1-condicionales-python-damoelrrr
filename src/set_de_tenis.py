def evaluar(num_victorias_a, num_victorias_b):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
    if (num_victorias_a == 3 and num_victorias_b == 7) or (num_victorias_b == 7 and num_victorias_a == 3) or \
       (num_victorias_a == 0 and num_victorias_b == 7) or (num_victorias_b == 0 and num_victorias_a == 7) or \
       (num_victorias_a == 8 or num_victorias_b == 8) or (num_victorias_a > 7 or num_victorias_b > 7):
        return "Inválido"
    if (num_victorias_a >= 6 and num_victorias_a - num_victorias_b >= 2) or (num_victorias_a == 7 and num_victorias_b == 6):
        return "Ganó A"
    if (num_victorias_b >= 6 and num_victorias_b - num_victorias_a >= 2) or (num_victorias_a == 6 and num_victorias_b == 7):
        return "Ganó B"
    return "Aún no termina"
