from datetime import datetime
from time import gmtime, strftime

import json
import requests 

class ResponseBot():
    def __init__(self):
        pass

    def parsedEstructuraRutas(self, depot, token, ruc_empresa):
        # Extraemos de Nimbus todas las rutas que pertenecen a la empresa segun filtro por token y depot  
        raw = self.parsedConsumirRutas(depot, token)

        # Luego de extraer las rutas las listamos guardando en un diccionario solo el nombre y los puntos que pertenecen a esa ruta
        # Ejemplo de como vienen los datos [{'nombre': 'RUTA08', 'puntosC': [334153, 334154, 398253, 334155, 334156, 334157, 334158, 334159, 334160, 398252, 334161]},{...}]
        rutas = self.listaRutas(raw)

        # Extraemos todos los puntos que pertenecen a la empresa segun filtro token y depot
        puntos = self.consumirPuntos(depot,token)
        
        estructura = []
        contador =0
        # Creamos un bucle segun la cantidad de rutas en la lista "rutas"
        while contador<len(rutas):
            enviarRuta = {}
            # Extraemos los puntos de control de la ruta
            puntosRuta = rutas[contador]['puntosC']

            # Llamamos al metodo parsedParadasInicioFin que nos retornara un diccionario con el nombre de pc inicio y fin
            namespc = self.parsedParadasInicioFin(puntos, puntosRuta)

            SM_RUC_PROVEEDOR = "1716024474001"
            SM_RUC_EMPRESA= ruc_empresa
            SM_CODIGO_RUTA = rutas[contador]['nombre']
            SM_NOMBRE= namespc['inicio'] + " - " + namespc['fin']
            # Llamamos al metodo obtenerCoordenadas que nos retornara un string con todas las coordenadas concatenadas
            SM_COORDENADAS = self.obtenerCoordenadas(puntos,puntosRuta)
            SM_ESTADO = "A"

            enviarRuta['SM_RUC_PROVEEDOR']=SM_RUC_PROVEEDOR
            enviarRuta['SM_RUC_EMPRESA']=SM_RUC_EMPRESA
            enviarRuta['SM_CODIGO_RUTA']=SM_CODIGO_RUTA
            enviarRuta['SM_NOMBRE']= SM_NOMBRE
            enviarRuta['SM_COORDENADAS']=SM_COORDENADAS
            enviarRuta['SM_ESTADO']=SM_ESTADO

            #Una vez terminado el diccionario con toda la estructura lista la agregamos a la lista estrctura
            estructura.append(enviarRuta)
            contador += 1
        estructuraf=json.dumps(estructura)
        return estructuraf

    def parsedConsumirRutas(self, depot, token):
        headers={
            "Authorization":f"Token {token}"
            }
        response = requests.get(f'https://nimbus.wialon.com/api/depot/{depot}/routes', headers=headers)
        raw = response.json()
        return raw

    def listaRutas(self, raw):
        listaRutas = []
        # Recorremos las rutas para extraer solo el nombre e id de sus puntos de control
        for r in raw['routes']:
            rutas = {}
            puntos = []
            rutas['nombre']= r['n']
            # Dentro de la ruta recorremos r['t'] que contiene la lista de pc
            for p in r['st']:
                puntos.append(p['id']) # Extraemos id de pc
            rutas['puntosC']=puntos
            listaRutas.append(rutas)
        return listaRutas

    def consumirPuntos(self, depot, token):
        headers={
            "Authorization":f"Token {token}"
            }
        response = requests.get(f'https://nimbus.wialon.com/api/depot/{depot}/stops', headers=headers)
        raw = response.json()    
        puntos=raw['stops']        
        
        return puntos

    def obtenerCoordenadas(self, puntos, puntosRuta):    
        coordenadas=""
        # Recorremos los puntos c
        for p in puntos:
            # Comparamos el id de los puntos de toda la empresa con nuestra lista que solo contiene el id de los puntos de la ruta que queremos analizar
            if p['id'] in puntosRuta:
                # Si cumple la condicion guardamos su p['p'] que contendra la lista con las coordenadas del pc
               listcoord = p['p']
               for l in listcoord:
                    coordenadas = "("+str(l['y'])+","+str(l['x'])+"),"+coordenadas
        coordenadas = coordenadas[:-1]      
            
        return coordenadas

    def parsedMostrarRutasPuntos(self, depot, token):
        headers={
            "Authorization":f"Token {token}"
            }
        response = requests.get(f'https://nimbus.wialon.com/api/depot/{depot}/routes', headers=headers)
        raw = response.json()
        rutas = self.listaRutas(raw)
        # Muestra solo [{'nombre': 'R. Alime', 'puntosC': [404831, 404832, 404833, 404847, 404848, 404849, 405041]}, {...}]
        return rutas

    def parsedParadasInicioFin(self, puntos, puntosRuta):
        # De puntosRuta estamos recibiendo una lista de id de los pc [404831, 404832, 404833, 404847, 404848, 404849, 405041]
        puntoinicio = puntosRuta[0]
        # Agarramos el primer y ultimo id
        puntofin= puntosRuta[-1]
        names = {}
        for p in puntos:
            #Recorremos todos los puntos de la empresa y donde coincida el id del primer o ultimo pc, extraemos su nombre
            if(p['id']==puntoinicio):
                names['inicio']=p['n']
            elif(p['id']==puntofin):
                names['fin']=p['n']
        return names