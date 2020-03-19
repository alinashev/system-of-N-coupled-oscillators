import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['animation.ffmpeg_path'] = 'ffmpeg.exe'
import matplotlib.animation as animation
n=25
t0 = 1000
dt=0.005
m=1
k=5
q=1
ANIM = []
ANIMT=[]
Ampl=0.05
w=1

class Oscil:
    x=0
    y=0
    Vy=0
    q=0
    k=0
    def printX(self):
        for i in range(0,n):
            print(A[i].x)
def F(left,center,right):
    return -k*center.x+q*(left.x-center.x)+q*(right.x-center.x)
A=[Oscil() for i in range(0,n)]
for j in range(0,n):
    A[j].y=j
    A[j].q=80
    A[j].k=0.01
for t in range(0,int(t0/dt)):
    if t*dt<2*np.pi:
        A[0].x= Ampl*np.sin(w*t*dt)
    else:
        A[n-1].x=0
        A[0].x=0
    for j in range(1, n-1):
        A[j].Vy=A[j].Vy+dt*(F(A[j-1],A[j],A[j+1]))
        A[j].x=A[j].x+dt*A[j].Vy
    data=[]
    if t%100==0:
        for l in range(0,n):
            data.append([])
            data[l].append(A[l].y)
            data[l].append(A[l].x)
        ANIM.append(data)
        ANIMT.append(t*dt)
def update(i):
    scat.set_offsets(ANIM[i])
fig,ax = plt.subplots()
X=[]
Y=[]
for j in range(0,n):
    X.append(A[j].x)
    Y.append(A[j].y)

#print(X)
#print(Y)


scat=ax.scatter(Y,X,c="black",s=25)

#fig.set_figwidth(8)
#fig.set_figheight(8)

ani=animation.FuncAnimation(fig,update,frames=int(len(ANIM)),interval=1)
Writer=animation.writers['ffmpeg']
writer=Writer(fps=15,metadata=dict(artist='Yamasato'),bitrate=1800)
ani.save('osc.mp4',writer=writer)
plt.show()