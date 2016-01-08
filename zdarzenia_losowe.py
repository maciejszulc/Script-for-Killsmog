from random import randint

transport = [
"pojechales do pracy tramwajem, +1 zl, -1 do smogu",
"jedziesz rowerem +1 zdrowia",
"poszedles na spacer +1 do zdrowia",
"wziales udzial w maratonie +2 do zdrowia, -1 do smogu",
"jedziesz samochodem +1 do smogu",
"stoisz w korku. Tracisz jedna ture.",
"Kupujesz bilet miesieczny. -2 zl, - 1 smogu, +1 zdrowia",

]

pogoda = [
"wieje wiatr. -2 smogu",
"idzie zima. ludzie pala w piecach. +2 smogu",
"spadl deszcz. -1 smogu",
"mgla. smog narasta. +2 do smogu",
"idzie lato. -1 smogu",
"mroz. ludzie grzeja wszystkim, co maja. +2 smogu",
"wieje wiatr. -1 smogu",

]


szansa = [
"W Twojej okolicy zrobiono nasadzenia. Poziom smogu obniza sie. -2 smogu",
"Kupiles maske antysmogowa. -1 zl +1 zdrowia",
"Dostales dotacje. +10 zl",
"Cofasz sie o 4 pola. Wykonujes intrukcje pola, na ktore sie udajesz.",
"Przez smog zachorowales na astme. -2 zdrowia; tracisz 1 ture.",
"Miasto Krakow wsparlo Twoje starania o wymiane pieca. Zamien 1 ze swoich domow na dom ogrzewany przez MPEC.",
"Postanowiles pozbyc sie paru zbednych rzeczy poprzez spalenie ich. +2 smogu",
"Wspomogles babcie w przylaczeniu sie do ogrzewania miejskiego. Zamien jeden ze swoich domow na dom MPEC.",
"Trzesienie ziemi. Placisz 1 zl za kazdy posiadany dom.",
"Po latach pracy udalo Ci sie zarobic na nowy dom. Zamien jeden ze swoich domkow na dom eko.",
"Odziedziczyles kamienice. Dostajesz dwa domki ogrzewane weglem.",
"Doszlo do wycinki parku w Twojej okolicy. +2 smogu",
"Zabudowano korytarze powitrzne w Twojej okolicy. Stojace powietrze nasila dramatycznie smog. +3 smogu",
"Poszedles na basen. +1 zdrowia",
"Wprowadzono zakaz palenia weglem. Za kazdy domek opalany smieciami placisz 2 zl kary; za kazdy dom \nopalany weglem 1 zl kary.",
"Bedac w Wieliczce poodychales czystym powietrzem w kopalni soli. -1 zl, +1 zdrowia",
"Dzis jest wyjatkowo gesty smog. W zwiazku z tym, zostajesz w omu. tracisz jedna ture.",
"Remontujesz swoje domy. -1 zl za kazdy dom",
"Gigantyczny smog zaczal odstraszac turystow. -2 zl",
"Znalazles pieniadze w okolicach Rynku. +1 zl",
"Patrol Strazy Miejskiej. Za kazdy dom ogrzewany smieciami placisz mandat w wysokosci 2 zl. Jezeli nie masz takiej ilosci \npiniedzy, sad skazuje Cie na areszt - tracisz 2 tury.",

]


# A function that uses the lists from above to print a random event

def question():

    print "Ponizej wpisz rodzaj pola na ktorym stoisz. Jezeli gra sie skonczyla, wpisz 'koniec gry'."

    while True:
        print "Na jakim polu stoisz?"
        answer = raw_input("> ")
        if answer == "transport":
            print transport[randint(0, len(transport)-1)]
        elif answer == "pogoda":
            print pogoda[randint(0, len(pogoda)-1)]
        elif answer == "szansa":
            print szansa[randint(0, len(szansa)-1)]
        elif answer == "koniec gry":
            return False
        elif answer == "Szansa":
            print szansa[randint(0, len(szansa)-1)]
        elif answer == "Pogoda":
            print pogoda[randint(0, len(pogoda)-1)]
        elif answer == "Transport":
            print transport[randint(0, len(transport)-1)]
        else:
            print "Nie rozumiem"


question()
