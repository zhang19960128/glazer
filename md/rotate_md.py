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
 if inline.find("Atoms")!=-1:
  print inline.replace('\n','');
  inline=infile_fs.readline();
  while inline:
   stream=inline.split();
   if inline.find("Angles")!=-1:
    print inline.replace('\n','');
    inline=infile_fs.readline();
    while inline:
     print inline.replace('\n','');
     inline=infile_fs.readline();
   elif len(stream)==0:
    print ''
   elif stream[2]=='3' and round(float(stream[6])/cell_p*4)==1:
    n=round(float(stream[4])/cell_p*4);
    k=round(float(stream[5])/cell_p*4);
    if n==1 and k==0:
     print stream[0]+' 1 3 -0.93866'+" "+str(float(stream[4])-delta)+" "+stream[5]+" "+stream[6];
    elif n==3 and k==0:
     print stream[0]+' 1 3 -0.93866'+" "+str(float(stream[4])+delta)+" "+stream[5]+" "+stream[6];
    elif n==0 and k==1:
     print stream[0]+' 1 3 -0.93866'+" "+stream[4]+" "+str(float(stream[5])+delta)+" "+stream[6];
    elif n==2 and k==1:
     print stream[0]+' 1 3 -0.93866'+" "+stream[4]+" "+str(float(stream[5])-delta)+" "+stream[6];
    elif n==1 and k==2:
     print stream[0]+' 1 3 -0.93866'+" "+str(float(stream[4])+delta)+" "+stream[5]+" "+stream[6];
    elif n==3 and k==2:
     print stream[0]+' 1 3 -0.93866'+" "+str(float(stream[4])-delta)+" "+stream[5]+" "+stream[6];
    elif n==0 and k==3:
     print stream[0]+' 1 3 -0.93866'+" "+stream[4]+" "+str(float(stream[5])-delta)+" "+stream[6];
    elif n==2 and k==3:
     print stream[0]+' 1 3 -0.93866'+" "+stream[4]+" "+str(float(stream[5])+delta)+" "+stream[6];
   elif stream[2]=='3' and round(float(stream[6])/cell_p*4)==3:
    n=round(float(stream[4])/cell_p*4);
    k=round(float(stream[5])/cell_p*4);
    if n==1 and k==0:
     print stream[0]+' 1 3 -0.93866'+" "+str(float(stream[4])+delta)+" "+stream[5]+" "+stream[6];
    elif n==3 and k==0:
     print stream[0]+' 1 3 -0.93866'+" "+str(float(stream[4])-delta)+" "+stream[5]+" "+stream[6];
    elif n==0 and k==1:
     print stream[0]+' 1 3 -0.93866'+" "+stream[4]+" "+str(float(stream[5])-delta)+" "+stream[6];
    elif n==2 and k==1:
     print stream[0]+' 1 3 -0.93866'+" "+stream[4]+" "+str(float(stream[5])+delta)+" "+stream[6];
    elif n==1 and k==2:
     print stream[0]+' 1 3 -0.93866'+" "+str(float(stream[4])-delta)+" "+stream[5]+" "+stream[6];
    elif n==3 and k==2:
     print stream[0]+' 1 3 -0.93866'+" "+str(float(stream[4])+delta)+" "+stream[5]+" "+stream[6];
    elif n==0 and k==3:
     print stream[0]+' 1 3 -0.93866'+" "+stream[4]+" "+str(float(stream[5])+delta)+" "+stream[6];
    elif n==2 and k==3:
     print stream[0]+' 1 3 -0.93866'+" "+stream[4]+" "+str(float(stream[5])-delta)+" "+stream[6];
   else:
    print inline.replace('\n','');
   inline=infile_fs.readline();
 else:
  print inline.replace('\n','');
 inline=infile_fs.readline();
