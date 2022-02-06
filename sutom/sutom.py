
import os


class Sutom:

    def récupération_fichier():
        for count, file in enumerate(os.listdir("fichier_a_analyser")):
            nom_fichier = os.path.join("fichier_a_analyser", file)
        return nom_fichier, count

    def récupération_donnée(nom_fichier):
        dict_joueurs = {}
        with open(nom_fichier,'r',encoding = 'utf-8') as f:
            for l in f:
                loc_sutom = l.find(": SUTOM #")
                if loc_sutom != -1:
                    loc_nom = l.find(" - ")+3
                    nom = l[loc_nom:loc_sutom]
                    if nom not in dict_joueurs:
                        dict_joueurs[nom] = [0, 0]
                    loc_score = l[loc_sutom+9:].find(" ")+(loc_sutom+9)+1
                    new_score = l[loc_score:loc_score+1]
                    new_score = 7 if new_score == "-" else int(new_score)
                    old_total = dict_joueurs[nom]
                    old_score = old_total[0]
                    old_partie =  old_total[1]
                    dict_joueurs[nom] = [old_score+new_score,old_partie+1]
        return dict_joueurs

    def trie_et_moyenne(dict_joueurs):
        for j in dict_joueurs.items():
            total = dict_joueurs[j[0]]
            score = total[0]
            partie =  total[1]
            dict_joueurs[j[0]] = [score, partie,round(score/partie, 2)]
        return sorted(dict_joueurs.items(), key=lambda t: t[1][2])

    def affichage(liste_tri):
        for count, j in enumerate(liste_tri):
            if count == 0:
                print(
                        f'{count+1}er : {j[0]} : {j[1][1]} Parties, {j[1][0]} Points, {j[1][2]} de moyenne'
                )
            else:
                print(
                        f'{count+1}ème : {j[0]} : {j[1][1]} Parties, {j[1][0]} Points, {j[1][2]} de moyenne'
                )

class Start:

    nom_fichier, count = Sutom.récupération_fichier()
    if count != 0:
        print ("ERREUR : Trop de fichier dans le dossier <fichier_a_analyser>")
    else:
        dict_joueurs = Sutom.récupération_donnée(nom_fichier)
        liste_tri = Sutom.trie_et_moyenne(dict_joueurs)
        Sutom.affichage(liste_tri)