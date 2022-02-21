from kompositsioon.Aknad_ja_Uksed import Aknad_ja_Uksed




class Tuba():
    def __init__(self, pikkus, laius, korgus):
        self.aknad_uksed = []
        self.laius = laius
        self.korgus = korgus
        self.pikkus = pikkus
    def pindalad(self):
        pindalad = 2 * self.korgus * (self.pikkus + self.laius)
        return pindalad
    def tappedi_rull(self, pikkus,laius):
        self.tappedi_rull1 = pikkus * laius
        self.tappedi_rull = self.toapindala() / self.tappedi_rull1
    def Lisa_Aknad_Uksed(self, au_laius, au_korgus):
        self.aknad_uksed.appened(Aknad_ja_Uksed(au_laius, au_korgus))
    def toopindala(self):
        uus_pindala = self.pindala(self.pikkus, self.laius, self.korgus)
        for element in self.aknad_uksed:
            uus_pindala = uus_pindala - element.pindala
        return uus_pindala