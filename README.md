# Linear_regression-using-BGD


Batch Gradient Descent(BGD) is an approach to find the least squared error which is defined by a Cost Function.
In this method, we have to come across the training examples in the data set multiple times. The whole training
set is considered as a Batch which is visited again and again over several epochs until convergence starts and 
tend to become significant.

The merits of using this approach lie in the fact that BGD converges to exact minima and the path travelled in the 
process is smoother. You don't necessarily need random data set as required in SGD(which you will come across in 
another folder in repository). Here we consider sum or an average of the whole set to find the cost function and the error
associated to a particular example.

Basic Definitions:

1. Epochs represent the no. of times we visit the data set.

2. Rate represents the size of step we take to reach minima (confidence) also called alpha.

3. Cost Function defines the relation for the Least Squared Error.

4. Bias term refers to the intercept term in the hypothesis equation.


Limitation of using this approach:

It pays visit to the whole set again and again and approach uses more complex time so it is not as faster as SGD.
