import csv # Para leer los csv de datos
from collections import namedtuple # Para definir tuplas con nombres
from datetime import datetime # Para leer fechas
Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido') # Tuplas

def lee_entrenos(nombre_fichero):
    entreno = []
    with open(nombre_fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for linea in f:
            tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido = linea.split(",")
            tipo = str(tipo)
            fechahora = datetime.strptime(fechahora, "%d/%m/%Y %H:%M")
            ubicacion = str(ubicacion)
            duracion = int(duracion)
            calorias = float(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido = compartido == "S" #bool(compartido)
            entreno.append(Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido))
        return entreno

def tipos_entreno(entrenos):
    res = set()
    for e in entrenos:
        res.add(e.tipo)
    return sorted(res)

def entrenos_duracion_superior(entrenos, d):
    res = []
    for e in entrenos:
        if e.duracion > d:
            res.append(e)
    return res

def suma_calorias(entrenos,f_inicio,f_fin):
    res = 0
    for e in entrenos:
        if f_inicio <= e.fechahora <= f_fin:
            res += e.calorias
    return res

