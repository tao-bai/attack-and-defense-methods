```
@inproceedings{Inkawhich_2019_CVPR,
author = {Inkawhich, Nathan and Wen, Wei and Li, Hai (Helen) and Chen, Yiran},
booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
month = {jun},
title = {{Feature Space Perturbations Yield More Transferable Adversarial Examples}},
year = {2019}
}
```

This paper investigated the influence of feature space on adversarial examples's transferability. They proposed a new attack method for better transferability. The loss function is designed as the Euclidean distance between the vectorized source image activations and vectorized target image activations at some layer L. if two images is similar at some hidden layers, they are likely to be classified as one class. Based on this loss function, the image will be modified.

They also did some experiments to investigate which layer is the best layer to be involved in the loss function. They mesured the Euclidean distance between original images purturbed images from two perspectives: image domain and the first two principal component directions. Details are in Section 6.3.