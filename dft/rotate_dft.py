#!/usr/bin/env python
import numpy as np
import math
import sys
filein=sys.argv[2];
infile_fs=open(filein,"r");
inlines=infile_fs.readlines();
length=len(inlines);
infile_fs.close();
infile_fs=open(filein,"r");
cell_p=8.386494280;
angle=float(sys.argv[1]);
delta=math.tan(angle/180.0*math.pi)*cell_p/4;
inline=infile_fs.readline();
while(inline):
	if inline.find("ATOMIC_POSITIONS")!=-1:
		print inline.replace('\n','');
		inline=infile_fs.readline();
		while inline:
			stream=inline.split();
			if stream[0]=='O' and round(float(stream[3])/cell_p*4)==1:
				n=round(float(stream[1])/cell_p*4);
				k=round(float(stream[2])/cell_p*4);
				if n==1 and k==0:
					print 'O'+"\t"+str(float(stream[1])-delta)+"\t"+stream[2]+"\t"+stream[3];
				elif n==3 and k==0:
					print 'O'+"\t"+str(float(stream[1])+delta)+"\t"+stream[2]+"\t"+stream[3];
				elif n==0 and k==1:
					print 'O'+"\t"+stream[1]+"\t"+str(float(stream[2])+delta)+"\t"+stream[3];
				elif n==2 and k==1:
					print 'O'+"\t"+stream[1]+"\t"+str(float(stream[2])-delta)+"\t"+stream[3];
				elif n==1 and k==2:
					print 'O'+"\t"+str(float(stream[1])+delta)+"\t"+stream[2]+"\t"+stream[3];
				elif n==3 and k==2:
					print 'O'+"\t"+str(float(stream[1])-delta)+"\t"+stream[2]+"\t"+stream[3];
				elif n==0 and k==3:
					print 'O'+"\t"+stream[1]+"\t"+str(float(stream[2])-delta)+"\t"+stream[3];
				elif n==2 and k==3:
					print 'O'+"\t"+stream[1]+"\t"+str(float(stream[2])+delta)+"\t"+stream[3];
			elif stream[0]=='O' and round(float(stream[3])/cell_p*4)==3:
				n=round(float(stream[1])/cell_p*4);
				k=round(float(stream[2])/cell_p*4);
				if n==1 and k==0:
					print 'O'+"\t"+str(float(stream[1])+delta)+"\t"+stream[2]+"\t"+stream[3];
				elif n==3 and k==0:
					print 'O'+"\t"+str(float(stream[1])-delta)+"\t"+stream[2]+"\t"+stream[3];
				elif n==0 and k==1:
					print 'O'+"\t"+stream[1]+"\t"+str(float(stream[2])-delta)+"\t"+stream[3];
				elif n==2 and k==1:
					print 'O'+"\t"+stream[1]+"\t"+str(float(stream[2])+delta)+"\t"+stream[3];
				elif n==1 and k==2:
					print 'O'+"\t"+str(float(stream[1])-delta)+"\t"+stream[2]+"\t"+stream[3];
				elif n==3 and k==2:
					print 'O'+"\t"+str(float(stream[1])+delta)+"\t"+stream[2]+"\t"+stream[3];
				elif n==0 and k==3:
					print 'O'+"\t"+stream[1]+"\t"+str(float(stream[2])+delta)+"\t"+stream[3];
				elif n==2 and k==3:
					print 'O'+"\t"+stream[1]+"\t"+str(float(stream[2])-delta)+"\t"+stream[3];
			else:
				print inline.replace('\n','');
			inline=infile_fs.readline();
	else:
		print inline.replace('\n','');
	inline=infile_fs.readline();
