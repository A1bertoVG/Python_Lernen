import numpy
#===================CÓDIGO DE PRUEBAS USANDO NUMPY===========================
'''
l = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13, 14, 15, 16]]

print('print (l)')
print(l)

print('numpy.array')
print(numpy.array(l))

print('imprimir 2 primeros grupos')
print(numpy.array(l)[0:2])

print('imprimir seccion de los 2 primeros grupos')
print(numpy.array(l)[0:2, 1:3])
'''

##===================Bedingungen===========================
'''
a=50
b=20

if a>b:
    print('a ist größer als b')

elif a == b:
    print('beide sind gleich')

else:
    print('b ist größer als a')
'''
##===================Drunken===========================
'''print('a')
print('-----0')
print('.w'*10)
'''
##===================Variablen===========================
'''
a=10                 #Zahlen ohne Dezimalstellen heisst "Integrer"
b= 4.5                  # das heisst "floating point number/ float for short/ floats"
c='string'              #Strings
is_published = False    #Variable "boolean", es ist ja oder nein
'''
#Beispiel: der Patient John Smith ist 20 Jahre alt und ist ein neuer Patient
'''name = 'John Smith'
age = 20
registered = False'''

#===================Eingang===========================
#Beispeil: Fragst du der Name und die Lieblingsfarbe
'''name = input('Wie heißen Sie? ')
farbe = input('Was ist deine Lieblingsfarbe? ')
print(name + ' magst ' + farbe)'''

#===================Typkonvertierung===========================
#Funktionen zum Konvertieren Werte:
'''
int()      Konvertieren in Integrer
float()    Konvertieren in float (Zahlen mit Dezimal)
bool()    Konvertieren in Boolean Value
'''
#Beispiel: Schreiben sie ein Programm das Kilo in Pfund umrechnen.
'''Pfund = 2.20462
peso_kilo = input('Wie viel wiegen Sie? ')
peso_pfund = Pfund * int(peso_kilo)
print( 'Sie wiegen ' + str(peso_pfund) + ' Pfund' )'''

#===================Strings===========================

course = 'Python for beginners'
course1 = "Python for 'Beginners'"
course2 = 'Python for "Beginners"'

course3 = '''Guten Tag Herr García,

Willkommen zu diesen neuen Kurs.

Viele Grüße
Alberto Velasquez Garcia'''

'''
print(course)
print(course1)
print(course2)
print(course3)

course4 = 'Python for beginners'
#          0123456789......     Das ist der Index, jeden Buchstabe hat ein Zahl oder Platzevalure.
print(course4[::-1])
#Man kann auch ein String in andere Sttring speichernen.
speirchernen = course4[11:]
print(speirchernen)
print(course4[:10] + ' ' + speirchernen [::-1])
print(speirchernen[1:-1])
print(speirchernen[:-1])
'''

#===================Formated Strings===========================
'''
Vorname = 'Alberto'
Name = 'Velasquez'
nachricht = Vorname + ' [' + Name + '] ist Programmierer' #(das heißt Concatenation)wir müssen es einfacher machen,dann...
nr= f'{Vorname} [{Name}] ist Programmierer' #Das ist eine formated string
print(nachricht)
print(nr)
'''
#===================Strings Methods===========================
'''
print(len(course)) #Ich benutze ""course" in linie 71
# Mit "len" kann Man wissen wie vielen Buchstabe es gibt.
print(course.upper())
print(course.lower())
print(course.find('y'))  #Es gibt die Index von der Buchstabe
print(course.replace('e', 'i'))
print('Python' in course) #Es ist ein ""Boolean" Ausdruck, deshalb gibt es nur True oder False als antwort
'''
#===================Arithmetic Operations===========================
#Es gibt Addition +, Subtraktion -, Multiplikation * und Division
'''
print(10 / 3) #Es gibt ein Float
print(10 // 3) #Es gibt ein Integrer
print(10 % 3) #Es gibt Divisions Rest
print(10 ** 3) #Es gibt Potenz

a = 10
a = a + 3
print(a)
a **= 3
print(a)
'''
#===================Operator Precedence===========================
#x = 3+3*3**3-3/3
#print(x)
'''Erste: Potenz und Wurzeln
Zweite: Divisionen und Multiplikationen
Letzte: Additionen und Subtraktionen.'''

