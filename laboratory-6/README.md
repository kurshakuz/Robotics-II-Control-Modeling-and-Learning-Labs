# Laboratory 6.

### Initial architecture 

![](./images/17-19-58.png)
![](./images/17-20-11.png)

### Additional FC Layer

![](./images/17-21-36.png)
![](./images/17-21-48.png)

### Switch ReLu to LeakyReLu

![](./images/17-22-15.png)
![](./images/17-22-34.png)


### 512-1024-512 architecture
This architecture has proven to show the best performance on test data.
![](./images/17-06-13.png)
![](./images/17-06-28.png)

### 512-1024-1024-512 architecture
Additional layer was added to test if architecture will perform better. Showed worse results.
![](./images/17-07-16.png)
![](./images/17-07-30.png)

### 1024-2048-1024 architecture
Additional neurons were added to test if the architecture will perform better. Showed worse results.
![](./images/17-11-44.png)
![](./images/17-08-54.png)


### Tanh activation function
Changed to see if tanh activation function will perform better. Showed worse results.
![](./images/17-12-25.png)
![](./images/17-11-56.png)


### Final architecture + change of training parameters
This is the final architecture. Best results. Mean error 6.8%.
![](./images/17-38-58.png)
![](./images/17-41-39.png)
Finally change number of training samples, number of epochs, and minibatch sizes. Showed even better results and mean error of 3%.
![](./images/17-43-10.png)
![](./images/17-43-25.png)








