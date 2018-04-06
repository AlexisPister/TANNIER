
# on crée deux listes de gènes (taille 7 et 13, comme dans l'énoncé)
A = c('A','B','C','D','E','F','G')
B = c('A','B','C','D','E','F','G','H','I','J','K','L','M')

#Permet de prendre une liste de gènes et de la mélanger.
E = vector(length = length(A))
for (i in 1:length(A)){
  E = sample(A,replace = F)
}

# prend une liste de gènes et les orientations. Effectue une inversion quelque part dans le génome.
# La taille maximale des inversion est limitée à 1/100 du génome soit environ 8 bases.
permutateur2 = function(frame){
  vec1 <- frame[,1]
  vec2 <- frame[,2]
  borne_inf = sample((1:length(vec1)),1, replace = FALSE)
  borne_sup = borne_inf + sample((1:round(length(vec1)/100)),1, replace = FALSE)
  if (borne_sup > length(vec1)){
    borne_sup <- length(vec1)
  }
  subseq = vec1[borne_inf:borne_sup]
  vec1[borne_inf:borne_sup] = rev(subseq)
  vec2[borne_inf:borne_sup] = (-1)*vec2[borne_inf:borne_sup]
  frame <- matrix(data = c(vec1,vec2),ncol = 2,byrow = F)
  return(frame)
}

#print(evolution())


# Question 1 de la partie 2
# On crée un liste de gènes avec ses orientations que l'on converti en data.frame
Genes = seq(from = 1,to = 803, by = 1)
orient = rep(1,803)
frame <- matrix(data = c(Genes,orient),ncol = 2,byrow = F)
frame <- data.frame(frame)
colnames(frame) <- c("gene_id","direction")
final_frame <- frame

#Question 7 de la partie 1, 10000 permutations de taille 98, trouvée avec entre les drosophiles
for (i in 1:10000){
  frame <- matrix(data = c(Genes,orient),ncol = 2,byrow = F)
  frame <- data.frame(frame)
  for (j in 1:98){
    frame <- permutateur2(frame)
    frame <- data.frame(frame)
    colnames(frame) <- c("gene_id","direction")
    if(j%%98==0){
      final_frame <- cbind(final_frame,frame)
    }
  }
  print(i)
}

#visualisation (plot du 5 partie 1)
col = vector(length = 803)

for (i in 1:length(frame[,2])){
  if (frame[i,2]== 1){
    col[i] = "red"
  }else{
    col[i] = "blue"
  }
}
# affichage graphique
par(mfrow = c(2,3))
plot(frame[,1],col = col, xlab = "gene_id_origine", ylab = "gene_id_dérivé",las=1,main = "20 inversions")
legend("topleft",legend = c("orientation +1","orientation -1"), col = c("red","blue"), pch = c(1,1))
output = data.frame(frame)
colnames(output) <- c("gene_id","direction")

#export de la table dans un fichier
write.table(final_frame,file = "permut_algo_98_10000.txt",sep = "\t",eol = "\n",row.names=FALSE)