#===================Matematische Funktionen===========================
'''x= 2.5
print(round(x))  #Funktion benutzt um eine Zahl zu runden.
print(abs(-3.25)) #Funktion benutzt um der Absolutwert  zu erhalten.'''

#import math  Modul mit Matematik calculus wie cos, sin, tan, etc...

#===================if-Anweisungen===========================
'''
warm_tag = True
kalt_tag = False

if warm_tag:
    print('Wasser trinken')

elif kalt_tag:
    print('Einen Jacke benutzen')

else:
    print('Alles sind in Ornung')

print('Haben Sie einen guten Tag')'''
#Beispiel: ein Haus kost $1M, ob der Käufer guten Kredit haben, subtrahieren Sie 10%.
# Andernfalls subtrahieren Sie 20%.
'''
guter_kredit = False

kost = 10**6

if guter_kredit:
    zahlung = kost * 0.1

else:
    zahlung = kost * 0.2

print(f'der Kost des Hauses= ${zahlung}')
'''
#===================Logische Operatoren===========================
#Ob ein Bewerber ein hohes Einkommen und einen guten Kredit hat, kann Man einen Kredit haben.
'''guten_kredit = True
hohes_einkommen = False

if guten_kredit and not hohes_einkommen:   #Man kann "and", "or" oder "and not" benutzen
    print('Autorisierten Kredit')

else:
    print('Kredit nicht möglich. ')'''

#=================Split String==================
'''
nachricht = 'Alberto Velasquez Garcia'
x = nachricht.split()
print(f'Iniciales= {x[0][0]}.{x[1][0]}.{x[2][0]}.')

# len() cuenta los caracteres de un mensaje
'''
#================Vergleichsoperatoren================
'''
temp = 26;

if 26 <= temp:
    print('Es ist einen warmen Tag')

elif 15 < temp < 26:
    print('Es ist einen schönen Tag')

else:
    print('Es ist einen kalten Tag')
'''
#z.B. Der Name muss mehr als 3 Buchstaben sein und wenig als 50.

'''name = input('Schreiben Sie Ihnen Name:  ')
x = len(name)

if x > 15:
    print('Es muss wenig als 50 Buchstaben sein')

elif 3 <= x:
    print('Willkommen ' + name)

else:
    print('Das sieht nicht wie ein Name aus.')'''

    #Beispiel 2. Fragen Sie das Gewicht und wenn es Kg oder Lb ist, dann umrechnen Sie es.

'''gewicht = input('Wie viel wiegen Sie? ')
einheiten = input('Welche Einheiten? (kg oder lb) ')

if einheiten.upper() == 'KG' :                #.upper kovertiert alles in Großbuchstaben
    umrechnen = int(gewicht) / 0.4536
    print(f'Sie wiegen {int(umrechnen)} lb')

elif einheiten == 'LB':
    umrechnen = int(gewicht) * 0.4536
    print(f'Sie wiegen {int(umrechnen)} kg')'''

#================While================

'''i = 1
while i<=5:
    print('*'*i)
    i+=1'''
    # Beispiel 2. Ein Spiel wo Man muss ein Zahl vermuten.

geheime_num = 9
vermutet_versucht =0
vermutet_max = 3

while vermutet_versucht < vermutet_max:
    ver_zahl = int(input('Vermuten: '))
    vermutet_versucht += 1

    if geheime_num == ver_zahl:
        print('Geschafft!')
        break

else:
    print('Du hast verloren')



