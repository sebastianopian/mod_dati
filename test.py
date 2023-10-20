import math 
dx= math.pi/16; sa=0; sb=0; cov=0; m=0
aa=-12; bb=-12; max= -10000000000.0; i = 0
fi=[]; al=[]; bl=[]; a=0; b=0
isto=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

fi = open("dat.txt", "r").readlines()

while i < 4999:
    ind =  int(float(fi[i])/dx)
    isto[ind]=int((isto[ind] +1))
    i=i+1

i=0
num=open("textfile.txt",'w').close()
num=open("textfile.txt",'a')

while i< 31:
    num.write(str(dx*(i-1)+dx/2)+"  " + str(isto[i]) +"  "+ str(math.sqrt(isto[i]))+"\n")
    i=i+1
    
num.close()
i=0

while i < 4999:
    a=a+2*(math.cos(float(fi[i])))/5000
    b=b+ 2* (math.sin(float(fi[i])))/5000
    i=i+1

i=0

while i<4999:
    sa=sa + (math.cos(float(fi[i]))-a/2)**2
    sb=sb + (math.sin(float(fi[i]))-b/2)**2
    cov=cov +(math.cos(float(fi[i]))-a/2)*(math.sin(float(fi[i]))-b/2)
    i=i+1

sa=(4*sa/(5000*4999))**0.5
sb=(4*sb/(5000*4999))**0.5
cov= cov/(4999*5000)
corr= cov/(sa*sb)
print('--------------------------')
print('Metodo dei valori medi')
print('Stima di a:', a)
print('Stima di b:', b)
print('Stima della deviazione standard di a:', sa)
print('Stima della deviazione standard di b:', sb)
print('Stima del coeff. di correlazione:', corr)
print('-------------------------------')
