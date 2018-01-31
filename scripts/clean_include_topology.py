#!/usr/bin/python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser

""" 
Hey ! If you're here, you must be interested in what's inside this script.
Basically, it removes all the lines starting with # (which are the include statements)
and puts a pre-defined stack of includes instead.

The whole ArgumentParser stuff is what handles the -f and -o from the command line, 
for inputs and outputs.
"""

parser = ArgumentParser(description=""" Clean the includes in the topology
Used within the INSANE tutorial""")

# Named arguments
parser.add_argument("-f", "--file", help="The name of the input topology file", required=True)
parser.add_argument("-o", "--output", help="The name of the output topology file", required=True)
args = parser.parse_args()

# Input / Output
topolname = args.file
out_topolname = args.output

######################## The script ########################

# It's straightforward: load the topology (as list of lines)
topology = open(topolname, "r").readlines()

# Remove the lines that start with #
topology = [x for x in topology if x.startswith("#") == False]

# Put it back together
topology = "".join(topology)

# Small modification here, Protein is in fact Protein_A in our topology file
topology = topology.replace("Protein", "Protein_A")

# We want to add a small list of includes ...
includes = """#include "martini_v2.2.itp"
#include "Protein_A.itp"
#include "martini_v2.0_lipids_all_201506.itp"
#include "martini_v2.0_ions.itp
"""

# Open the output
out_ = open(out_topolname, "w")

# Just write everything into it
out_.write(includes + topology)

# Close the output
out_.close()






