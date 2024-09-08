def evaluar(numero1, numero2, numero3, numero4):
    
    numeros = [numero1, numero2, numero3, numero4]
    
    
    numeros.sort()
    
    
    return str(numeros)

if __name__ == '__main__':
    numero1 = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))
    numero3 = int(input("Número 3: "))
    numero4 = int(input("Número 4: "))
    
    respuesta = evaluar(numero1, numero2, numero3, numero4)
    print(respuesta)
