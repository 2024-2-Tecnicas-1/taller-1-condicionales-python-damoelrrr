def evaluar(dividendo, divisor):
    if divisor == 0:
        return "Error: No se puede dividir por cero."
    
    cociente = dividendo // divisor
    residuo = dividendo % divisor
    
    if residuo == 0:
        respuesta = "La división es exacta.\n"
    else:
        respuesta = "La división no es exacta.\n"
    
    respuesta += f"Cociente: {cociente}\nResiduo: {residuo}"
    return respuesta

if __name__ == '__main__':
    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))
    
    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
