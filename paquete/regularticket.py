from paquete.aticket import ATicket
from typing import Optional, Iterable, Iterator, cast
class RegularTicket(ATicket):
    def __init__(self, movie:str, cuando:int, donde:str) -> None:
        super().__init__()
        self.movie = movie
        self.cuando = cuando
        self.donde = donde 
    
    @property
    def movie(self):
        print("Getting value...")
        return self._movie

    @movie.setter
    def movie(self, value):
        print("Setting value...")
        self._movie = value

    @property
    def cuando(self):
        print("Getting value...")
        return self._movie

    @cuando.setter
    def cuando(self, value):
        print("Setting value...")
        self._cuando = value