#coding: utf8
import numpy as np
import random

N = 3 #Longueur de la chaine
liste_rangee = range(N) #liste ordonnée à atteindre
OK = 0 #Critere d'arret tant qu'on ne tombe pas sur la sequence alignee


#Retourne toutes les permutations sous forme d'une liste à partir d'une sequence en entree (sous forme de liste)
def Permutation(liste):
	perms = []
	for i in range(len(liste)+1):
		for j in range(len(liste)+1):
			if (i != j) and ((i-j > 1) or (i-j < -1)) and (i < j):
				p = list(liste)
				p[i:j] = p[i:j][::-1]
				perms.append(p)
				if p == liste_rangee:
					global OK
					OK = 1
	return perms


T = 5 #nombre de repetitions
Nb_perms = [] #Stock les nombres de permutations necessaires pour chaque séquence

for t in range(T):
	#Cree une chaine de longueur N triée aleatoirement
	liste = range(N)
	random.shuffle(liste)
	Dict = {0 : liste} #On stocke les nouvelles permutations de chaque pas de temps dans un dictionnaire
	i = 1
	OK = 0
	while OK != 1: #Tant que la sequence n'est pas rangée
		if i == 1:
			Dict[i] = Permutation(Dict[i-1]) 
		else:
			PERMS= []
			for permu in Dict[i-1]: #Realise toutes les inversions possibles
				PERMS = PERMS + Permutation(permu)
			Dict[i] = PERMS #Stockage
		
		i += 1
	
	Nb_perms.append(max(Dict.keys()))
	
print "Pour une taille de séquence de ", N, ": ", Nb_perms

mon_fichier = open("Resultats%d.txt"%N, "w")
mon_fichier.write(str(Nb_perms))
mon_fichier.close()
