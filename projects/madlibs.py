lang = int(input("Limba/Language:\n1 Romana\n2 English\n"))
if lang == 1:
    print("Hai sa construim o poveste impreuna! Va trebui sa alegi pe rand cate un substantiv, adjectiv sau verb.")
    adjectiv1 = input("Adjectiv: ")
    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    substantiv1 = input("Substantiv: ")
    verb3 = input("Verb: ")
    adjectiv2 = input("Adjectiv: ")
    substantiv2 = input("Substantiv: ")
    mesaj = f"Afara este o zi {adjectiv1}. Pasarile {verb1} pe intinderea cerului insorit. In casa pisicile {verb2} toata ziua. Totusi s-a intamplat sa ti se strice {substantiv1}, asa ca ai decis sa {verb3}. Acolo totul a fost {adjectiv2}. Si cam aceasta a fost {substantiv2}."
    print(mesaj)
    # Primul exemplu: Afara este o zi sportiva. Pasarile s-au omorat pe intinderea cerului insorit. In casa pisicile au taiat toata ziua. Totusi s-a intamplat sa ti se strice incarcatorul, asa ca ai decis sa alergi. Acolo totul a fost galagios. Si cam aceasta a fost masa
else:
    print("Let's build a story together! You'll have to choose one by one a substantive, adjective or verb.")
    adjective1 = input("Adjective: ")
    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    substantive1 = input("Substantive: ")
    verb3 = input("Verb: ")
    adjective2 = input("Adjective: ")
    substantive2 = input("Substantive: ")
    mesaj = f"Outside is a {adjective1} day. The birds {verb1} on the sunny sky. The cats {verb2} in house all the day. However it happen to broken your {substantive1}, so you decided to {verb3}. There everything were {adjective2}. And that was the {substantive2}."
    print(mesaj)
    # Outside is a hot day. The birds run on the sunny sky. The cats joy in house all the day. However it happen to broken your heart, so you decided to bite. There everything were strong. And that was the hand.
    