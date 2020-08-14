import matplotlib.pyplot as plt
import numpy as np
import torch
import torchvision
import cv2

def show_img(img, size):
    plt.figure(figsize=(size, size)) 
    npimg = img.numpy()
    npimg = np.clip(npimg, 0., 1.)
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show() 

def show_random_images(dataset, size):
  # get some random training images
  dataiter = iter(dataset)
  bg, image, mask, depthmap = dataiter.next()
  img_list = range(5, 10)
  # show images
  print('bg:', bg.shape)
  show_img(torchvision.utils.make_grid(bg[img_list]), size)
  print('image:', image.shape)
  show_img(torchvision.utils.make_grid(image[img_list]), size)
  print('mask:', mask.shape)
  show_img(torchvision.utils.make_grid(mask[img_list]), size)
  print('depthmap:', depthmap.shape)
  show_img(torchvision.utils.make_grid(depthmap[img_list]), size)


def plot_metric(data1, data2, metric, label1, label2):
  plt.plot(data1)
  plt.plot(data2)
  plt.ylabel(metric)
  plt.xlabel('epoch')
  plt.legend([f'{label1}', f'{label2}'], loc='upper left')
  plt.show()
