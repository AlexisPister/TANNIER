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

def view_and_write_graph(aGraph):
	pos=nx.spring_layout(G)
	color_map = []
	for node in G:
		if random.random() <0.5:
			color_map.append('red')
	else :
		color_map.append('blue')  
	labels = {}
	for idx, node in enumerate(G.nodes()):
		labels[node] = ''.join([sr.choice('AGTC') for x in range(size_of_genes)])
	nx.draw(G,labels = labels,node_color = color_map, with_labels = True)
	plt.show()
	nx.write_adjlist(G,"test_de_graph.adjlist")

def genome_generation_v1(number_of_genes,size_of_genes):
	gene_id_h = []
	sequence_h = []
	order_h = []
	adjacency_h = []

	G=nx.path_graph(number_of_genes)
	all_genes = range(number_of_genes)
	gene_id_h = np.copy(all_genes)
	order = [0,1]
	for i in range(number_of_genes):
		gene = []
		for j in range(size_of_genes):
			gene = ''.join([sr.choice('AGTC') for x in range(size_of_genes)]) 
		sequence_h.append(gene)
		if i<len(all_genes)-1:
			order_i = sr.choice(order)
			order_h.append(order_i)
			adjacency_i = i+1
			adjacency_h.append(adjacency_i)
			file.write(str(i)+"\t"+str(gene)+"\t"+str(order_i)+"\t"+str(adjacency_i)+"\n")
		else : 
			order_i = sr.choice(order)
			order_h.append(order_i)
			adjacency_h.append(None)
			file.write(str(i)+"\t"+str(gene)+"\t"+str(order_i)+"\t"+str("None")+"\n")
	print(gene_id_h,sequence_h,order_h,adjacency_h)
	return (G)
	#return(sequence_h)

def genome_generation_v2(number_of_genes,size_of_genes):
	sequence_h = []
	for i in range(number_of_genes):
		gene = []
		for j in range(size_of_genes):
			gene = ''.join([sr.choice('AGTC') for x in range(size_of_genes)]) 
		sequence_h.append(gene)
	all_genome = ''.join(sequence_h)
	return(all_genome)

def genome_generation_v3(size_of_genome):
	sequence_h = ''.join(sr.choice('AGTC') for x in range(size_of_genome)) 
	return(sequence_h)


def q3_muta_ponct(genome1):
	i = int(round(random.random()*(len(genome1)-1)))
	mut = sr.choice('AGTC')
	while(genome1[i] == mut):
		mut = sr.choice('AGTC')
	genome1[i] = mut
	return(genome1)


def alignment_gen1(genome1,genome2):
	alignments = pairwise2.align.globalxx(genome1,genome2,one_alignment_only = True)
	#for elem in alignments:
		#print(elem)
	return(alignments[0][2])

def alignment_gen2(genome1,genome2):
	alignments = pairwise2.align.globalms(genome1,genome2, 2, -1, -2, -0.5,MAX_ALIGNMENTS = 3)
	#for elem in alignments:
		#print(elem)
	return(alignments[0][2])

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



evolution_of_a_genome(100000,50000,50000)
#time_tester_for_genome(30000,3)
#genome_generation_v3(100)
#filename1 = 'my_genome.txt'
#file = open("my_genome.txt","w") 
#file.write("gene_id \t sequence \t order \t adjacency \n")
#G = genome_generation(number_of_genes = 5,size_of_genes = 3)
#file.close()