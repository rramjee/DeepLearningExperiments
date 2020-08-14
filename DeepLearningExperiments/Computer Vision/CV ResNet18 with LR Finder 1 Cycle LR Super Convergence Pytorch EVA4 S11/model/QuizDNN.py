import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        # Input Block
        self.convblock1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=16, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),
            nn.BatchNorm2d(16),
        )  

        # Convolution Block 1
        self.convblock2 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=16, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),
            nn.BatchNorm2d(16),
        ) 

        self.convblock3 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=16, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),
            nn.BatchNorm2d(16),
        ) 


        # Max Pool 1
        self.pool1 = nn.MaxPool2d(2, 2) # output_size = 16, receptive field: 8

        # Convolution Block 2
        self.convblock4 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=16, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),
            nn.BatchNorm2d(16),
        ) 

        self.convblock5 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=16, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),
            nn.BatchNorm2d(16),
        ) 

        # Max Pool 2
        self.pool2 = nn.MaxPool2d(2, 2) # output_size = 8, receptive field: 18

        # Convolution Block 3
        self.convblock6 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=16, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),
            nn.BatchNorm2d(16),
        ) 

        self.convblock7 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=16, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),
            nn.BatchNorm2d(16),
        ) 


        # Max Pool 3
        self.pool3 = nn.MaxPool2d(2, 2) # output_size = 4, receptive field: 38

        # Convolution Block 4
        self.convblock8 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=16, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),
            nn.BatchNorm2d(16),
        ) 

        self.convblock9 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=16, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),
            nn.BatchNorm2d(16),
        ) 

        # Output Block 
        self.gap = nn.Sequential(
            nn.AvgPool2d(kernel_size=8)
        ) 

        self.convblock10 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=10, kernel_size=(1, 1), padding=0, bias=False),
        ) 

    def forward(self, x): 
        x1 = self.convblock1(x)
        x2 = self.convblock2(x1)
        x3 = self.convblock3(x1 + x2)     
        x4 = self.pool1(x1 + x2 + x3)

        x5 = self.convblock4(x4)

        x6 = self.convblock5(x4 + x5)
        x7 = self.convblock6(x4 + x5 + x6)

        x8 = self.pool1(x5 + x6 + x7)

        x9 = self.convblock7(x8)

        x10 = self.convblock8(x8 + x9)
        x11 = self.convblock9(x8 + x9 + x10)
        x12 = self.gap(x11)
        x13 = self.convblock10(x12)       

        return F.log_softmax(x, dim=-1)