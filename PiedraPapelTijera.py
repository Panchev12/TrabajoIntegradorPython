while True:
    a = int(input("Jugador 1: 1=Piedra, 2=Papel, 3=Tijeras: "))
    b = int(input("Jugador 2: 1=Piedra, 2=Papel, 3=Tijeras: "))

    if a == 1 and b == 3:
        print('Jugador 1 Gana: Piedra gana a Tijera')
    elif a == 2 and b == 1:
        print('Jugador 1 Gana: Papel gana a Piedra')
    elif a == 3 and b == 2:
        print('Jugador 1 Gana: Tijeras gana a Papel')
    elif b == 1 and a == 3:
        print('Jugador 2 Gana: Piedra gana a Tijera')
    elif b == 2 and a == 1:
        print('Jugador 2 Gana: Papel gana a Piedra')
    elif b == 3 and a == 2:
        print('Jugador 2 Gana: Tijeras gana a Papel')
    else:
        print('Ninguno gana')