
import argparse
import logging
import os
import numpy as np
import torch
import torchvision
import torchvision.transforms as transforms
import zipfile
import requests
from tqdm import notebook
from io import StringIO,BytesIO
from albumentations import PadIfNeeded, IAAFliplr, Compose, RandomCrop, Normalize, HorizontalFlip, Resize, ToFloat, Rotate, Cutout
from albumentations.pytorch import ToTensor
from torch.utils.data import Dataset, random_split
from PIL import Image
from utils import dice
from utils import visualize
from model import dnn
import torchvision
import matplotlib.pyplot as plt

import torch
from torch.autograd import Variable



def get_args():
    parser = argparse.ArgumentParser(description='Predict masks & depthmap from input images',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--model', '-m',
                        metavar='FILE',
                        help="Specify the file in which the model is stored")

    parser.add_argument('--background', '-bg', metavar='INPUT', nargs='+',
                        help='filename of input background image', required=True)

    parser.add_argument('--image', '-img', metavar='INPUT', nargs='+',
                        help='filename of input image')

    return parser.parse_args()



def load_image(bgfile, imgfile, dim):
  
  mean = (0.50169254, 0.51531572, 0.38720035)
  std = (0.25096876, 0.2417532, 0.28520041)
  
  preprocess = transforms.Compose([
                                   transforms.Resize(dim),
                                   transforms.ToTensor(),
                                   transforms.Normalize(mean, std)
                                   ])
  
  bg_pil = Image.open(bgfile)
  bg_tensor = preprocess(bg_pil).float()
  bg_tensor = bg_tensor.unsqueeze_(0)
  bg = Variable(bg_tensor)

  img_pil = Image.open(imgfile)
  img_tensor = preprocess(img_pil).float()
  img_tensor = img_tensor.unsqueeze_(0)
  image = Variable(img_tensor)

  return bg, image

def load_image_nonorm(bgfile, imgfile, dim):
  
  mean = (0.50169254, 0.51531572, 0.38720035)
  std = (0.25096876, 0.2417532, 0.28520041)
  
  preprocess = transforms.Compose([
                                   transforms.Resize(dim),
                                   transforms.ToTensor(),
                                   ])
  
  bg_pil = Image.open(bgfile)
  bg_tensor = preprocess(bg_pil).float()
  bg_tensor = bg_tensor.unsqueeze_(0)
  bg = Variable(bg_tensor)

  img_pil = Image.open(imgfile)
  img_tensor = preprocess(img_pil).float()
  img_tensor = img_tensor.unsqueeze_(0)
  image = Variable(img_tensor)

  return bg, image  


def predict_images(modelpath, filepath, bgfile, imgfile):
  dim = 64
  dispnorm = False
  bg, image = load_image(filepath, bgfile, imgfile, dim)
  bg_disp, image_disp = load_image_nonorm(filepath, bgfile, imgfile, dim)
  
  if modelpath:
    inchannels = 3
    model = dnn.CustomNet15(inchannels)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    checkpoint = torch.load(modelpath)
    model.load_state_dict(checkpoint['state_dict'])
    model.to(device=device)
  #  optimizer.load_state_dict(checkpoint['optimizer'])
  #  epoch = checkpoint['epoch']

  model.eval()
  bg, image = bg.to(device), image.to(device)
  predmask, preddepth = model(bg, image)
  visualize.show_img(torchvision.utils.make_grid(bg_disp), 3)
  visualize.show_img(torchvision.utils.make_grid(image_disp), 3)
  if dispnorm:
    visualize.show_img(torchvision.utils.make_grid(bg.detach().cpu()), 3)
    visualize.show_img(torchvision.utils.make_grid(image.detach().cpu()), 3)
  visualize.show_img(torchvision.utils.make_grid(predmask.detach().cpu()), 3)
  visualize.show_img(torchvision.utils.make_grid(preddepth.detach().cpu()), 3)

#if __name__ == "__main__":
#    args = get_args()
#    bg_file = args.background
#    img_file = args.image
#    modelpath = args.model

#    inchannels = 3
#    net = dnn.CustomNet15(inchannels)

#    logging.info("Loading model...")

#    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#    logging.info(f'Using device {device}')
#    net.to(device=device)
#    checkpoint = torch.load(modelpath)
#    net.load_state_dict(checkpoint['state_dict'])

#    logging.info("Model loaded !")
#    logging.info("\nPredicting image...")
#    predict_images(bg_file, img_file, net, device, dim=64, dispnorm=False)