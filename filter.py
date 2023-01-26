leden = {"lid 1":{"naam":"John","stad":"Amsterdam"},
         "lid 2":{"naam":"Anne","stad":"Utrecht"},
         "lid 3":{"naam":"Lisa","stad":"Groningen"},
         "lid 4":{"naam":"Mark","stad":"Dordrecht"},
         "lid 5":{"naam":"Frank","stad":"Rotterdam"},
         "lid 6":{"naam":"Peter","stad":"Eindhoven"}
         }

filter = {}
def toon_filter():
    print("--------------------------------------------------")
    print("ID","\t\t","Naam","\t","stad")
    print("--------------------------------------------------")

    for id,lid in filter.items():#buiten
        print(id,end="\t")
        for info in lid.values():#binnen
            print(info,end="\t\t")
        print("")
    print("--------------------------------------------------")

    
def toon_leden():
    print("--------------------------------------------------")
    print("ID","\t\t","Naam","\t","stad")
    print("--------------------------------------------------")

    for id,lid in leden.items():#buiten
        print(id,end="\t")
        for info in lid.values():#binnen
            print(info,end="\t\t")
        print("")
    print("--------------------------------------------------")

    
def toon_leden_uit():
    filter.clear()
    stad = input("van welke stad wil je de leden")
    for id,lid in leden.items():
            if lid["stad"] == stad:
                filter.update({id:{"naam":lid["naam"],"stad":lid["stad"]}})
    toon_filter()

toon_leden()
toon_leden_uit()
