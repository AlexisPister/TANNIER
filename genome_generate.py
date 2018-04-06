#! /usr/bin/env python
# -*- coding:utf-8 -*-

import networkx as nx
from networkx.utils import not_implemented_for
import matplotlib.pyplot as plt
import numpy as np
import random
import time
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
sr = random.SystemRandom()
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
import math

MAX_ALIGNMENTS = 2

#générer un génome
def genome_generation_v3(size_of_genome):
	sequence_h = ''.join(sr.choice('AGTC') for x in range(size_of_genome)) 
	return(sequence_h)

#réaliser une mutation ponctuelle
def q3_muta_ponct(genome1):
	i = int(round(random.random()*(len(genome1)-1)))
	mut = sr.choice('AGTC')
	while(genome1[i] == mut):
		mut = sr.choice('AGTC')
	genome1[i] = mut
	return(genome1)

#réalise des alignements
def alignment_gen1(genome1,genome2):
	#alignments = pairwise2.align.globalxx(genome1,genome2,one_alignment_only = True, MAX_ALIGNMENTS = 2)
	alignments = pairwise2.align.globalxx(genome1,genome2,one_alignment_only = True)
	#for elem in alignments:
		#print(elem)
	return(alignments[0][2])

#non utilisé ici, c'est un autre tye d'alignement
def alignment_gen2(genome1,genome2):
	alignments = pairwise2.align.globalms(genome1,genome2, 2, -1, -2, -0.5,MAX_ALIGNMENTS = 3)
	#for elem in alignments:
		#print(elem)
	return(alignments[0][2])
#réalise l'évolution du génome
def evolution_of_a_genome(gen_size,number_of_generations,step):
	t1 = time.time()
	my_seq = Seq(genome_generation_v3(gen_size))
	#print(my_seq)
	y = []
	print("J'ai fait le genome en %.4f secondes." %(time.time()-t1))
	for i in range(number_of_generations): #number of generations
		y.append(int(gen_size-i)) # size of genome - i
	y = y[0:number_of_generations:step]
	print("J'ai fait y")
	my_seq1 = my_seq.tomutable()
	hist_scor_align1 = []
	old_seq = my_seq1

	for i in range(number_of_generations):
		new_seq = q3_muta_ponct(old_seq)
		#print(new_seq)
		if (i%step==0):
			hist_scor_align1.append(int(alignment_gen1(my_seq,new_seq)))
		old_seq = new_seq
	print("J'ai fait les alignements")
		#if(np.absolute((hist_scor_align1[i/10]-y[i])/y[i]) > 0.05):
	i=0
	#affiche l'évolution des paramètres
	plt.plot(np.arange(0,number_of_generations,step),hist_scor_align1,label="score de pairwise2xx")
	plt.plot(np.arange(0,number_of_generations,step),y,label="Nombre de bases identiques theorique")
	plt.xlabel("Nombre de mutations")
	plt.ylabel("Bases identiques")
	plt.legend()
	plt.show()

	#while (np.absolute(((float(hist_scor_align1[i]-y[i]))/float(hist_scor_align1[i])))<0.05):
		#i+=1
	#print(i*step)
def time_tester_for_genome(gen_size,repetition):
	times = []
	for i in range(repetition):
		t1 = time.time()
		hist = genome_generation_v3(gen_size)
		times.append(time.time()-t1)
	print(gen_size,np.mean(times))


#réaliser une évolution avec des genomes de taille 100000, sur 50000 générations par pas de 50000.
evolution_of_a_genome(100000,50000,50000)
#time_tester_for_genome(30000,3)
#genome_generation_v3(100)
#filename1 = 'my_genome.txt'
#file = open("my_genome.txt","w") 
#file.write("gene_id \t sequence \t order \t adjacency \n")
#G = genome_generation(number_of_genes = 5,size_of_genes = 3)
#file.close()
