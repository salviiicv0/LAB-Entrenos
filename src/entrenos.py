import csv
from collections import namedtuple
from datetime import datetime

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(fichero):
    entrenos = []
    with open(fichero, encoding='UTF-8') as f:
        lector = csv.reader(f)
        next(lector)
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            tipo = str(tipo)
            fechahora = datetime.strptime(fechahora, '%d/%m/%Y %H:%M')
            ubicacion = str(ubicacion)
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido = bool(compartido)
            entrenos.append(Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido))
    return entrenos

def entrenos_duracion_superior(entrenos, d):
    res = []
    for entreno in entrenos:
        if entreno.duracion > d:
            res.append(entreno)
    return res

def suma_calorias(entrenos, f_inicio, f_fin):
    res = 0
    for entreno in entrenos:
        if entreno.fechahora >= f_inicio and entreno.fechahora <= f_fin:
            res += entreno.calorias
    return res