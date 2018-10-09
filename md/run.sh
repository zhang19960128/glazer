#!/bin/bash
#PBS -q debug
#PBS -l select=3:ncpus=32:mpiprocs=32 
#PBS -l walltime=1:00:00
#PBS -j oe
#PBS -A ONRDC17423173
cd $PBS_O_WORKDIR
path_lmp=/u/jiahaoz/lammps-17Dec13/src;
LMP="aprun -n 96 ${path_lmp}/lmp_crayxe6"
path=`pwd`
for j in `seq -10 1 10`
do
	rm -rf $path/angle$j
	mkdir $path/angle$j
	cd $path/angle$j
	cp ../test.lammpsinput .
	cp ../mixdata.BTO .
	cp ../rotate.py .
	cp mixdata.BTO gg.in
  ./rotate.py $j mixdata.BTO >temp
	cp temp mixdata.BTO
 $LMP < test.lammpsinput > ./out
done
