import random
from matplotlib import pyplot as plt

Arand=0
Nrand=0
GaussAdd=0
GaussFac=0

def InitGauss(seed):
    global Arand
    global Nrand
    global GaussAdd
    global GaussFac
    Nrand=4
    Arand= (2**31) -1
    GaussAdd= (3*Nrand)**0.5
    GaussFac=2*GaussAdd/(Nrand*Arand)
    random.seed(seed)
    return None

def Gauss():
    global Arand
    global Nrand
    global GaussAdd
    global GaussFac
    sum=0
    i=1
    while i<Nrand+1:
        sum+=random.uniform(0,Arand)
        i+=1
    return (GaussFac*sum-GaussAdd)

def WhiteNoiseBM(x,n,seed):
    x[0]=0
    InitGauss(seed)
    i=0
    while i<n:
        x[i]=x[i-1]+Gauss()/(n-1)
        i+=1
    return None
        
def GaussianNoise(n):
    y=[]
    for i in range(0,n):
        y.append(Gauss()/n**2)#*i)   
    return y

#Datos del programa
fig, ax = plt.subplots(1,2,layout='constrained')
n= int(input("Digite el tamaño del set de datos: "))
seed=random.uniform(0,10000)
y=[0]*n
WhiteNoiseBM(y,n,seed)
x=list(range(n))
    
ax[0].plot(x,y,label="Brown Noise")

ax[1].plot(x,GaussianNoise(n),label="White Noise",color="r")
ax[0].legend()
ax[1].legend()
fig.suptitle('Noise')
plt.show()
print("YA ACABO")