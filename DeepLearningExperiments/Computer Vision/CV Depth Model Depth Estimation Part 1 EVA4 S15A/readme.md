# Session 15A Assignment:

## Dataset Link:
You can download the complete dataset from the google drive link below <br/> <br/>
[Dataset Download Link](https://drive.google.com/file/d/1w_5-yxq-blACNahl1moMzSuSf3z8DSAb/view?usp=sharing) <br/>
Filename: image_dataset.zip

## Background Images
<img src="bg/bg_21.jpg" width="150" > <img src="bg/bg_22.jpg" width="150" > <img src="bg/bg_23.jpg" width="150" > <img src="bg/bg_24.jpg" width="150" > <img src="bg/bg_25.jpg" width="150" > 

## Foreground Images
<img src="bg/fg_21.png" width="150" > <img src="bg/fg_22.png" width="150" > <img src="bg/fg_23.png" width="150" > <img src="bg/fg_24.png" width="150" > <img src="bg/fg_25.png" width="150" > 

## Foreground Mask Images
<img src="fg_mask/fg_21.jpg" width="150" > <img src="fg_mask/fg_22.jpg" width="150" > <img src="fg_mask/fg_23.jpg" width="150" > <img src="fg_mask/fg_24.jpg" width="150" > <img src="fg_mask/fg_25.jpg" width="150" > 

## Generated Images (superimpose foreground on background image)
<img src="fg_bg/fg_bg_21.jpg" width="150" > <img src="fg_bg/fg_bg_121.jpg" width="150" > <img src="fg_bg/fg_bg_221.jpg" width="150" > <img src="fg_bg/fg_bg_321.jpg" width="150" > <img src="fg_bg/fg_bg_421.jpg" width="150" > 

## Masks for Generated Images 
<img src="fg_bg_mask/fg_bg_mask_21.jpg" width="150" > <img src="fg_bg_mask/fg_bg_mask_121.jpg" width="150" > <img src="fg_bg_mask/fg_bg_mask_221.jpg" width="150" > <img src="fg_bg_mask/fg_bg_mask_321.jpg" width="150" > <img src="fg_bg_mask/fg_bg_mask_421.jpg" width="150" > 

## Depthmap for Generated Images
<img src="depthmap/depth_21.jpg" width="150" > <img src="depthmap/depth_121.jpg" width="150" > <img src="depthmap/depth_221.jpg" width="150" > <img src="depthmap/depth_321.jpg" width="150" > <img src="depthmap/depth_421.jpg" width="150" > 

## How it is created
* Background images (bg) : Downloaded from internet, resized to 220x220. --> 100 Images
* Foreground images (fg) : Downloaded from internet with mostly transparent images, removed the background using powerpoint, resized to 110x110. --> 100 Images
* Foreground Mask images (fg_mask) : This is created using code, also gimp video is available,
It will create the masks for the foreground --> 100 Images

Generated images:
Then used Dataset Generation notebook, uploaded the created images to gdrive and used.

This code takes created images as the input and create superimpose foreground images on the background. Each foreground images (total 100) and flipped (now total 200) are superimposed 20 times randomly on background images, so 200x20x100 = 400k images.
Also it will create respective 400k mask images.

Depthmap images:
These are generated using depthmap model, code is available. --> 400k Images

https://github.com/ialhashim/DenseDepth



### Dataset Statistics ###
| Image Type  | Mean | Standard Deviation |
| ----------- | ---------- | ---------------- |
| Generated Image  | [0.50169254 0.51531572 0.38720035] | [0.25096876 0.2417532 0.28520041]  |
| Generated Image Mask  | [0.09301607 0.09301607 0.09301607]  |  [0.28483643 0.28483643 0.28483643] |
| Depthmap Image   | [0.34092307 0.34092307 0.34092307]  | [0.23391564 0.23391564 0.23391564]  |

###  ###
