from entrenos import *

def test_lee_entrenos(fichero):
    entrenos = lee_entrenos(fichero)
    print(entrenos)

def test_entrenos_duracion_superior(entrenos, d):
    res = entrenos_duracion_superior(entrenos, d)
    print(res)

def test_suma_calorias(entrenos, f_inicio, f_fin):
    res = suma_calorias(entrenos, f_inicio, f_fin)
    print(res)

if __name__ == '__main__':
    fichero = "data\entrenos.csv"
    entrenos = lee_entrenos(fichero)
    #test_lee_entrenos(fichero)
    #test_entrenos_duracion_superior(entrenos, 125)
    test_suma_calorias(entrenos, datetime(2019, 1, 1, 00, 00), datetime(2019, 12, 31, 00, 00))


    


    