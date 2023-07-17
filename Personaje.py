from Movimiento import Movimiento
from typing import List
import json
import os
from dotenv import load_dotenv

load_dotenv()

class Personaje:
    energia:int
    nombre:str
    movimientos:List[Movimiento]
    historial_movimientos = []
    botones_movimientos = ["A", "S", "D", "W"]
    botones_ataques = ["K", "P"]
    conteo_golpes:int
    conteo_movimientos:int
    
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 6
        self.movimientos = []
        self.golpes = []
        self.cargar_movimientos()
        
    def potencia_golpe(self, golpe:str):
        for m in self.movimientos:
            if(m.nombre == golpe):
                return m.energia
        return 0
    
    def imprimir_historial(self):
        print(self.nombre)
        for i in self.historial_movimientos:
            for j in i:
                print(j)
    
    def movimientos_a_golpe(self, combinacion:str) -> list:
        mov = self.str_boton_a_movimiento(combinacion)
        if(mov == None):
            combinacion_separada = combinacion.split("+")
            if(len(combinacion_separada) > 1):
                mov1 = self.str_boton_a_movimiento(combinacion_separada[0])
                mov2 = self.str_boton_a_movimiento(combinacion_separada[1])
                self.historial_movimientos.append({mov1, mov2})
                return 
        self.historial_movimientos.append({mov})
        return {mov}
    
    def es_movimiento(self, combinacion:str) -> bool:
        if(len(combinacion) > 0):
            return(combinacion[0] in self.botones_movimientos)
        return False
    
    def es_ataque(self, combinacion:str) -> bool:
        if(len(combinacion) > 0):
            return(combinacion[0] in self.botones_ataques)
        return False

    def contar_movimientos(self, movimientos:list):
        self.conteo_movimientos = 0
        for i in movimientos:
            if(i != ""):
                self.conteo_movimientos += 1
    def contar_golpes(self, golpes:list):
        self.conteo_golpes = 0
        for i in golpes:
            if(i != ""):
                self.conteo_golpes += 1
       
    def cargar_movimientos(self):
        path = os.getenv("PATH_CONFIGURACIONES")
        with open(path, 'r') as f:
            data = json.load(f)
            
        for p in data["personajes"]:
            if(p["nombre"] == self.nombre):
                for m in p["movimientos"]:
                    mov = Movimiento()
                    mov.combinacion = m["combinacion"]
                    mov.energia = m["energia"]
                    mov.mensaje = m["mensaje"]
                    mov.nombre = m["nombre"]
                    self.movimientos.append(mov)
    def str_boton_a_movimiento(self, combinacion:str)-> Movimiento:
        combinacion = combinacion.strip()
        for m in self.movimientos:
            if(m.combinacion == combinacion):
                return m
        mov = Movimiento()
        botones = os.getenv("BOTONES_MOVIMIENTO").split(',')
        mensajes = os.getenv("MENSAJES_BOTONES_MOVIMIENTO").split(',')
        for i in range(len(botones)):
            if(botones[i] == combinacion):
                mov.combinacion = botones[i]
                mov.mensaje = mensajes[i]
                mov.nombre = botones[i]
                mov.energia = 0
                return mov
        
        return None
                    
