

def recoger_datos(tipo_dato:str):
    print(f"digite {tipo_dato}")
    dato = input()
    if len(dato)>0:
        return dato
    return None
