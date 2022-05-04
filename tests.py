print ("hello world")
print ("laipni luugts testaa par Zemes grupas planeetam! (Marss, Zeme, Venera, Merkurs) ")
 playing = input ("Vai esi gatavs/a? ")
 
def new_func():
    return else

if playing != " ja ":
   new_func() quit()
print ("labi! sākam!")

score = 0


answer = input ("Mazākā Saules sistēmas planēta? ")
if answer == " Merkurs ":
    print ('pareizi!')
    score +=1
else:
    print ('nepareizi!')

answer = input ("Merkuram ir pavadoņi? ")
if answer == " ne ":
    print ('pareizi!')
    score +=1
else:
    print ('nepareizi!')

answer = input ("Otrā Saulei tuvākā planēta? ")
if answer == " Venera ":
    print ('pareizi!')
    score +=1
else:
    print ('nepareizi!')


answer = input ("Pati karstākā Saules sistēmas planēta? ")
if answer == " Venera ":
    print ('pareizi!')
    score +=1
else:
    print ('nepareizi!')

answer = input ("Vai Zeme ir apaļa? ")
if answer == " ne ":
    print ('pareizi!')
    score +=1
else:
    print ('nepareizi!')


answer = input ("Uz Zemes pastāv dzīvība? ")
if answer == " ja ":
    print ('pareizi!')
    score +=1
else:
    print ('nepareizi!')


answer = input ("Zemi klāj 2/3 okeāni, bet 1/3 aizņem ..... ? ")
if answer == " sauszeme ":
    print ('pareizi!')
    score +=1
else:
    print ('nepareizi!')

answer = input ("Zemei līdzīgākā planēta? ")
if answer == " Marss ":
    print ('pareizi!')
    score +=1
else:
    print ('nepareizi!')

answer = input ("Kā sauc Zemes pavadoni? ")
if answer == " Mēness ":
    print ('pareizi!')
    score +=1
else:
    print ('nepareizi!')

answer = input ("Cik pavadoņu ir Marsam?? ")
if answer == " 2 ":
    print ('pareizi!')
    score +=1
else:
    print ('nepareizi!')



print ("Tu atbildēji pareizi uz  " + str (score)+ " jautājumiem no 10")
print ("Tu ieguvi  " + str (score/4 * 100)+ " % ")


