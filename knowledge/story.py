from logic import *

# - Herkes bir tane eşya almıştır.
# - Elif perde almamıştır.
# - Mehmet veya Selim buzdolabi almistir.
# - Mehmet perde veya buzdolabi almistir.
# - Ahmet TV almıştır.

people = ["Mehmet", "Elif", "Ahmet", "Selim"]
stuff = ["hali", "perde", "tv", "buzdolabi"]
symbols = []

for person in people:
    for object in stuff:
        symbols.append(Symbol(f"{person} {object} almistir"))

knowledge = And()

#her biri icin bir esya 
for person in people:
    for object1 in stuff:
        for object2 in stuff:
            if object1 != object2:
                knowledge.add(
                    Implication(Symbol(f"{person} {object1} almistir"), Not(Symbol(f"{person} {object2} almistir")))
                )

#her bir esya icin bir kisi
for object in stuff:
    for p1 in people:
        for p2 in people:
            if p1 != p2:
                knowledge.add(
                    Implication(Symbol(f"{p1} {object} almistir"), Not(Symbol(f"{p2} {object} almistir")))
                )

knowledge.add(
    Or(Symbol("Mehmet buzdolabi almistir"), Symbol("Selim buzdolabi almistir"))
)

knowledge.add(
    Or(Symbol("Mehmet buzdolabi almistir"), Symbol("Mehmet perde almistir"))
)

knowledge.add(
    Not(Symbol("Elif perde almistir"))
)

knowledge.add(
    Not(Symbol("Elif buzdolabi almistir"))
)

knowledge.add(
    Symbol("Ahmet tv almistir")
)

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)

