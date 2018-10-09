#!/bin/bash
#PBS -q debug
#PBS -l select=10:ncpus=32:mpiprocs=32 
#PBS -l walltime=1:00:00
#PBS -j oe
#PBS -A ONRDC17423173
cd $PBS_O_WORKDIR
module load espresso
PARA_PREFIX="aprun -n 320"
############################################################################
unalias rm
path=`pwd`;
# how to run executables
PW_COMMAND_SCF="$PARA_PREFIX  pw.x -nk 4 -nd 80"
length="8.386494280";
for j in `seq `
do
	rm -rf $path/angle$j
	mkdir $path/angle$j
	cd $path/angle$j
	cp -rf ../psudo .
	cp ../BZO.in .
	cp ../rotate.py .
	./rotate.py $j BZO.in >gg.in
 $PW_COMMAND_SCF < gg.in > ./scf.out
done
