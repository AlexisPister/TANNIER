import ast


def moyenne(liste): 
	return float(sum(liste)) / len(liste)

def variance(liste): 
    if (liste!= []): 
        Esp = moyenne(liste) 
        liste2 = [(float(x)-Esp)**2 for x in liste] 
        return moyenne(liste2)

Analyse = open('Analyse.txt', 'a')

for i in range(3,8):
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
			Analyse.write("Moyenne :%f \n"%moy)
			Analyse.write("Variance : %f \n \n"%var)
			
			
Analyse.close()
