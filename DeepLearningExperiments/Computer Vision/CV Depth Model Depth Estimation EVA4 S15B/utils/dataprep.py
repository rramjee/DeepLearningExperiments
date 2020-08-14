import numpy as np
import torch
import os
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



class album_Compose:
    def __init__(self, mean, std, imgdim = 64, augmentations=True):
        if augmentations:
            self.albumentations_transform = Compose([
                                                     Resize(imgdim, imgdim, interpolation=1, always_apply=False, p=1),
                                                     Normalize(mean=mean, std=std,),
                                                     ToTensor()
                                                     ])
        else:
            self.albumentations_transform = Compose([
                                                     Resize(imgdim, imgdim, interpolation=1, always_apply=False, p=1),
                                                     Normalize(mean=mean, std=std,),
                                                     ToTensor()
                                                     ])

    def __call__(self, img):
        img = np.array(img)
        img = self.albumentations_transform(image=img)['image']
        return img

class FGBGCustomDatasetSubset(Dataset):
  def __init__(self, subset):
    self.subset = subset
    self.length = len(self.subset)

  def __getitem__(self, index):
    bg, fgbg, mask, depthmap = self.subset[index]
    return bg, fgbg, mask, depthmap

  def __len__(self):
    return self.length  

class FGBGCustomDataset(Dataset):
  def __init__(self, path, datalen, image_transform, mask_transform, depth_transform):
    self.path = path
    self.files = list(range(1, datalen))
    self.length = len(self.files)
    self.image_transform = image_transform
    self.mask_transform = mask_transform
    self.depth_transform = depth_transform

  def __getitem__(self, index):
    #Get the index of BG based on the index of image
    new_index = index + 1
    if new_index%4000 == 0:
      bg_index = int(new_index/4000)
    else:
      bg_index = int(new_index/4000)+1   
    bg = Image.open(self.path+'bg/bg_'+str(bg_index)+'.jpg')
    fgbg = Image.open(self.path+'image/fg_bg_'+str(new_index)+'.jpg')
    mask = Image.open(self.path+'mask/fg_bg_mask_'+str(new_index)+'.jpg')
    depthmap = Image.open(self.path+'depthmap/depth_'+str(new_index)+'.jpg')
    
    if self.image_transform:
      bg = self.image_transform(bg)
      fgbg = self.image_transform(fgbg)
    if self.mask_transform:  
      mask = self.mask_transform(mask)
    if self.depth_transform:  
      depthmap = self.depth_transform(depthmap)

    return bg, fgbg, mask, depthmap

  def __len__(self):
    return self.length


def load_data(path, datalen, splitsize, mean, std, imgdim, batchsize=512, numworkers=4, albumentations=False):
  if albumentations:
    print("Using Albumentations")
    image_transform = album_Compose(mean, std, imgdim, augmentations=True)
    mask_transform = album_Compose(mean, std, imgdim, augmentations=False)
    depth_transform = album_Compose(mean, std, imgdim, augmentations=False)
  else:
    print("Not Using Albumentations")
    image_transform = transforms.Compose([
                                          transforms.Resize((imgdim, imgdim)),
                                          #transforms.Grayscale(num_output_channels=1),
                                          transforms.ToTensor(),
                                          transforms.Normalize(mean, std)
                                         ])
    
    mask_transform = transforms.Compose([
                                          transforms.Resize((imgdim, imgdim)),
                                          transforms.Grayscale(num_output_channels=1),
                                          transforms.ToTensor()
                                        ])
    
    depth_transform = transforms.Compose([
                                          transforms.Resize((imgdim, imgdim)),
                                          transforms.ToTensor()
                                        ])


  dataset = FGBGCustomDataset(path, 
                              datalen, 
                              image_transform=image_transform, 
                              mask_transform=mask_transform,
                              depth_transform=depth_transform
                              )
  train_len = len(dataset)*splitsize//100
  test_len = len(dataset) - train_len 

  print("Train Length: ", train_len, "Test Length: ", test_len)
  
  train_set, test_set = torch.utils.data.random_split(dataset, [train_len, test_len])
    
  train_dataset = FGBGCustomDatasetSubset(train_set)
  test_dataset = FGBGCustomDatasetSubset(test_set) 
  
  random_seed = 42

  # CUDA?
  cuda = torch.cuda.is_available()
  print("CUDA Available?", cuda)

  # For reproducibility
  torch.manual_seed(random_seed)

  if cuda:
    torch.cuda.manual_seed(random_seed) 
    
  dataloader_args = dict(shuffle=True, batch_size=batchsize, num_workers=numworkers, pin_memory=True) if cuda else dict(shuffle=True, batch_size=64)
  trainloader = torch.utils.data.DataLoader(train_dataset, **dataloader_args)
  testloader = torch.utils.data.DataLoader(test_dataset, **dataloader_args)
  
  return trainloader, testloader