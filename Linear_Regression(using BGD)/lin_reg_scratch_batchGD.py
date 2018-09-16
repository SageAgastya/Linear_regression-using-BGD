import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:

    def __init__(self):
        #q0 and q1 are parameters defining best fit 
        self.q0=0.0
        self.q1=0.0
        self.rate=0.001
        self.epoch=10000


    def train_by_converge(self,x,y):  #training model
        for i in range(self.epoch):
            yp=(self.q1*x+self.q0)
            cost=sum((y-yp)**2)*0.5
            min_cost_bias=-sum(1*(y-yp))
            min_cost_slope=-sum(x*(y-yp))
            self.q0=self.q0-(self.rate*min_cost_bias)
            self.q1=self.q1-(self.rate*min_cost_slope)
            print("Iteration: ", i+1, " Cost: ", cost)
        return cost,self.q0,self.q1,yp

    def test(self,test_x):   #testing using best fit
        predicted_y=(test_x*self.q1)+self.q0
        return predicted_y

x=np.array([4,2,6,3,7])
y=np.array([4,3,7,2,9])
lr=LinearRegression()    #object creation
cost,b,m,yp=lr.train_by_converge(x,y)
print cost,m,b
print lr.test(x)
plt.scatter(x,y)
plt.plot(x,yp,"r")
plt.show()
