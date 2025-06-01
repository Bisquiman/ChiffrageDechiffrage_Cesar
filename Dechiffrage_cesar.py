#######################################################
# Crée par Mathis Robinet
# Crée le 2025-05-28 à 12h35, fini le 2025-05-28 à 18h17
# Algorithm de dechiffrage du code César
#######################################################

import pandas as pd

code= input(str("Entrez votre code secret (en minuscule) :"))
code_min=code.lower()
remplace_accent = {224: 97, 225: 97, 226: 97, 231: 99, 232: 101, 233: 101, 234: 101, 235: 101, 238: 105, 239: 105,
                   244: 111, 246: 111, 249: 117, 251: 117, 252: 117}
codeF= code_min.translate(remplace_accent)

dico= pd.read_csv("C:/temp/Lexique382.csv")

alphabet= "abcdefghijklmnopqrstuvwxyz"
ponctuation= ",.:;?!"
apostrophe= "'"
espace= " "
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

            elif caractere in apostrophe:
                resultat.append(caractere)
                resultat_dico.append(caractere + espace)

            elif caractere in tiret or espace:
                resultat.append(caractere)
                resultat_dico.append(caractere)

            elif caractere in ponctuation:
                resultat.append(caractere)

        resultat = "".join(resultat)
        resultat_dico= "".join(resultat_dico)

        n_espace = resultat_dico.count(" ")
        mot = resultat_dico.split()

# À ajouter: si mot en début de phrase ajouter MAJ après trad + mots avec tiret

        for i in range(n_espace+1):
            if mot[i] in dico["ortho"].to_list():
                proba.append(1)
                proba_FR=sum(proba)
                pourcentage=((n_espace+1)*70)/100
#Si le nombre de motrs francais dans le message est plus grand que 70% du nombre de mot du message, la clé est la bonne, comme ca ca résous le problème des "c'est"
#ou le "c(apostrophe)" est conté comme un mot ou meme le probvleme des nom propre qui ne sont pas dans le dico.
                if  proba_FR > pourcentage:
                    print(f"Le code a une clé de {cle:} et est: {resultat}")
                    exit()
            else:
                proba.append(0)

    print("Le déchiffrage a échoué")

dechiffrage_cesar(codeF)

#je mange des choux-fleurs= to wkxqo noc mryeh-pvoebc (tiret)
#gros bol= qbyc lyv
#le gros chat escalade un arbre= oh jurv fkdw hvfdodgh xq dueuh
#l'asticot = m'btujdpu