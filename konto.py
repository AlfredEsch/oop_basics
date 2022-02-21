class konto():
    def __init__(self, nimi, saldo):
        self.nimi  =  nimi
        self.saldo = saldo

    def deposiit(self, kogus):
        if kogus > 0:
            self.__saldo += kogus
        else:
            print("sisestage positiivne summa! ")

    def ylekanne(self, amount):
        if amount > 0:
            self.saldo -= amount
        else:
            print("sisestage positiivne summa! ")