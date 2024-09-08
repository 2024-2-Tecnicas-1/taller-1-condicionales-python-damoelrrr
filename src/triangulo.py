def evaluar(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "No es un triángulo válido"
    else:
        if a == b == c:
            return "Triángulo equilátero"
        elif a == b or a == c or b == c:
            return "Triángulo isósceles"
        else:
            return "Triángulo escaleno"

if __name__ == '__main__':
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    
    respuesta = evaluar(a, b, c)
    print(respuesta)
