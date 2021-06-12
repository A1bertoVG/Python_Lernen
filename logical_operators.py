#Variablen als "int"

a=50
b=20

if a>b:
    print('a ist größer als b')

elif a == b:
    print('beide sind gleich')

else:
    print('b ist größer als a')

#===================================================
#Variablen als "boolean"

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

#===================================================
#Beispiel: ein Haus kost $1M, ob der Käufer guten Kredit haben, subtrahieren Sie 10%.
# Andernfalls subtrahieren Sie 20%.
'''
guter_kredit = False  #Hier kann Mann es für "True" ändern.

kost = 10**6

if guter_kredit:
    zahlung = kost * 0.1

else:
    zahlung = kost * 0.2

print(f'der Kost des Hauses= ${zahlung}')
'''
#===================================================

#===================Logische Operatoren===========================
#Ob ein Bewerber ein hohes Einkommen und einen guten Kredit hat, kann Man einen Kredit haben.

'''guten_kredit = True
hohes_einkommen = False

if guten_kredit and not hohes_einkommen:   #Man kann "and", "or" oder "and not" benutzen
    print('Autorisierten Kredit')

else:
    print('Kredit nicht möglich. ')'''
