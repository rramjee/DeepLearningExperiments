

## 1. Image Normalization
Image Normalization is first step to be taken care before feeding the image to the CNN layers as input.  Image normalization  ensures that each input pixel has a similar data distribution. This makes convergence faster while training the network. Basically if the pixel value is between 0 to 255, this ensures that the pixel value is between 0 to 1. 
## 2. Receptive Field		
The receptive field is defined as the region in the input space that a particular CNN's feature is looking at . Need to look at the data of the training set and decide on the  optimum receptive field for the problem in hand. the last layer in the network should be able to view the entire subject in its receptive field to make prediction.
## 3. 3*3 convolutions
Need to decide on the number of 3*3 convolutions required to get required features in a image and to create a rich feature map to help with correct classification.
## 4. How many Layers 
will need to decide on the number of layers in the architecture keeping in mind the 
	1. problem at hand or the goal
	2. Hardware specs 
## 5. Kernels and how do we decide the number of kernels
Kernels are filters that are used convolute the input images in a CNN to learn features ranging from edges and gradients to entire image.
You can use as many kernels to convolute over a particular layer of cnn but adding too many kernels will only increase the number of parameters used by your neural network. Each Kernel will learn a channel of information from the input layer. So, need to decide on optimum number of kernels to be used in every layer that are sufficient enough to learn the features.
## 6. Concept/Position of Transition Layers
Transition layers are layers in a network which is build of max pooling and 1*1 convolution layer. The idea of transition layer is for dimensionality reduction or downsize an image. It is recommended to use a transition layer after every 3 convolution layers and not at least 3 layers before output layer. 
## 7.	1*1 convolutions
The 1*1 convolutions is also used for dimensionality reduction of the input image. In most cases, it is used to reduce the number of channels and there by number of parameters in a network. Also, by keeping the pixel or feature size of the image the same, reducing the channels allows the layer to learn more sophisticated information from the image by compounding information from multiple channels.

## 8.  MaxPooling, Position of max pooling
Max pooling helps to extracts the sharpest features of an image and also progressively reduce the spatial size of the representation to reduce the amount of parameters and computation in the network. So given an image, the sharpest features are the best lower-level representation of an image.
## 9. Distance of max pooling from prediction:
Last max pooling should be at least 4 or 5 layers before the prediction layer to ensure that we do not loose any learned features in the last few layers.
## 10. Batch Size:
The total images in a training set is split in equal number of batches and trained to speed up the training. If there are n number of images in a batch, there will be n forward propagation and 1 back propagation per batch, The number of images per batch should usually consist of images from all the possible classes to ensure that training accuracy is good. 
## 11. Effect of Batch Size:
Ideally batch size should be dependant on a dataset. 
## 12. Batch Normalization:
Batch normalization is a process of getting all the inputs within a range of values. basically all the values are subtracted by the mean of values and divided by standard deviation. This helps in speeding up the training and also reduces overfitting to an extent.
## 13. The distance of Batch Normalization from Prediction:
Batch Normalization can be before or after any layer in the network except before the prediction layer.
## 14. Relu and Softmax:
Relu is used as activation function for adding non-lineraity to all the hidden layers of the CNN. This addresses the problem of exploding and vanishing gradients faced in the sigmoid or tanh activation functions. This ensures that all negative values are set to 0 and x value between 0 to x.
Softmax is used as activation function in the last layer to predict the classes. Softmax is a probablity like function that outputs the sum of probablity of the all  the classes to 1.  
## 15. Number of Epochs and when to increase them:
An epoch is one complete pass through the training set. number of epochs is a parameter in model.fit function that determines the number of passes through the training set and accuracy is calculated at the end of every epoch. You may need to increase the number of epoch until expected accuracy is reached. 
## 16. DropOut and When do we introduce DropOut, or when do we know we have some overfitting:
Dropout is method to reduce overfitting. you may need to introduce dropout if there is variance between training accuracy and test accuracy. dropout is a process of turning off some of the neurons randonly decided by the dropout rate. a dropout of 0.2 means that 20% of the activations or neuron are turned off during prediction. By this way the network learns to predict without getting to see part of the image. But, this is applied only during training and all of them are turned off during test set.
## 17. Learning Rate:
Learning rate is parameter that defines the measure or step size by which the weights and bias values need to adjusted after every back back prop. Setting a constant learning rate can make training very slow as the weights get adjusted in a very slow manner even if the current accuracy is way off and the cost is very high.
## 18. LR schedule:
LR Schedule is a function that defines how the learning rate are changed over time. It is usually passed as parameter to optimizer functions such as Adam, SGD, etc. The learning rates are changes as we progress through training. usually higher training rates are used in the beginning and smaller rates are used as we go towards global minima.
## 19. Loss Function:
A cost function is a measure of "how good" a neural network did with respect to it's given training sample and the expected output. Usually Categorical Cross entropy is used a loss function for classification problems.
## 20. Adam vs SGD:
These are optimization functions used to adjust the learning rates. Adam is considered more sophisticated optimizer function but generally SGD works well too. I prefer using Adam as an optimizer function.
## 21. How do we know our network is not going well, comparatively, very early:
Usually the first 10 to 20 epochs is a good measure of network. If the training accuracy or test accuracy is not improving over the first 10 to 20 epochs, then it means the network is not doing well and need to adjust parameters and hyper parameters accordingly.
## 22. When do we add validation checks:
Validation checks are usually to tune the parameters used during training and it is required when the model is not doing well during testing. Also, when the test accuracy is very bad compared to the training set.


