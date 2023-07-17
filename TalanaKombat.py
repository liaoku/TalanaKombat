
import json
from Personaje import Personaje



class TalanaKombat:
    player1 = Personaje("Tonyn")
    player2 = Personaje("Arnaldor")
    historial:list    
    def __init__(self):
        historial = []
        
        
    def intercalar_listas(self, lista1, lista2):
        resultado = []
        largo = max(len(lista1), len(lista2))
        for i in range(largo):
            if(i < len(lista1)):
                resultado.append(lista1[i])
            if(i < len(lista2)):
                resultado.append(lista2[i])
        return resultado
        
    def movimientos_players(self, combinaciones:str):
        combate = json.loads(combinaciones)
        self.player1.contar_golpes(combate["player1"]["golpes"])
        self.player1.contar_movimientos(combate["player1"]["movimientos"])
        self.player2.contar_golpes(combate["player2"]["golpes"])
        self.player2.contar_movimientos(combate["player2"]["movimientos"])
        
        largop1 = max(len(combate["player1"]["movimientos"]), len(combate["player1"]["golpes"]))
        
        for p1 in range(largop1):
            if(p1 < len(combate["player1"]["golpes"]) and p1 < len(combate["player1"]["movimientos"])):
                self.player1.movimientos_a_golpe(combate["player1"]["movimientos"][p1]+" + "+combate["player1"]["golpes"][p1])
            else:
                if(p1 >= len(combate["player1"]["golpes"])):
                    self.player1.movimientos_a_golpe(combate["player1"]["movimientos"][p1])
                if(p1 >= len(combate["player1"]["movimientos"])):
                    self.player1.movimientos_a_golpe(combate["player1"]["golpes"][p1])
            
            
        self.player2.historial_movimientos = []
        
        largop2 = max(len(combate["player2"]["movimientos"]), len(combate["player2"]["golpes"]))
        for p2 in range(largop2):
            if(p2 < len(combate["player2"]["golpes"]) and p2 < len(combate["player2"]["movimientos"])):
                self.player2.movimientos_a_golpe(combate["player2"]["movimientos"][p2]+" + "+combate["player2"]["golpes"][p2])
            else:
                if(p2 >= len(combate["player2"]["golpes"])):
                    self.player2.movimientos_a_golpe(combate["player2"]["movimientos"][p2])
                if(p2 >= len(combate["player2"]["movimientos"])):
                    self.player2.movimientos_a_golpe(combate["player2"]["golpes"][p2])

    
    def quien_inicia_combate(self):
        parte_payer1 = None
        primer_combate = []
        if(self.player1.conteo_movimientos == self.player2.conteo_movimientos and self.player1.conteo_golpes==self.player2.conteo_golpes):
            parte_payer1 = True
            primer_combate = self.intercalar_listas(self.player1.historial_movimientos, self.player2.historial_movimientos)
            print("Inicia player 1")
        if(parte_payer1==None and (self.player1.conteo_movimientos+self.player1.conteo_golpes) < (self.player2.conteo_movimientos + self.player2.conteo_golpes)):
            parte_payer1 = True
            primer_combate = self.intercalar_listas(self.player1.historial_movimientos, self.player2.historial_movimientos)
            print("Inicia player 1")
        if(parte_payer1==None and (self.player1.conteo_movimientos+self.player1.conteo_golpes) > (self.player2.conteo_movimientos + self.player2.conteo_golpes)):
            parte_payer1 = False
            primer_combate = self.intercalar_listas(self.player2.historial_movimientos, self.player1.historial_movimientos)
            print("Inicia player 2")
        if(parte_payer1==None and (self.player1.conteo_movimientos) < (self.player2.conteo_movimientos)):
            parte_payer1 = True
            print("Inicia player 1")
            primer_combate = self.intercalar_listas(self.player1.historial_movimientos, self.player2.historial_movimientos)
        if(parte_payer1==None and (self.player1.conteo_movimientos) > (self.player2.conteo_movimientos)):
            parte_payer1 = False
            print("Inicia player 2")
            primer_combate = self.intercalar_listas(self.player2.historial_movimientos, self.player1.historial_movimientos)
        if(parte_payer1==None and (self.player1.conteo_golpes) < (self.player2.conteo_golpes)):
            parte_payer1 = True
            print("Inicia player 1")
            primer_combate = self.intercalar_listas(self.player1.historial_movimientos, self.player2.historial_movimientos)
        if(parte_payer1==None and (self.player1.conteo_golpes) > (self.player2.conteo_golpes)):
            parte_payer1 = False
            print("Inicia player 2")
            primer_combate = self.intercalar_listas(self.player2.historial_movimientos, self.player1.historial_movimientos)
        if(parte_payer1==None):
            parte_payer1 = True
            print("Inicia player 1")
            primer_combate = self.intercalar_listas(self.player1.historial_movimientos, self.player2.historial_movimientos)
        return parte_payer1, primer_combate
    
    def verificar_json(self, combinaciones:str):
        try:
            combate = json.loads(combinaciones)
            for p1 in combate["player1"]["movimientos"]:
                if(len(p1)>5):
                    return False, "La combinacion de movimientos no puede ser mayor a 5"
            for p2 in combate["player2"]["movimientos"]:
                if(len(p2)>5):
                    return False, "La combinacion de movimientos no puede ser mayor a 5"
            for p1 in combate["player1"]["golpes"]:
                if(len(p1)>1):
                    return False, "La combinacion de golpes puede ser máximo 1"
            for p2 in combate["player2"]["golpes"]:
                if(len(p2)>1):
                    return False, "La combinacion de golpes puede ser máximo 1"
        except:
            return False, "No es un json valido"
        return True, "Json valido"
       
    
    def simular_combate(self, combinaciones:str):
        varificacion, mensaje = self.verificar_json(combinaciones)
        if(not varificacion):
            print(mensaje)
            return
        self.movimientos_players(combinaciones)
        parte_player1, primer_combate = self.quien_inicia_combate()        
        
        self.correr_combate(parte_player1, self.player1.historial_movimientos, self.player2.historial_movimientos)
        #self.imprimir_combate(parte_player1, primer_combate)

    def realizar_ataque(self,combate:list, hist:str):
        at =list(combate)[::-1]
        realiza_accion = False
        energia_ataque = 0
        for ata in at:
            if(ata != None):
                hist = hist +  ata.mensaje+" y "
                realiza_accion = True
                energia_ataque += ata.energia
        if(not realiza_accion):
            hist = hist + "se mueve  "
        print(hist[:-2])
        return energia_ataque
    
    def verificar_salud(self):
        if(self.player1.energia<=0):
            print(self.player2.nombre+" gana la pelea y aun le queda "+str(self.player2.energia)+" de energia")
            return False
        if(self.player2.energia<=0):
            print(self.player1.nombre+" gana la pelea y aun le queda "+str(self.player1.energia)+" de energia")
            return False
        return True
    
    def correr_combate(self, parte_payer1:bool ,combate_p1:list, combate_p2:list):
        largo = max(len(combate_p1), len(combate_p2))
        for i in range(largo):
            if(parte_payer1):
                if(i < len(combate_p1)):
                    hist  = self.player1.nombre + " "
                    energia_ataque = self.realizar_ataque(combate_p1[i], hist)
                    self.player2.energia  = self.player2.energia - energia_ataque
                    continuar = self.verificar_salud()
                    if(not continuar):
                        break
                    
                if(i < len(combate_p2)):
                    hist  = self.player2.nombre + " "
                    energia_ataque = self.realizar_ataque(combate_p2[i], hist)
                    self.player1.energia  = self.player1.energia - energia_ataque
                    continuar = self.verificar_salud()
                    if(not continuar):
                        break
            else:  
                if(i < len(combate_p2)):
                    hist  = self.player2.nombre + " "
                    energia_ataque = self.realizar_ataque(combate_p2[i], hist)
                    self.player1.energia  = self.player1.energia - energia_ataque
                    continuar = self.verificar_salud()
                    if(not continuar):
                        break
                
                if(i < len(combate_p1)):
                    hist  = self.player1.nombre + " "
                    energia_ataque = self.realizar_ataque(combate_p1[i], hist)
                    self.player2.energia  = self.player2.energia - energia_ataque
                    continuar = self.verificar_salud()
                    if(not continuar):
                        break
        if(self.player1.energia>0 and self.player2.energia>0):
            print("La pelea termina en empate con "+str(self.player1.energia)+" de energia para "+self.player1.nombre+" y "+str(self.player2.energia)+" de energia para "+self.player2.nombre)
                
       
