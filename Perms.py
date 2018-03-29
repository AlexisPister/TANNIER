#coding: utf8
import numpy as np
import random

#Initialise une liste de dimension voulue
def create_empty_array_of_shape(shape):
    if shape: return [create_empty_array_of_shape(shape[1:]) for i in xrange(shape[0])]


N = 7 #Longueur de la chaine
liste_rangee = range(N) #liste ordonnée à atteindre
OK = 0 #Critere d'arret tant qu'on ne tombe pas sur la sequence alignee


#Retourne toutes les permutations sous forme d'une liste à partir d'une sequence en entree
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



#Cree une chaine de longueur N triée aleatoirement
liste = range(N)
random.shuffle(liste)


T = 50 #nombre de repetitions
Nb_perms = [] #Stock le nombre de permutations necessaires

for t in range(T):
	#Cree une chaine de longueur N triée aleatoirement
	liste = range(N)
	random.shuffle(liste)
	Dict = {0 : liste} #On stocke les nouvelles permutations de chaque pas de temps dans un dictionnaire
	i = 1
	OK = 0
	while OK != 1:
		if i == 1:
			Dict[i] = Permutation(Dict[i-1])
		else:
			PERMS= []
			for permu in Dict[i-1]:
				PERMS = PERMS + Permutation(permu)
			Dict[i] = PERMS
		
		i += 1
	
	Nb_perms.append(max(Dict.keys()))
	
print "Pour une taille de séquence de ", N, ": ", Nb_perms
