from ipywidgets import HBox, Label, IntProgress
import time
from IPython.display import display
from tqdm import tqdm_notebook as tqdm
import torch
#Training & Testing Loops
from tqdm import tqdm
from tqdm import notebook
import torch.nn as nn
import torch.optim as optim
from torch.optim.lr_scheduler import StepLR
from matplotlib import pyplot as plt
import cv2
import kornia
import numpy as np
from utils import visualize
from utils import dice
from utils import customloss
import torchvision


train_losses = []
test_losses = []
test_miou_masks = []
test_miou_depths = []


def train_model(status, epoch, model, device, train_loader, criterion_mask, criterion_depth, optimizer, depthweight= 0.5, printtestimg = False, printinterval=2000, scheduler=False):
  model.train()
  pbar = notebook.tqdm(train_loader)
  for batch_idx, (bg, image, mask, depthmap) in enumerate(pbar):
    bg, image, mask, depthmap = bg.to(device), image.to(device), mask.to(device), depthmap.to(device)
    # Init
    optimizer.zero_grad()
    # Predict
    predmask, preddepth = model(bg, image)

    loss_mask = criterion_mask(predmask, mask)
    #loss_depth = criterion_depth(preddepth, depthmap)
    loss_depth = customloss.depth_loss(preddepth, depthmap, criterion_depth)
    loss = ((1-depthweight) * loss_mask) + (depthweight * loss_depth)
    train_losses.append(loss)
    
    # Backpropagation
    loss.backward()
    optimizer.step()
    if(scheduler):
        scheduler.step(loss)
    
    pbar.set_description(desc= f'Loss={loss.item()} Batch_id={batch_idx}') 
    status.value = f'epoch={epoch}, Batch_id={batch_idx}, Loss={loss}, Mask={loss_mask}, Depth={loss_depth}'
    
    if batch_idx % 500 == 0:
      torch.cuda.empty_cache()

    if printtestimg:
      if batch_idx % printinterval == 0:
        print('*********************** TRAINING *******************')
        print('======================= IMAGE ======================')
        print('image:', image.shape)
        visualize.show_img(torchvision.utils.make_grid(image.detach().cpu()[1:5]), 8)
        print('======================= MASK =======================')
        print('actual:', mask.shape)
        visualize.show_img(torchvision.utils.make_grid(mask.detach().cpu()[1:5]), 8)
        print('predicted:', predmask.shape)
        visualize.show_img(torchvision.utils.make_grid(predmask.detach().cpu()[1:5]), 8)
        print('======================= DEPTHMAP ===================')
        print('actual:', depthmap.shape)
        visualize.show_img(torchvision.utils.make_grid(depthmap.detach().cpu()[1:5]), 8)
        print('predicted:', preddepth.shape)
        visualize.show_img(torchvision.utils.make_grid(preddepth.detach().cpu()[1:5]), 8)
  return train_losses

def test_model(model, device, criterion_mask, criterion_depth, test_loader, depthweight= 0.5):
  model.eval()
  datalength = len(test_loader)
  dice_mask = 0
  dice_depth = 0
  final_dice_mask = 0
  final_dice_depth = 0
  with torch.no_grad():
    pbar = notebook.tqdm(test_loader)
    for batch_idx, (bg, image, mask, depthmap) in enumerate(pbar):
      bg, image, mask, depthmap = bg.to(device), image.to(device), mask.to(device), depthmap.to(device)
      predmask, preddepth = model(bg, image)
      
      loss_mask = criterion_mask(predmask, mask)
      loss_depth = criterion_depth(preddepth, depthmap)

      total_loss = ((1-depthweight) * loss_mask) + (depthweight * loss_depth)
      test_losses.append(total_loss) 

      #Calculate Dice Coeff for Mask
      pred_m = torch.sigmoid(predmask)
      pred_m = (pred_m > 0.5).float()
      dice_mask += dice.dice_coeff(pred_m, mask).item()

      #Calculate Dice Coeff for Depthmap
      dice_depth += dice.dice_coeff(preddepth, depthmap).item()
      
      pbar.set_description(desc= f'Loss={total_loss}')

    final_dice_mask = dice_mask / datalength
    final_dice_depth = dice_depth / datalength
    print('*********************** TEST ***********************')
    print('Mask Dice Coeff: ', final_dice_mask, 'Depthmap Dice Coeff: ', final_dice_depth)
    print('======================= IMAGE ======================')
    print('image:', image.shape)
    visualize.show_img(torchvision.utils.make_grid(image.detach().cpu()[1:5]), 8)
    print('======================= MASK =======================')
    print('actual:', mask.shape)
    visualize.show_img(torchvision.utils.make_grid(mask.detach().cpu()[1:5]), 8)
    print('predicted:', predmask.shape)
    visualize.show_img(torchvision.utils.make_grid(predmask.detach().cpu()[1:5]), 8)
    print('======================= DEPTHMAP ===================')
    print('actual:', depthmap.shape)
    visualize.show_img(torchvision.utils.make_grid(depthmap.detach().cpu()[1:5]), 8)
    print('predicted:', preddepth.shape)
    visualize.show_img(torchvision.utils.make_grid(preddepth.detach().cpu()[1:5]), 8)
    return test_losses,  final_dice_mask, final_dice_depth