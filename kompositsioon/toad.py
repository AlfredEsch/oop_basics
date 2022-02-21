from kompositsioon.Tuba import Tuba
tuba = Tuba(int(input("sisestage toa pikkus" )), int(input("sisestage toa laius")), int(input("sisestage toa korgus")))
tuba.lisa_aknad_uks(input("sisestage ukse laius")), int(input("sisestage ukse korgus")))
valik = input("kas toas on aknaid? yes/no")
if valik == "yes":
while kordamine == True:
    tuba.lisa.aknad_uks(input("Sisestage akna laius" )), int(input("Sisestage akna korgus"))

tuba.tapendi_rull(int(input("Sisestage tapeedi rulli laius ")), int(input("Sisestage tapeedi rulli pikkus")))
print("Tapeetil on vaja {0} m2, mis on {1} rull".format(tuba.toopindala()), round(tuba.tappedi_rull))
