kinderen = {"kind_1":{"naam":"Inge","Leeftijd":12},
            "kind_2":{"naam":"Pieter","Leeftijd":10},
            "kind_3":{"naam":"Lander","Leeftijd":8}
            }


def voeg_kind_toe():
    id = "kind_"+str(len(kinderen)+1)
    naam_kind = input("geef de naam van het kind")
    leeftijd_kind = int(input("geef de leeftijd van het kind"))
    kinderen.update({id:{"naam":naam_kind,"Leeftijd":leeftijd_kind}})


def voeg_kinderen_toe():
    invoer = input("wil je nog een kind toevoegen")
    if invoer == "ja" or invoer == "nee":
        while not invoer == "nee":
            voeg_kind_toe()
            invoer = input("wil je nog een kind toevoegen")


def wijzig_leeftijd():
    toon_kinderen()
    id = input("geef het id van het kind waarvan we de leeftijd willen veranderen")
    if id in kinderen:
        nieuwe_leeftijd = int(input("geef de nieuwe leeftijd in"))
        kinderen[id]["Leeftijd"] = nieuwe_leeftijd


def geef_zakgeld():
    for kind in kinderen.values():
        kind["zakgeld"] = 20
        
        
def verhoog_zakgeld():
    for kind in kinderen.values():
        kind["zakgeld"] = kind["zakgeld"]+kind["Leeftijd"]


def toon_kinderen():
    print("--------------------------------------------------")
    print("ID","\t\t","Naam","\t","leeftijd","\t","zakgeld")
    print("--------------------------------------------------")

    for id,kind in kinderen.items():#buiten
        print(id,end="\t")
        for info in kind.values():#binnen
            print(info,end="\t\t")
        print("")
    print("--------------------------------------------------")

#wijzig_leeftijd()
toon_kinderen()
geef_zakgeld()
toon_kinderen()
verhoog_zakgeld()
toon_kinderen()
