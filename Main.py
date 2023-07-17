from TalanaKombat import TalanaKombat

import argparse

parser = argparse.ArgumentParser(description='Descripción de tu script')

parser.add_argument('-c', '--combate', type=str, help='Json de combate a simular')
parser.add_argument('-f', '--file', type=argparse.FileType('r'), help='Archivo de entrada')

args = parser.parse_args()

valor_combate = args.combate
if args.file:
    file = args.file.read()

    valor_combate = file


juego = TalanaKombat()
juego.simular_combate(str(valor_combate))