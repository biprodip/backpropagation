import numpy as np
import matplotlib.pyplot as mp

# X = (hours sleeping, hours studying), y = score on test
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
T = np.array(([92, 8], [86, 14], [11, 89]), dtype=float)

# scale units
X = X/np.amax(X, axis=0) # maximum of X array
T = T/100 # max test score is 100
X=X.T;
T=T.T;
[d,n]=X.shape; #N=no of samples    D=dimension of data

#network_structure
inputNodes = 2
hiddenNodes = 3
outputNodes = 2
eta_ih=1;
eta_ho=1;
nEpoch=500;

#weights initialization
W_IH = np.random.randn(inputNodes,hiddenNodes) 
W_HO = np.random.randn(hiddenNodes,outputNodes) 
W_IH = W_IH.T # (3x2) weight matrix from input to hidden layer
W_HO = W_HO.T # (2x3) weight matrix from hidden to output layer

Y_H=np.empty([hiddenNodes, n]);
Y_O=np.empty([outputNodes, n]);

loss=np.array([]);
for i in range(nEpoch): # trains the NN 1,000 times
  fpResult=forwardPass(X);
  backwardPass(X,T,Y_O,Y_H);
  loss=np.append(loss,np.mean(error(T,Y_O)));
  
  #print "Input: \n" + str(X) 
  #print "Actual Output: \n" + str(T) 
  print("Predicted Output: \n" + str(fpResult))
  print("Loss: \n" + str(np.mean(error(T,Y_O)))) # mean sum squared loss
  print("\n")
  
mp.plot(np.array([i for i in range(nEpoch)]),loss)
mp.xlabel("Epoch")
mp.ylabel("Loss")
  
