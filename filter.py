leden = {"lid 1":{"naam":"Jann","stad":"genk"},
         "lid 2":{"naam":"Anne","stad":"hasselt"},
         "lid 3":{"naam":"bert","stad":"genk"},
         "lid 4":{"naam":"frank","stad":"hasselt"},
         "lid 5":{"naam":"peter","stad":"genk"},
         "lid 6":{"naam":"karel","stad":"gent"}
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
