from paquete.cinema import Cinema
from paquete.regularticket import RegularTicket
from paquete.vipticket import VIPTicket
#%%
theater = Cinema(100, 100)
theater.buyTicket()

cuenta = input("Desea crear una cuenta?")
if cuenta == "si":
    nombre = input("Cual es su nombre?")
    pref = input("Que preferencia de asiento tiene?")
    print(f"Se guardara su preferencia {pref}")

