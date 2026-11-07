from varasto import Varasto


def testaa_getterit(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def testaa_setterit(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")


def testaa_virhetilanteet(mehua, olutta):
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

    olutta.lisaa_varastoon(1000.0)
    mehua.lisaa_varastoon(-666.0)
    olutta.ota_varastosta(1000.0)
    mehua.ota_varastosta(-32.9)


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

    testaa_getterit(olutta)
    testaa_setterit(mehua)
    testaa_virhetilanteet(mehua, olutta)

    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")


if __name__ == "__main__":
    main()
