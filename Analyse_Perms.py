#Analyse les fichiers des résultats des permutations
import ast

def moyenne(liste): #Moyenne d'une liste
	return float(sum(liste)) / len(liste)

def variance(liste): #Variance d'une liste
    if (liste!= []): 
        Esp = moyenne(liste) 
        liste2 = [(float(x)-Esp)**2 for x in liste] 
        return moyenne(liste2)

Analyse = open('Analyse.txt', 'a')

for i in range(3,8): #Pour les differents fichiers de resultat
	with open("Permut%d.txt"%i, "r") as f:
		for line in f.readlines():
			result = ast.literal_eval(line)
			print result
			print result[0]
			moy = moyenne(result)
			var = variance(result)
			
			Analyse.write("Resultats %d :\n"%i)
			Analyse.write(str(result))
			Analyse.write("\n")
			Analyse.write("Moyenne :%f \n"%moy) #Enregistre la moyenne
			Analyse.write("Variance : %f \n \n"%var) #Enregistre la variance
			
			
Analyse.close()
