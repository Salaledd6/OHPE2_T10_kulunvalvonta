avaimet = {123: ["A2", "A3"],
           124: ["A1"],
           125: ["A1", "A2", "A3"]}

aluuet = {"A1": ["A110", "A120", "A130", "A140"],
          "A2": ["A210", "A220", "A230", "A240"],
          "A3": ["A310", "A320", "A330", "A340"]}

tarkistettava_avain = int(input("Syötä avaimen id > "))
tarkistettava_tila = input("Syötä tilan tunnus > ")
avataan = False

avaimen_alueet = avaimet[tarkistettava_avain]
print(avaimen_alueet) # jos avain 125, niin ["A1", "A2", "A3"]

for alue in avaimen_alueet:
    if tarkistettava_tila in aluuet[alue]:
        avataan = True
    else:
        break

if avataan:
    print("Avataan")
else:
    print("Ei pääsyä")