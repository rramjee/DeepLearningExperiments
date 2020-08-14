from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
steps = 7
#iter = [0,5,10,15,20,25]
#lr = [0,1e2,0,1e2,0,1e2]
iter = [None] * steps
lr = [None] * steps


for i in range(steps):
    #print(i)
    if i==0:
        iter[i] = 0
    else:
        iter[i] = iter[i-1] + 5

    if i%2 == 0:
        lr[i] = 0
    else:
        lr[i] = 1e-2

plt.xlabel('Iterations')
plt.ylabel('Learning Rate')
plt.title('Cyclic LR')
plt.plot(iter,lr)
#plt.legend()
plt.tight_layout()
plt.show()