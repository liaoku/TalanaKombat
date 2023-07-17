# TalanaKombat

Talana Kombar, simula un combate desde un Json

## Requisitos
- Docker o python 3.8.10

## Uso python

- clona el proyecto
- crea un enviroment "python -m venv venv"
- instala las dependencias "pip install -r .\requirements.txt"
- ejecuta el combate con el siguiente comando "python .\Main.py -f entrada.json"
- tambien puedes ejecutarlo enviando directamente el json de esta forma "python .\Main.py -c '{\\"player1\\":{\\"movimientos\\":[\\"D\\",\\"DSD\\",\\"S\\",\\"DSD\\",\\"SD\\"],\\"golpes\\":[\\"K\\",\\"P\\",\\"\\",\\"K\\",\\"P\\"]},\\"player2\\":{\\"movimientos\\":[\\"SA\\",\\"SA\\",\\"SA\\",\\"ASA\\",\\"SA\\"],\\"golpes\\":[\\"K\\",\\"\\",\\"K\\",\\"P\\",\\"P\\"]}}'"

## Uso docker
- crea el docker "docker build -t < nombre repo > ."
- ejecuta "docker run --rm < nombre repo > -f entrada.json"
- tambien puedes ejecutarlo enviando directamente el json de esta forma "docker run --rm < nombre repo > -c '{\\"player1\\":{\\"movimientos\\":[\\"D\\",\\"DSD\\",\\"S\\",\\"DSD\\",\\"SD\\"],\\"golpes\\":[\\"K\\",\\"P\\",\\"\\",\\"K\\",\\"P\\"]},\\"player2\\":{\\"movimientos\\":[\\"SA\\",\\"SA\\",\\"SA\\",\\"ASA\\",\\"SA\\"],\\"golpes\\":[\\"K\\",\\"\\",\\"K\\",\\"P\\",\\"P\\"]}}'"


##Uso rápido

- está disponible de forma publica el docker "liaoku/talana" descarga el archivo entrada.json y ejecutalo con el siguiente comando "docker run --rm liaoku/talana -f entrada.json" (si no hace el pull solo Just do it "docker pull liaoku/talana")