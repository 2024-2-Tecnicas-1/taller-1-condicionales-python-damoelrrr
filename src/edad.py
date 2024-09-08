from datetime import datetime

def evaluar(dia, mes, anno):
    current_date = datetime.now()
    current_day = current_date.day
    current_month = current_date.month
    current_year = current_date.year
    
    edad = current_year - anno
    
    if current_month < mes or (current_month == mes and current_day < dia):
        edad -= 1
    
    return f"Usted tiene {edad} años"

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    anno = int(input("Año: "))
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)

