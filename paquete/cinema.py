from paquete.regularticket import RegularTicket
from paquete.vipticket import VIPTicket
class Cinema:
    """
    Clase del teatro que corre las peliculas
    """
    def __init__(self, seats, vipseats) -> None:
        self.normalseats = seats
        self.vipseats = vipseats
        self.cuentas = []
        self.tickets = []

    def buyTicket(self) -> None:
        """
        Correr toda la logica de comprar los tiquetes.
        Pedir informacion al usuario
        """
        print("Bienvenido al cine")
        try:
            cantidad = input("Cuantos ticketes desea?")
            cantidad = int(cantidad)
        except ValueError:
            print("Debe introducir un numero de ticketes")
        print(f"Seran {cantidad} asientos")
        print("En que posicion desea los asientos?")
        donde = input("Debe ser frente o atras")
        if(donde == "frente"):
            print("Se sentaran al frente")
        elif donde == "atras":
            print("Se sentaran atras")
        else:
            raise ValueError("Solo se puede ubicar al frente o atras")
        
        print("Que pelicula desea ver?")
        cual = input("Tiburones o asesinos?")
        if(donde == "tiburones"):
            print("Veran Tiburones")
        elif donde == "asesinos":
            print("Veran Asesinos")
        else:
            raise ValueError("Solo puede escoger entre las peliculas para ver")

        try:
            cuando = int(input("A que hora desea ver la pelicula?"))
        except ValueError:
            print("La hora debe ser un numero hasta las 12 de la noche")
        
        try:
            cuanto = int(input("Cuantos tiquetes desea?"))
        except ValueError:
            print("Debe ser una cantidad positiva")

        vip = input("Desea tickete vip?")
        for i in range(cuanto):
            if vip == "si":
                ticket = VIPTicket(cual, cuando, donde)
                self.tickets.append(ticket)
                self.vipseats -= 1
            else:
                ticket = RegularTicket(cual, cuando, donde)
                self.tickets.append(ticket)
                self.normalseats -= 1

    def crearCuenta(self, pref, nombre) -> None:
        """
        Crear cuenta al usuario con preferencias
        """
        self.cuentas.append((nombre, pref))