#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:54:32 2019

@author: C00252137
"""

import argparse
import numpy as np
import networkx as nx
import node2vec
import gensim
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

def parse_args():
	'''
	Parses the node2vec arguments.
	'''
	parser = argparse.ArgumentParser(description="Run node2vec.")

	parser.add_argument('--input', nargs='?', default='/home/debanjalib/1994-1996.csv',
	                    help='Input graph path')

	parser.add_argument('--output', nargs='?', default='94-96_graph.csv',
	                    help='Embeddings path')

	parser.add_argument('--dimensions', type=int, default=9,
	                    help='Number of dimensions. Default is 128.')

	parser.add_argument('--walk-length', type=int, default=9,
	                    help='Length of walk per source. Default is 80.')

	parser.add_argument('--num-walks', type=int, default=5,
	                    help='Number of walks per source. Default is 10.')

	parser.add_argument('--window-size', type=int, default=9,
                    	help='Context size for optimization. Default is 10.')

	parser.add_argument('--iter', default=1, type=int,
                      help='Number of epochs in SGD')

	parser.add_argument('--workers', type=int, default=8,
	                    help='Number of parallel workers. Default is 8.')

	parser.add_argument('--p', type=float, default=1,
	                    help='Return hyperparameter. Default is 1.')

	parser.add_argument('--q', type=float, default=1,
	                    help='Inout hyperparameter. Default is 1.')

	parser.add_argument('--weighted', dest='weighted', action='store_true',
	                    help='Boolean specifying (un)weighted. Default is unweighted.')
	parser.add_argument('--unweighted', dest='unweighted', action='store_false')
	parser.set_defaults(weighted=False)

	parser.add_argument('--directed', dest='default', action='store_true',
	                    help='Graph is (un)directed. Default is undirected.')
	parser.add_argument('--undirected', dest='undirected', action='store_false')
	parser.set_defaults(directed=False)

	return parser.parse_args()

def read_graph():
    fh=open("/home/debanjalib/1994-1996.csv",'r')
    if args.weighted:
         G = nx.Graph()
         for line in fh:
            tokens = line.split()
            print(tokens)
            if len(tokens)>1:
                G.add_weighted_edges_from([(int(tokens[0]),int(tokens[1]),int(tokens[2]))])
	#if args.weighted:
	#	G = nx.read_weighted_edgelist(args.input, nodetype=int, data=(('weight',float),),delimiter=',', create_using=nx.DiGraph())
    else:
        G = nx.read_weighted_edgelist(args.input, nodetype=int,create_using=nx.DiGraph())
        for edge in G.edges(data=True):
            G[edge[0]][edge[1]]['weight'] = 1
    if not args.directed:
        G = G.to_undirected()
    return G

def learn_embeddings(walks):
	'''
	Learn embeddings by optimizing the Skipgram objective using SGD.
	'''
	walks = [list(map(str, walk)) for walk in walks]
	model = Word2Vec(walks,size=args.dimensions, window=args.window_size, min_count=1,sg=1, workers=args.workers, iter=args.iter)
	model.wv.save_word2vec_format(args.output)
    #vmodel.wv.save_word2vec_format
	
	return

def main(args):
	'''
	Pipeline for representational learning for all nodes in a graph.
	'''
	nx_G = read_graph()
	G = node2vec.Graph(nx_G, args.directed, args.p, args.q)
	G.preprocess_transition_probs()
	walks = G.simulate_walks(args.num_walks, args.walk_length)
	learn_embeddings(walks)

if __name__ == "__main__":
	args = parse_args()
	main(args)


