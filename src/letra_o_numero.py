def evaluar(caracter):
    if not (caracter.isalpha() or caracter.isdigit()):
        return "No es letra ni número"
    
    if caracter.isdigit():
        return "Es número"
    elif caracter.isupper():
        return "Es letra mayúscula"
    elif caracter.islower():
        return "Es letra minúscula"
    
    return ""

if __name__ == '__main__':
    caracter = input("Caracter: ")
    
    respuesta = evaluar(caracter)
    print(respuesta)
