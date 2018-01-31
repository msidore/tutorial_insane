# Why

A simple tutorial to build a MARTINI membrane with or without a protein using the INSANE tool. Following the building of the membrane, a short minimization run will be done. 

# Prerequisite & notes

All files are located in the insane_tutorial subdirectory. 

You will need:
* The insane.py script (provided)
* The martinize.py script (provided)
* DSSP (provided)
* The MARTINI force-field files (provided)
* A .pdb of your membrane protein (provided)
* VMD, to visualize the structures ! http://www.ks.uiuc.edu/Research/vmd/
* If you want to further do simulations/minimization, GROMACS http://www.gromacs.org/

Simulation parameters are taken from:
* D.H. de Jong, S. Baoukina, H.I. Ingólfsson, Marrink S.J. Martini straight: boosting performance using a shorter cutoff and GPUs. Comput. Phys. Commun., 199:1-7, 2016. doi:10.1016/j.cpc.2015.09.014

Insane is published here:
* T.A. Wassenaar, H.I. Ingólfsson, R.A. Böckmann, D.P. Tieleman, S.J. Marrink. Computational lipidomics with insane: a versatile tool for generating custom membranes for molecular simulations. JCTC, 11:2144–2155, doi:2015.10.1021/acs.jctc.5b00209
