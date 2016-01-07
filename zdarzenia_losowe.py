from random import randint
from sys import *




   
def Transport():
        
    happening = randint(0,6)
    if happening == 0:
	    print "pojechales do pracy tramwajem, +1 zl, -1 do smogu"
            
    elif happening == 1:
	    print "jedziesz rowerem +1 zdrowia"
            
    elif happening == 2:
	    print "poszedles na spacer +1 do zdrowia"
            
    elif happening == 3:
	    print "wziales udzial w maratonie +2 do zdrowia, -1 do smogu"
        
    elif happening == 4:
	    print "jedziesz samochodem +1 do smogu"
        
    elif happening == 5:
	    print "stoisz w korku. Tracisz jedna ture."
        
    elif happening == 6:
	    print "Kupujesz bilet miesieczny. -2 zl, - 1 smogu, +1 zdrowia"
        
    else:
	    print "niemozliwe."
            
    question()
        
    
        
        
	
	
	
	
def Pogoda():
    happening = randint(0,6)
    if happening == 0:
	    print "wieje wiatr. -2 smogu"
        
    elif happening == 1:
	    print "idzie zima. ludzie pala w piecach. +2 smogu"
        
    elif happening == 2:
	    print "spadl deszcz. -1 smogu"
       
    elif happening == 3:
	    print "mgla. smog narasta. +2 do smogu"
        
    elif happening == 4:
	    print "idzie lato. -1 smogu"
        
    elif happening == 5:
	    print "mroz. ludzie grzeja wszystkim, co maja. +2 smogu"
       
    elif happening == 6:
	    print "wieje wiatr. -1 smogu"
        
    else:
	    print "niemozliwe."
        
        
    question()
        
		
		
def Szansa():
    happening = randint(0,20)
    if happening == 0:
	   print "W Twojej okolicy zrobiono nasadzenia. Poziom smogu obniza sie. -2 smogu"
    elif happening == 1:
       print "Kupiles maske antysmogowa. -1 zl +1 zdrowia"
    elif happening == 2:
       print "Dostales dotacje. +10 zl"
    elif happening == 3:
       print "Cofasz sie o 4 pola. Wykonujes intrukcje pola, na ktore sie udajesz."
    elif happening == 4:
       print "Przez smog zachorowales na astme. -2 zdrowia; tracisz 1 ture."
    elif happening == 5:
       print "Miasto Krakow wsparlo Twoje starania o wymiane pieca. Zamien 1 ze swoich domow na dom ogrzewany przez MPEC."
    elif happening == 6:
       print "Postanowiles pozbyc sie paru zbednych rzeczy poprzez spalenie ich. +2 smogu"
    elif happening == 7:
       print "Wspomogles babcie w przylaczeniu sie do ogrzewania miejskiego. Zamien jeden ze swoich domow na dom MPEC."
    elif happening == 8:
       print "Trzesienie ziemi. Placisz 1 zl za kazdy posiadany dom."
    elif happening == 9:
       print "Po latach pracy udalo Ci sie zarobic na nowy dom. Zamien jeden ze swoich domkow na dom eko."    
    elif happening == 10:
       print "Odziedziczyles kamienice. Dostajesz dwa domki ogrzewane weglem."
    elif happening == 11:
       print "Doszlo do wycinki parku w Twojej okolicy. +2 smogu"
    elif happening == 12:
       print "Zabudowano korytarze powitrzne w Twojej okolicy. Stojace powietrze nasila dramatycznie smog. +3 smogu"
    elif happening == 13:
       print "Poszedles na basen. +1 zdrowia"
    elif happening == 14:
       print "Wprowadzono zakaz palenia weglem. Za kazdy domek opalany smieciami placisz 2 zl kary; za kazdy dom \nopalany weglem 1 zl kary."
    elif happening == 15:
       print "Bedac w Wieliczce poodychales czystym powietrzem w kopalni soli. -1 zl, +1 zdrowia"
    elif happening == 16:
       print "Dzis jest wyjatkowo gesty smog. W zwiazku z tym, zostajesz w omu. tracisz jedna ture."
    elif happening == 17:       
       print "Remontujesz swoje domy. -1 zl za kazdy dom"
    elif happening == 18:
       print "Gigantyczny smog zaczal odstraszac turystow. -2 zl"
    elif happening == 19:
       print "Znalazles pieniadze w okolicach Rynku. +1 zl"
    elif happening == 20:
       print "Patrol Strazy Miejskiej. Za kazdy dom ogrzewany smieciami placisz mandat w wysokosci 2 zl. Jezeli nie masz takiej ilosci \npiniedzy, sad skazuje Cie na areszt - tracisz 2 tury."
    else:
	   print "niemozliwe."
    
    question()
       
       
       
       
       
def question():
    
    print "Na jakim polu stoisz?"
	
    answer = raw_input("> ")
    
    if answer == "Transport":
        return Transport()
    elif answer == "transport":
        return Transport()
    elif answer == "Pogoda":
	    return Pogoda()
    elif answer == "pogoda":
        return Pogoda()
    elif answer == "Szansa":
	    return Szansa()
    elif answer == "szansa":
        return Szansa()
    else:
	    print "Nie rozumiem."
	    return question()
	
question()	    
       

       
       
       
