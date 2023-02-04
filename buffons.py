import random
import matplotlib.pyplot as plt
import numpy as np

random.seed(400)
N=10000
hit=0
x=[]
y=[]
hit_d=[]
hit_theta=[]
miss_d=[]
miss_theta=[]

for i in range(1,N+1):
  #generate(d,theta)
  d=random.uniform(0,1)
  theta=random.uniform(0,np.pi/2)
  #print(d,theta)

  if d<=(1/2)*np.sin(theta):
    hit=hit+1
    hit_d.append(d)
    hit_theta.append(theta)
  else:
    miss_d.append(d)
    miss_theta.append(theta)

  if (i%100==0):
    # i= number thown needle
    x.append(i)

    est_pi=i/hit
    y.append(est_pi)

print(est_pi)
plt.scatter(x,y)

