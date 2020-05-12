```
@inproceedings{Gupta_2019_ICCV,
author = {Gupta, Puneet and Rahtu, Esa},
booktitle = {The IEEE International Conference on Computer Vision (ICCV)},
month = {oct},
title = {{CIIDefence: Defeating Adversarial Attacks by Fusing Class-Specific Image Inpainting and Image Denoising}},
year = {2019}
}
```
![](../pics/fig1_Gupta_2019_ICCV.png)

One of the key ideas in CIIDefence is to select those using Class Activation Map (CAM) technique that pinpoints the image parts most influential to the classification outcome.

Finally, we fuse our inpaint- ing based defence with wavelet based image denoising [1] to further improve the results. In addition, this combination provides a non-differentiable layer that turns out to be diffi- cult to approximate with simple differentiable alternatives

[1] Prakash, A., Moran, N., Garber, S., DiLillo, A., & Storer, J. A. (2018). Deflecting Adversarial Attacks With Pixel Deflection. 2018 {IEEE} Conference on Computer Vision and Pattern Recognition, {CVPR} 2018, Salt Lake City, UT, USA, June 18-22, 2018, 8571–8580. https://doi.org/10.1109/CVPR.2018.00894