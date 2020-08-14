import numpy as np
import torch
import torchvision
import torchvision.transforms as transforms
from albumentations import PadIfNeeded, IAAFliplr, Compose, RandomCrop, Normalize, HorizontalFlip, Resize, ToFloat, Rotate, Cutout
from albumentations.pytorch import ToTensor


class album_Compose:
    def __init__(self, train=True):
        if train:
            self.albumentations_transform = Compose([
                                                     PadIfNeeded(min_height=40, min_width=40, always_apply=True, p=1.0),
                                                     RandomCrop(height=32, width=32, always_apply=True, p=1.0),
                                                     IAAFliplr(p=0.5),
                                                     Cutout(num_holes=1, max_h_size=8, max_w_size=8, p=0.5),
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


def load(albumentations=True):
	#Define the transformations for both Test & Train, we may use Data Augmentation, hence better to keep 2 functions for test & train

	if albumentations:
		train_transform = album_Compose(train=True)
		test_transform = album_Compose(train=False)
	else:
		# Transformation for Training
		train_transform = transforms.Compose(
    		[transforms.ToTensor(),
     		transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])

		# Transformation for Test
		test_transform = transforms.Compose(
    		[transforms.ToTensor(),
     		transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])

	#Get the Train and Test Set
	trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=train_transform)
	testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=test_transform)


	SEED = 1

	# CUDA?
	cuda = torch.cuda.is_available()
	print("CUDA Available?", cuda)

	# For reproducibility
	torch.manual_seed(SEED)

	if cuda:
			torch.cuda.manual_seed(SEED)

	# dataloader arguments - something you'll fetch these from cmdprmt
	dataloader_args = dict(shuffle=True, batch_size=512, num_workers=4, pin_memory=True) if cuda else dict(shuffle=True, batch_size=64)

	trainloader = torch.utils.data.DataLoader(trainset, **dataloader_args)
	testloader = torch.utils.data.DataLoader(testset, **dataloader_args)

	classes = ('plane', 'car', 'bird', 'cat',
    	       'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

	return classes, trainloader, testloader


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

