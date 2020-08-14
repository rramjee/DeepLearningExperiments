import torch
import torch.nn as nn
import torch.nn.functional as F



class CustomResnetBlock(nn.Module):
  
  def __init__(self, in_planes, out_planes):
    super(CustomResnetBlock, self).__init__()
    
    self.conv1 = nn.Sequential(
        nn.Conv2d(in_channels=in_planes, out_channels=out_planes, kernel_size=3, stride=1, padding=1, bias=False),
        nn.BatchNorm2d(out_planes),
        nn.ReLU(),
    ) 

    self.conv2 = nn.Sequential(
        nn.Conv2d(in_channels=out_planes, out_channels=out_planes, kernel_size=3, stride=1, padding=1, bias=False),
        nn.BatchNorm2d(out_planes),
        nn.ReLU(),
    ) 

    self.conv3 = nn.Sequential(
        nn.Conv2d(in_channels=out_planes, out_channels=out_planes, kernel_size=3, stride=1, padding=1, bias=False),
        nn.BatchNorm2d(out_planes),
    )

    self.conv4 = nn.Sequential(
        nn.Conv2d(in_channels=in_planes, out_channels=out_planes, kernel_size=3, stride=1, padding=1, bias=False),
        nn.BatchNorm2d(out_planes),
    )

  def forward(self, x):
    x_main = self.conv3(self.conv2(self.conv1(x)))
    x_shortcut = self.conv4(x)
    x_out = F.relu(x_main + x_shortcut)
    return x_out

class CustomSequentialBlock(nn.Module):
  
  def __init__(self, in_planes, out_planes):
    super(CustomSequentialBlock, self).__init__()
    
    self.conv1 = nn.Sequential(
        nn.Conv2d(in_channels=in_planes, out_channels=out_planes, kernel_size=3, stride=1, padding=1, bias=False),
        nn.BatchNorm2d(out_planes),
        nn.ReLU(),
    ) 

    self.conv2 = nn.Sequential(
        nn.Conv2d(in_channels=out_planes, out_channels=out_planes, kernel_size=3, stride=1, padding=1, bias=False),
        nn.BatchNorm2d(out_planes),
        nn.ReLU(),
    ) 

  def forward(self, x):
    x_out = self.conv2(self.conv1(x))
    return x_out

class CustomHeadBlock(nn.Module):
  
  def __init__(self, in_planes, out_planes):
    super(CustomHeadBlock, self).__init__()
    
    self.conv1 = nn.Sequential(
        nn.Conv2d(in_channels=in_planes, out_channels=in_planes, kernel_size=3, stride=1, padding=1, bias=False),
        nn.BatchNorm2d(in_planes),
        nn.ReLU(),
    ) 

    self.conv2 = nn.Sequential(
        nn.Conv2d(in_channels=in_planes, out_channels=in_planes, kernel_size=3, stride=1, padding=1, bias=False),
        nn.BatchNorm2d(in_planes),
        nn.ReLU(),
    ) 

    self.conv3 = nn.Sequential(
        nn.Conv2d(in_channels=in_planes, out_channels=out_planes, kernel_size=3, stride=1, padding=1, bias=False),
    ) 

  def forward(self, x):
    x_out = self.conv3(self.conv2(self.conv1(x)))
    return x_out


class CustomResNet(nn.Module):
  
  def __init__(self, inchannel):
    super(CustomResNet, self).__init__()
    self.planes = 32
    self.image_preplayer = nn.Sequential(
        nn.Conv2d(in_channels=inchannel, out_channels=self.planes, kernel_size=3, stride=1, padding=1, bias=False),
        nn.BatchNorm2d(self.planes),
        nn.ReLU(),
    )
    
    self.bg_preplayer = nn.Sequential(
        nn.Conv2d(in_channels=inchannel, out_channels=self.planes, kernel_size=3, stride=1, padding=1, bias=False),
        nn.BatchNorm2d(self.planes),
        nn.ReLU(),
    )

    self.resnetlayer1 = self._make_resnet_layer(self.planes, self.planes*2)
    self.seqlayer1 = self._make_sequential_layer(self.planes, self.planes*2)

    self.resnetlayer2 = self._make_resnet_layer(self.planes*2, self.planes*4)
    self.seqlayer2 = self._make_sequential_layer(self.planes*2, self.planes*4)


    self.midconv_layer = nn.Sequential(
        nn.Conv2d(in_channels=self.planes*8, out_channels=self.planes*8, kernel_size=3, stride=1, padding=1, bias=False),
        nn.BatchNorm2d(self.planes*8),
        nn.ReLU(),
    )

    self.maskheadlayer = self._make_head_layer(self.planes*8, 1)
    self.depthheadlayer = self._make_head_layer(self.planes*8, 1)

  def _make_resnet_layer(self, in_planes, out_planes):
    return CustomResnetBlock(in_planes, out_planes)

  def _make_sequential_layer(self, in_planes, out_planes):
    return CustomSequentialBlock(in_planes, out_planes)

  def _make_head_layer(self, in_planes, out_planes):
    return CustomHeadBlock(in_planes, out_planes)   

  def forward(self, bg, image):
    # Both Inputs pass through the input layer
    res_out = self.image_preplayer(image)
    seq_out = self.bg_preplayer(bg)

    # Both Inputs pass through their respective networks
    res_out = self.resnetlayer1(res_out)
    res_out = self.resnetlayer2(res_out)

    seq_out = self.seqlayer1(seq_out)
    seq_out = self.seqlayer2(seq_out)

    # Concat the Outputs from both the networks
    main_out = torch.cat([res_out, seq_out], dim=1)

    #main_out = self.midconv_layer(main_out)

    # Head for Mask Prediction
    mask_out = self.maskheadlayer(main_out)

    # Head for DepthMap Prediction
    depth_out = self.depthheadlayer(main_out)
   
    return mask_out, depth_out

def CustomNet15(inchannel):
    return CustomResNet(inchannel)    
    