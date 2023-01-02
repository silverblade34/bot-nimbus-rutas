from datetime import datetime
from time import gmtime, strftime

import json
import requests 

class ResponseBot():
    def __init__(self):
        pass

    def parsedConsumirNimbus(self, depot, token,ruc_empresa):
        headers={
            "Authorization":f"Token {token}"
            }
        response = requests.get(f'https://nimbus.wialon.com/api/depot/{depot}/routes', headers=headers)
        raw = response.json()
        
        rutas = self.listaRutas(raw)
        puntos = self.consumirPuntos(depot,token)
        
        estructura = []
        contador =0
        while contador<len(rutas):
            enviarRuta = {}
            puntosRuta = rutas[contador]['puntosC']
            
            SM_RUC_PROVEEDOR = "1716024474001"
            SM_RUC_EMPRESA= ruc_empresa
            SM_CODIGO_RUTA = rutas[contador]['nombre']
            SM_NOMBRE= rutas[contador]['nombre']
            SM_COORDENADAS = self.obtenerCoordenadas(puntos,puntosRuta)
            SM_ESTADO = "A"

            enviarRuta['SM_RUC_PROVEEDOR']=SM_RUC_PROVEEDOR
            enviarRuta['SM_RUC_EMPRESA']=SM_RUC_EMPRESA
            enviarRuta['SM_CODIGO_RUTA']=SM_CODIGO_RUTA
            enviarRuta['SM_NOMBRE']=SM_NOMBRE
            enviarRuta['SM_COORDENADAS']=SM_COORDENADAS
            enviarRuta['SM_ESTADO']=SM_ESTADO

            estructura.append(enviarRuta)
            contador += 1
        estructuraf=json.dumps(estructura)
        return estructuraf

    def listaRutas(self, raw):
        listaRutas = []
        for r in raw['routes']:
            rutas = {}
            puntos = []
            rutas['nombre']= r['n']
            for p in r['st']:
                puntos.append(p['id'])
            rutas['puntosC']=puntos
            listaRutas.append(rutas)
        return listaRutas

    def consumirPuntos(self, depot, token):

        # puntosRuta = rutas[0]['puntosC']
        # coordenadas = []
        headers={
            "Authorization":f"Token {token}"
            }
        response = requests.get(f'https://nimbus.wialon.com/api/depot/{depot}/stops', headers=headers)
        raw = response.json()    
        puntos=raw['stops']        
        
        return puntos

    def obtenerCoordenadas(self, puntos, puntosRuta):    
        coordenadas=""
        for p in puntos:
            #listaCoordenadas = []
            if p['id'] in puntosRuta:
               listcoord = p['p']
               for l in listcoord:
                    coordenadas = "("+str(l['y'])+","+str(l['x'])+"),"+coordenadas
        coordenadas = coordenadas[:-1]      
            
        return coordenadas



