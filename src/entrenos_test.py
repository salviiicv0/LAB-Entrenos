from entrenos import *

def test_lee_entrenos(fichero):
    print(f"Probando la carga de datos de Entrenos...")
    entrenos = lee_entrenos(fichero)
    print(f"Tres primeros registros {entrenos[:3]}")
    print("========================================")
    print(f"Tres últimos registros {entrenos[:-3]}")

def test_tipos_entreno(entrenos):
    tipos = tipos_entreno(entrenos)
    print(f"Los tipos de entrenamientos en orden alfabético son: {tipos}")

def test_entrenos_duracion_superior(entrenos, d):
    res = entrenos_duracion_superior(entrenos, d)
    print(f"Los entrenos con duración superior a {d} son {res}")

def test_suma_calorias(entrenos,f_inicio,f_fin):
    total_cal = suma_calorias(entrenos,f_inicio,f_fin)
    print(f"La suma de las caloraias desde la fefcha {f_inicio} y {f_fin} es: {total_cal}")


if __name__ == "__main__":
    entrenos = lee_entrenos("data\entrenos.csv")
    #lee_entrenos_test("LAB-Entrenos\data\entrenos.csv")
    #test_tipos_entreno(entrenos)
    #test_entrenos_duracion_superior(entrenos,100)
    test_suma_calorias(entrenos,datetime(2019,12,1), datetime(2020,12,1))

