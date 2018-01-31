#!/usr/bin/python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser

""" 
Hey ! If you're here, you must be interested in what's inside this script.


The whole ArgumentParser stuff is what handles the -c, -co, -p and -po from the command line, 
for inputs and outputs.
"""

parser = ArgumentParser(description=""" Add antifreeze particles
Used within the INSANE tutorial""")

# Named arguments
parser.add_argument("-c", "--gro", help="The name of the input .gro file", required=True)
parser.add_argument("-co", "--outgro", help="The name of the output .gro file", required=True)
parser.add_argument("-p", "--top", help="The name of the input .top file", required=True)
parser.add_argument("-po", "--outtop", help="The name of the output .top file", required=True)
args = parser.parse_args()

# Input / Output
gro = args.gro
outgro = args.outgro
top = args.top
outtop = args.outtop

######################## The script ########################

#### Start with the topology and decide how many antifreeze we'll add

# Keep track of the number of ions
ion_count = 0

# This time, we'll write the new topology line by line
# The output topology will be
out_top_ = open(outtop, "w")

# And browse the input topology line by line
with open(top, "r") as openfileobject:
    for line in openfileobject:
            
        # A small thing to keep track of the number of ions, which will ease the next step
        if line.startswith("NA+") == True or line.startswith("CL-") == True:
            out_top_.write(line)
            
            # Add to the ion count
            ion_count += int(line.split()[1])
            
        # Here it's basic - write everything and do stuff if that's the line dealing with waters
        elif line.startswith("W       ") == False:
            out_top_.write(line)
            
        # Else it means that's the line we want, with waters
        else:
            
            # Split the line - btw, I'm always using "l" + variable name when splitting
            lline = line.split()
            
            # The current number of waters is
            W_current = int(lline[1])
            
            # We want 10% of that
            # Here, this is an euclidean division since both numbers are int
            WF_number = W_current / 10
            
            # Deduce the remaining number of W
            W_number = W_current-WF_number
            
            # Write the two lines
            W_line = "W            {:d}\n".format(W_number)
            WF_line = "WF           {:d}\n".format(WF_number)
            out_top_.write(W_line + WF_line)
            
# Close the output topology
out_top_.close()

#### Now the trickier part, the .gro

# We want to replace the last WF_number of W into WF
# First get a list of lines of the .gro
in_gro = open(gro, "r").readlines()

# The trick here is to select only the last WF_number of lines, + the ions
# Luckily, we know the number of ions, which is ion_count
# There are also 2 lines in the end (the box size and an empty \n)
# Which means we can just select the last 2+ion_count+WF_number lines

# The length of the file is
gro_length = len(in_gro)

# The magic number
magic_number = gro_length - (2+ion_count+WF_number)

# Cut this file into 2 variables
W_part = in_gro[:magic_number]
WF_part = in_gro[magic_number:]

# Cat the parts
W_part = "".join(W_part)
WF_part = "".join(WF_part)

# Replace the W into WF in two steps
# First replace "W " with "WF"
# Then replace " W" with "WF"
# This way we don't mangle the columns within the .gro
WF_part = WF_part.replace("W ", "WF")
WF_part = WF_part.replace(" W", "WF")

# Write everything into the new .gro
out_gro_ = open(outgro, "w")
out_gro_.write(W_part + WF_part)
out_gro_.close()










