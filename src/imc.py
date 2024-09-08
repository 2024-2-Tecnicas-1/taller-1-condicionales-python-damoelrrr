def evaluar(peso, estatura, edad):
    tope = 22.0
    imc = peso / (estatura * estatura)

    if imc < tope and edad < 45:
        return "bajo"
    elif imc >= tope and edad < 45:
        return "medio"
    elif imc < tope and edad >= 45:
        return "medio"
    else:
        return "alto"

if __name__ == '__main__':
    peso = int(input("Peso: "))
    estatura = float(input("Estatura: "))
    edad = int(input("Edad: "))
    
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
