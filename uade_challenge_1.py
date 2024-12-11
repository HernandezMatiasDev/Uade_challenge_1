import random
import time
jugadoras = [
    ("Argentina", 7, "Carla Rebecchi"),
    ("Argentina", 19, "Delfina Merino"),
    ("Argentina", 3, "Florencia Habif"),
    ("Argentina", 2, "María Noel Barrionuevo"),
    ("Argentina", 14, "Lucina von der Heyde"),
    ("Argentina", 1, "Belen Succi"),
    ("Argentina", 15, "Rocio Sanchez Moccia"),
    ("Argentina", 4, "Victoria Sauze"),
    ("Argentina", 17, "Agustina Albertario"),
    ("Argentina", 5, "Sofia Toccalino"),
    ("Argentina", 9, "Valentina Costa Biondi"),
    ("Argentina", 10, "Agustina Gorzelany"),
    ("Argentina", 6, "Victoria Miranda"),
    ("Argentina", 8, "Bianca Donati"),
    ("Argentina", 11, "Priscila Jardel"),
    ("Argentina", 12, "Celina Di Santo"),
    ("Australia", 16, "Jodie Kenny"),
    ("Australia", 27, "Emily Smith"),
    ("Australia", 10, "Karri McMahon"),
    ("Australia", 8, "Jane Claxton"),
    ("Australia", 7, "Grace Stewart"),
    ("Australia", 4, "Gabrielle Nance"),
    ("Australia", 13, "Amy Lawton"),
    ("Australia", 2, "Brooke Peris"),
    ("Australia", 5, "Savannah Fitzpatrick"),
    ("Australia", 17, "Edwina Bone"),
    ("Australia", 23, "Madison Fitzpatrick"),
    ("Australia", 20, "Maddy Fitzpatrick"),
    ("Australia", 26, "Kaitlin Nobbs"),
    ("Australia", 3, "Sophie Taylor"),
    ("Australia", 12, "Georgia Wilson"),
    ("Australia", 11, "Rebecca Greiner"),
    ("Australia", 19, "Emma de Broughe"),
    ("Australia", 18, "Lily Brazel"),
    ("Australia", 24, "Kaitlin Knobs"),
    ("Australia", 22, "Sophie Taylor"),
    ("Australia", 21, "Georgia Wilson"),
    ("Australia", 14, "Rebecca Greiner"),
    ("Australia", 15, "Emma de Broughe"),
    ("Australia", 25, "Lily Brazel"),
    ("Australia", 29, "Kaitlin Knobs"),
    ("Argentina", 21, "Florencia Mutio"),
    ("Argentina", 22, "Agustina Fernández"),
    ("Argentina", 23, "Agustina Gorzelany"),
    ("Argentina", 24, "Sofía Maccari"),
    ("Argentina", 25, "María Emilia Forcherio"),
    ("Argentina", 26, "Agustina Gorzelany"),
    ("Argentina", 27, "Paula Ortiz"),
    ("Argentina", 28, "Micaela Retegui"),
    ("Argentina", 29, "Valentina Raposo"),
    ("Argentina", 30, "Sofía Toccalino")
]

with open("jugadas.txt", "w") as archivo:
    for i in range(50000):
        jugadora = random.choice(jugadoras)
        acerto_el_pase = random.randint(0, 1)
        minuto = random.randint(1, 90)
        pase_info = jugadora[0]+";"+str(jugadora[1])+";"+jugadora[2] +";"+ str(acerto_el_pase)+";" + str(minuto)
        archivo.write(pase_info + '\n')


