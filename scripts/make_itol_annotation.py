#!/usr/bin/env python3
from pylab import *
import matplotlib
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("input_csv",help="Two-column csv of the form sequence_name,annotation")
parser.add_argument("annotation_start",help="iTOL dataset starter file")
parser.add_argument("--dataset_name",default="iTOL_dataset",help="Dataset name")
parser.add_argument("--output_file",default="iTOL_annotation.txt",help="output iTOL annotation file")
parser.add_argument("--colour_file",default=None,help="two-column csv of the form annotation,hex_colour")
args=parser.parse_args()

sequences_to_clades=dict()
for line in open(args.input_csv):
	tokens=line.strip().split(",")
	if len(tokens)==2:
		sequences_to_clades[tokens[0]]=tokens[1]

clade_colours=dict()
if args.colour_file is not None:
	for line in open(args.colour_file):
		tokens=line.strip().split(",")
		if len(tokens)==2:
			clade_colours[tokens[0]]=tokens[1]
	for clade in sequences_to_clades.values():
		if clade not in clade_colours.keys():
			print(f"Missing colour for clade {clade}.")
			exit(1)
else:
	cmap =cm.get_cmap("magma",len(set(sequences_to_clades.values())))
	for i,clade in enumerate(list(set(sequences_to_clades.values()))):
		rgba=cmap(cmap.N-i)
		clade_colours[clade]=matplotlib.colors.rgb2hex(rgba)


output=open(args.output_file,"w")
for line in open(args.annotation_start):
	output.write(line.replace("MY_DATASET",args.dataset_name))

for sequence,clade in sequences_to_clades.items():
        output.write(f"{sequence},{clade_colours[sequences_to_clades[sequence]]},{sequences_to_clades[sequence]}\n")
output.close()

