from aticket import ATicket

class VIPTicket(ATicket):
    def __init__(self, movie:str, cuando:int, donde:str) -> None:
        super().__init__()
        self.movie = movie
        self.cuando = cuando
        self.donde = donde 