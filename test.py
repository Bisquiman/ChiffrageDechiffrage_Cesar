# Crée le 2025-05-28 à 12h35
# Algorithm de dechiffrage du code César

#proba=[2,3]
#
#proba.append(1)
#x= sum(proba)
#print(x)

#dawdawdwadawdawdawdwa

#for i in range(3):
#    proba.append(i)
#    x= sum(proba)
#
#    if proba == n_mots:
#        print("ENFIIIIIIIIIIIIIIIIIIN")
#        exit()


#apstrophe et convertir accent
import math
import pandas as pd

code = input(str("Entrez votre code secret (en minuscule) :"))
code_min=code.lower()
remplace_accent = {224: 97, 225: 97, 226: 97, 231: 99, 232: 101, 233: 101, 234: 101, 235: 101, 238: 105, 239: 105,
                   244: 111, 246: 111, 249: 117, 251: 117, 252: 117}
codeF=code_min.translate(remplace_accent)

dico = pd.read_csv("C:/temp/Lexique382.csv")

alphabet= "abcdefghijklmnopqrstuvwxyz"
ponctuation= ",.:;?!"
apostrophe= "'"
espace= " "
#accent = "éèêôöîïàâçùûü"
#c="c'"
tiret="-"

taille=len(alphabet)

def dechiffrage_cesar(codeF):
    for cle in range(1,taille):
        resultat= []
        proba = []
        resultat_dico= []

        for caractere in codeF:
            if caractere in alphabet:
                index = alphabet.index(caractere)
                nouveau_index = (index - cle) % taille
                resultat.append(alphabet[nouveau_index])
                resultat_dico.append(alphabet[nouveau_index])
            # Problème: lorsque "c'est" est dans le code secret, le "c'" est séparé du "est", il ne trouve pas le "c'" dans le dico alors le dechiffrement échoue
            elif caractere in apostrophe:
                resultat.append(caractere)
                resultat_dico.append(caractere+espace)

            #elif caractere in apostrophe.startswith("c"):
            #   resultat.append(caractere)
            #   resultat_dico.append(caractere)
            #
            #elif caractere in c:
            #   resultat.append(caractere)
            #   resultat_dico.append(caractere)

            elif caractere in ponctuation:
                resultat.append(caractere)

            elif caractere in espace:
                resultat.append(caractere)
                resultat_dico.append(caractere)

        resultat = "".join(resultat)
        resultat_dico= "".join(resultat_dico)
        n_espace = resultat.count(" ")                          #enlever les ponctuations pour le split sion le mots ne sera pas trouveé dans le dictinnaire,...
        mot = resultat_dico.split()                             #...mais garder trait union et apostrophe


        for i in range(n_espace+1):                                      #n_espace est choisis, car dans une liste, le 0 est le début, alors si on compte le 0, nbr espaces =nbr mots,...
            if mot[i] in dico["ortho"].to_list():                        #...car nrb espace= nbr mots -1
                proba.append(1)
                proba_FR=sum(proba)                                    #Additionner la proba précedante + i (quand i=0 la proba initiale est de 0, la liste est vide)

                if  proba_FR == n_espace+1:
                    print(f"Le code a une clé de {cle:} et est: {resultat}")
                    exit()
            else:
                proba.append(0)



    print("Le déchiffrage a échoué")

dechiffrage_cesar(codeF)

#je mange des choux-fleurs= to wkxqo noc mryeh-pvoebc
#gros bol= qbyc lyv
#le gros chat escalade un arbre= oh jurv fkdw hvfdodgh xq dueuh

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#pour mettre la liste de caractère en un mots regarder la méthode split ou chercher syntax comme print une liste



#cle= int(input("choisis ta clé:"))
#
#while True:
#    mot= []
#    message = input(str("Écrivez votre message codé en minuscule:"))
#    alphabet = "abcdefghijklmnopqrstuvwxyz"
#    index= alphabet.index(message)
#    index_new= index + cle
#    mot.append(alphabet[index_new])
#    print(mot)
#    mot.clear()

##########
#df = pd.read_excel("C:/temp/Lexique382.xlsx")
#x= "bleu"
#y= "noir"

#liste=[y]
#
#liste.append(x)
#print(liste)
#n_espace=liste.count()
#print(n_espace)
#n_mots= n_espace + 1
#
#print(n_mots)
#print(liste[0] and liste[1] in df["ortho"].to_list())


#if liste in df["ortho"].to_list():
#    print('True')











#def dechiffrer_cesar(message):
#    """Essaie toutes les clés de 1 à 25 pour déchiffrer message"""
#    alphabet = "abcdefghijklmnopqrstuvwxyz"
#    taille = len(alphabet)
#
#    for cle in range(1, taille):
#        resultat = []
#
#        for caractere in message:
#            #if caractere in alphabet:
#            #    index = alphabet.index(caractere)
#            #    nouveau_index = (index - cle) % taille
#            #    resultat.append(alphabet[nouveau_index])
#            #else:
#            #    resultat.append(caractere)  # conserve espace/ponctuation
#
#        texte_dechiffre = "".join(resultat)
#        print(f"Clé {cle:2d} : {texte_dechiffre}")
#
#message=input(str("Écrivez votre message codé en minuscule:"))
#dechiffrer_cesar(message)

#import os
#
#chemin = "C:/temp/Lexique382.xlsx"
#
#if os.path.exists(chemin):
#    print(" Fichier trouvé.")
#else:
#    print(" Fichier introuvable.")
#


#
#chemin = "C:/temp/Lexique382.xlsx"
#
#df = pd.read_excel(chemin)
#print(df["ortho"].to_list())
#
#for i in range(1,5):
#   #df = pd.read_excel( "Lexique382")
#   #mots_francais= df[1][i]
#   #print(df)  # Affiche les 5 premières lignes
#cle= int(input("choisis ta clé:"))
#message=input(str("Écrivez votre message codé en minuscule:"))
#
##def chifferage_cesar(message):
##    resultat= []
##    alphabet = "abcdefghijklmnopqrstuvwxyz"
##    index= alphabet.index(message)
##    index_new= index + cle
##    resultat.append(alphabet[index_new])
##    print(resultat)
##
##chifferage_cesar(message)