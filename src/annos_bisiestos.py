def evaluar(anno):
    if anno < 1582:
        if anno % 4 == 0:
            return f"{anno} es un año bisiesto (calendario juliano)"
        else:
            return f"{anno} no es bisiesto (calendario juliano)"
    else:
        if anno % 400 == 0:
            return f"{anno} es un año bisiesto (calendario gregoriano)"
        elif anno % 100 == 0:
            return f"{anno} no es bisiesto (calendario gregoriano)"
        elif anno % 4 == 0:
            return f"{anno} es un año bisiesto (calendario gregoriano)"
        else:
            return f"{anno} no es bisiesto (calendario gregoriano)"
if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
