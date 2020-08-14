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
from torch.utils.data.sampler import SubsetRandomSampler
from torch.utils.data import Dataset, random_split
from PIL import Image

class album_Compose:
    def __init__(self, train=True):
        if train:
            self.albumentations_transform = Compose([
                                                     PadIfNeeded(min_height=72, min_width=72, always_apply=True, p=1.0),
                                                     RandomCrop(height=64, width=64, always_apply=True, p=1.0),
                                                     IAAFliplr(p=0.5),
                                                     Cutout(num_holes=3, max_h_size=16, max_w_size=16, p=0.8),
                                                     Normalize(mean=[0.49139968, 0.48215841, 0.44653091], std=[0.24703223, 0.24348513, 0.26158784],),
                                                     ToTensor()
                                                     ])
        else:
            self.albumentations_transform = Compose([
                                                     Normalize(mean=[0.49139968, 0.48215841, 0.44653091], std=[0.24703223, 0.24348513, 0.26158784],),
                                                     ToTensor()
                                                     ])

    def __call__(self, img):
        img = np.array(img)
        img = self.albumentations_transform(image=img)['image']
        return img

def load(datasetname, splitsize, batch_size=512, split=False, albumentations=True):
  random_seed = 42
  
  if datasetname == 'cifar10':
    mean_tuple = (0.485, 0.456, 0.406)
    std_tuple = (0.229, 0.224, 0.225)
  elif datasetname == 'tinyimagenet':
    mean_tuple = (0.485, 0.456, 0.406)
    std_tuple = (0.229, 0.224, 0.225)

  if albumentations:
    train_transform = album_Compose(train=True)
    test_transform = album_Compose(train=False)
  else:
    # Transformation for Training
    train_transform = transforms.Compose([transforms.ToTensor(),
                                          transforms.Normalize(mean_tuple, std_tuple)])
        # Transformation for Test
    test_transform = transforms.Compose([transforms.ToTensor(), 
                                       transforms.Normalize(mean_tuple, std_tuple)])

  if datasetname == 'cifar10':
    #Get the Train and Test Set
    trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=train_transform)
    testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=test_transform)
    classes = ('plane', 'car', 'bird', 'cat',
               'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
  elif datasetname == 'tinyimagenet':
    down_url  = "http://cs231n.stanford.edu/tiny-imagenet-200.zip"
    dataset = TinyImageNetDataset(down_url)
    classes = dataset.classes
    train_len = len(dataset)*splitsize//100
    test_len = len(dataset) - train_len 
    train_set, val_set = random_split(dataset, [train_len, test_len])
    train_dataset = DatasetFromSubset(train_set, transform=train_transform)
    test_dataset = DatasetFromSubset(val_set, transform=test_transform)


  # CUDA?
  cuda = torch.cuda.is_available()
  print("CUDA Available?", cuda)

    # For reproducibility
  torch.manual_seed(random_seed)

  if cuda:
    torch.cuda.manual_seed(random_seed) 

    dataloader_args = dict(shuffle=True, batch_size=batch_size, num_workers=4, pin_memory=True) if cuda else dict(shuffle=True, batch_size=64)
    trainloader = torch.utils.data.DataLoader(train_dataset, **dataloader_args)
    testloader = torch.utils.data.DataLoader(test_dataset, **dataloader_args)
       

  return classes, trainloader, testloader


class TinyImageNetDataset(Dataset):
    def __init__(self, url):
        self.data = []
        self.target = []
        self.classes = []
        self.path = 'tiny-imagenet-200'
        
        self.download_dataset(url)
        
        wnids = open(f"{self.path}/wnids.txt", "r")
        for line in wnids:
          self.classes.append(line.strip())
        wnids.close()  

        wnids = open(f"{self.path}/wnids.txt", "r")
        
        for wclass in notebook.tqdm(wnids, desc='Loading Train Folder', total = 200):
          wclass = wclass.strip()
          for i in os.listdir(self.path+'/train/'+wclass+'/images/'):
            img = Image.open(self.path+"/train/"+wclass+"/images/"+i)
            npimg = np.asarray(img)
            if(len(npimg.shape) ==2):
              npimg = np.repeat(npimg[:, :, np.newaxis], 3, axis=2)
            self.data.append(npimg)  
            self.target.append(self.classes.index(wclass))

        val_file = open(f"{self.path}/val/val_annotations.txt", "r")
        for i in notebook.tqdm(val_file,desc='Loading Test Folder',total =10000):
          split_img, split_class = i.strip().split("\t")[:2]
          img = Image.open(f"{self.path}/val/images/{split_img}")
          npimg = np.asarray(img)
          if(len(npimg.shape) ==2):        
            npimg = np.repeat(npimg[:, :, np.newaxis], 3, axis=2)
          self.data.append(npimg)  
          self.target.append(self.classes.index(split_class))
            
    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        data = self.data[idx]
        target = self.target[idx]
        img = data     
        return data,target
    
    def classes(self):
      return self.classes    
    
    def download_dataset(self, url):
      if (os.path.isdir("tiny-imagenet-200")):
        print ('Images already downloaded...')
        return
      r = requests.get(url, stream=True)
      print ('Downloading TinyImageNet Data' )
      zip_ref = zipfile.ZipFile(BytesIO(r.content))
      for file in notebook.tqdm(iterable=zip_ref.namelist(), total=len(zip_ref.namelist())):
        zip_ref.extract(member = file)
      zip_ref.close()

class DatasetFromSubset(Dataset):
    def __init__(self, subset, transform=None):
        self.subset = subset
        self.transform = transform

    def __getitem__(self, index):
        x, y = self.subset[index]
        if self.transform:
            x = self.transform(x)
        return x, y

    def __len__(self):
        return len(self.subset)


#Old Album compose
#class album_Compose:
#    def __init__(self, train=True):
#        if train:
#            self.albumentations_transform = Compose([
#                                                     Rotate(limit=20, p=0.5),
#                                                     HorizontalFlip(),
#                                                     Cutout(num_holes=3, max_h_size=8, max_w_size=8, p=0.5),
#                                                     Normalize(mean=[0.49139968, 0.48215841, 0.44653091], std=[0.24703223, 0.24348513, 0.26158784],),
#                                                     ToTensor()
#                                                     ])
#        else:
#            self.albumentations_transform = Compose([
#                                                     Normalize(mean=[0.49139968, 0.48215841, 0.44653091], std=[0.24703223, 0.24348513, 0.26158784],),
#                                                     ToTensor()
#                                                     ])
#
#    def __call__(self, img):
#        img = np.array(img)
#        img = self.albumentations_transform(image=img)['image']
#        return img
#       

