```
@inproceedings{DBLP:conf/cvpr/XieWMYH19,
author = {Xie, Cihang and Wu, Yuxin and van der Maaten, Laurens and Yuille, Alan L and He, Kaiming},
booktitle = {{\{}IEEE{\}} Conference on Computer Vision and Pattern Recognition, {\{}CVPR{\}} 2019, Long Beach, CA, USA, June 16-20, 2019},
pages = {501--509},
publisher = {Computer Vision Foundation / {\{}IEEE{\}}},
title = {{Feature Denoising for Improving Adversarial Robustness}},
url = {http://openaccess.thecvf.com/content{\_}CVPR{\_}2019/html/Xie{\_}Feature{\_}Denoising{\_}for{\_}Improving{\_}Adversarial{\_}Robustness{\_}CVPR{\_}2019{\_}paper.html},
year = {2019}
}
```
## Motivation
Adversarial purturbations on images lead to noise in the features constructed by these networks.

## Methods
They developed new network architectures that increase adversarial robustness by performing feature denoising. Specifically, their networks contains blocks that denoise the features using non-means or other filters and the networks are trained end-to-end combined with adversarial training.

The denoising block processes the input features by a denosing operation, such as non-local means or other variants. The denoised representation is first processed by a 1x1 convolutional layer, and then added to the block's input via a residual connection.
Only the non-local means operation in the denoising block is actually doing the denoising; the 1x1 convolutions and the residual connection are mainly for feature combination. The authors however presented the effectiveness of both residual connection and 1x1 convolution.